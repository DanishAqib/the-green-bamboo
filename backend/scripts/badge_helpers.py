from datetime import datetime, timedelta

def check_and_award_badge(conn, user_id, action_type, related_entity=None, entity_id=None, entity_type=None, badge_type=None):
    """
    Check if user qualifies for a badge update and process accordingly
    
    Parameters:
    - action_type: The type of action ('Review', 'ExtensiveReview', etc)
    - related_entity: For country/category/type specific badges (e.g., 'Japan', 'Rum / Rhum')
    - entity_id: The ID of the associated entity (e.g., review ID)
    - entity_type: The type of entity (e.g., 'review')
    - badge_type: Explicitly specify the badge type ('Country', 'DrinkType', 'Category', 'Action')
    """
    print(f"Checking badge: action_type={action_type}, related_entity={related_entity}, badge_type={badge_type}")
    
    # First, record the action
    record_badge_action(conn, user_id, action_type, related_entity, entity_id, entity_type)
    
    # For review with related entity, handle as specific badge type
    if related_entity is not None:
        # If badge_type is explicitly provided, use it
        if badge_type:
            print(f"Processing {badge_type} badge for {related_entity}")
            return update_related_entity_badge(conn, user_id, badge_type, related_entity, action_type)
        else:
            # Fallback to determining badge type (shouldn't happen with our updated code)
            badge_type = determine_badge_type(conn, related_entity)
            if badge_type:
                print(f"Determined {badge_type} badge for {related_entity}")
                return update_related_entity_badge(conn, user_id, badge_type, related_entity, action_type)
            else:
                print(f"Could not determine badge type for {related_entity}, skipping")
                return []
    
    # For general action badges
    if badge_type == 'Action' or badge_type is None:
        print(f"Processing action badge for {action_type}")
        return update_action_badge(conn, user_id, action_type)
    
    return []

def determine_badge_type(conn, related_entity):
    """Determine the type of badge based on the related entity"""
    with conn.cursor() as cur:
        # Check if it's a country (most specific check first)
        cur.execute("SELECT COUNT(*) FROM \"listings\" WHERE \"originCountry\" = %s", (related_entity,))
        if cur.fetchone()['count'] > 0:
            return 'Country'
            
        # Check if it's a drink type
        cur.execute("SELECT COUNT(*) FROM \"listings\" WHERE \"drinkType\" = %s", (related_entity,))
        if cur.fetchone()['count'] > 0:
            return 'DrinkType'
            
        # Check if it's a category
        cur.execute("SELECT COUNT(*) FROM \"listings\" WHERE \"typeCategory\" = %s", (related_entity,))
        if cur.fetchone()['count'] > 0:
            return 'Category'
            
        # If we can't determine the type, return None
        return None

# Helper functions to get all countries and drink types
def get_all_countries(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT \"originCountry\" FROM \"listings\"")
        return [row['originCountry'] for row in cur.fetchall()]
        
def get_all_drink_types(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT DISTINCT \"drinkType\" FROM \"listings\"")
        return [row['drinkType'] for row in cur.fetchall()]

def record_badge_action(conn, user_id, action_type, related_entity=None, entity_id=None, entity_type=None):
    """Record a badge-worthy action for a user"""
    with conn.cursor() as cur:
        print(f"Recording action: {action_type} for user {user_id} with entity {related_entity}")
        cur.execute("""
            INSERT INTO "badgeActions" 
            ("userId", "actionType", "relatedEntity", "entityId", "entityType", "createdDate")
            VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP)
        """, (user_id, action_type, related_entity, entity_id, entity_type))
        conn.commit()

def calculate_badge_level(conn, action_count, action_type):
    """
    Calculate badge level and progress based on action count
    
    Parameters:
    - action_count: The total number of actions performed
    - action_type: The type of action
    
    Returns:
    - A tuple of (level, progress) where:
      - level: The current badge level
      - progress: The progress toward the next level
    """
    with conn.cursor() as cur:
        # Get all badge rules for this action type
        cur.execute("""
            SELECT "levelStart", "levelEnd", "actionsRequired" FROM "badgeRules"
            WHERE "actionType" = %s
            ORDER BY "levelStart" ASC
        """, (action_type,))
        rules = cur.fetchall()
        
        if not rules:
            print(f"No badge rules found for action type: {action_type}")
            return 1, 0  # Default to level 1, progress 0
        
        # Tracks actions used to reach current level
        actions_used = 0
        current_level = 1
        
        # Initialize to handle case where we haven't achieved any levels
        total_actions_for_next_level = 0
        
        # Process each range of levels
        for rule in rules:
            level_start = rule['levelStart']
            level_end = rule['levelEnd']
            actions_required = rule['actionsRequired']
            
            # Calculate how many levels this rule applies to
            levels_in_range = level_end - level_start + 1
            
            # Calculate total actions needed for all levels in this range
            total_actions_in_range = levels_in_range * actions_required
            
            # If we don't have enough actions for all levels in this range
            if action_count - actions_used < total_actions_in_range:
                # How many complete levels we can achieve in this range
                complete_levels = (action_count - actions_used) // actions_required
                
                # Update current level based on complete levels in this range
                current_level = level_start + complete_levels
                
                # Calculate progress toward next level
                actions_for_complete_levels = complete_levels * actions_required
                progress = (action_count - actions_used) - actions_for_complete_levels
                
                # Return level and progress
                return min(current_level, 100), progress
            
            # We have enough actions for all levels in this range
            current_level = level_end + 1
            actions_used += total_actions_in_range
            
            # If this is the last rule, store actions required for next level
            if rule == rules[-1]:
                total_actions_for_next_level = actions_required
        
        # If we processed all rules and still have actions left
        remaining_actions = action_count - actions_used
        
        # Cap at level 100
        current_level = min(current_level, 100)
        
        # If at max level, return all remaining actions as progress
        if current_level == 100:
            return current_level, remaining_actions
        
        # For the case when we've used all rules but have remaining actions
        # and we know actions required for next level
        if total_actions_for_next_level > 0:
            complete_extra_levels = remaining_actions // total_actions_for_next_level
            current_level += complete_extra_levels
            progress = remaining_actions % total_actions_for_next_level
            return min(current_level, 100), progress
        
        # Default case
        return current_level, 0

def update_related_entity_badge(conn, user_id, badge_type, related_entity, action_type):
    """
    Update badges related to countries, drink types, and categories
    
    Parameters:
    - badge_type: The type of badge ('Country', 'DrinkType', 'Category')
    - related_entity: The specific entity (e.g., country name, drink type)
    - action_type: The type of action (usually 'Review')
    """
    if not related_entity:
        print(f"No related entity provided for {badge_type}")
        return []
    
    updates = []
    with conn.cursor() as cur:
        # Find the appropriate badge for this entity
        cur.execute("""
            SELECT id, "badgeLevel" FROM "badges"
            WHERE "badgeType" = %s AND "relatedEntity" = %s
            ORDER BY "badgeLevel" DESC
            LIMIT 1
        """, (badge_type, related_entity))
        
        badge_row = cur.fetchone()
        
        # If badge doesn't exist, skip it instead of creating a new one
        if not badge_row:
            print(f"No badge exists for {badge_type}: {related_entity}, skipping")
            return []
            
        badge_id = badge_row['id']
        
        # Count actions for this entity
        cur.execute("""
            SELECT COUNT(*) as count FROM "badgeActions"
            WHERE "userId" = %s AND "actionType" = %s AND "relatedEntity" = %s
        """, (user_id, action_type, related_entity))
        
        action_count = cur.fetchone()['count']
        print(f"User has {action_count} {action_type} actions for {related_entity}")
        
        # Calculate the new level and progress
        new_level, new_progress = calculate_badge_level(conn, action_count, action_type)
        print(f"Calculated new level: {new_level}, new progress: {new_progress}")
        
        # Get current user badge status
        cur.execute("""
            SELECT id, "currentLevel", "currentProgress" FROM "userBadges"
            WHERE "userId" = %s AND "badgeId" = %s
        """, (user_id, badge_id))
        
        user_badge = cur.fetchone()
        
        # Update badge if necessary
        if user_badge:
            current_level = user_badge['currentLevel']
            current_progress = user_badge['currentProgress']
            
            # Only update if there's a change
            if new_level != current_level or new_progress != current_progress:
                cur.execute("""
                    UPDATE "userBadges"
                    SET "currentLevel" = %s, "currentProgress" = %s, "lastUpdated" = CURRENT_TIMESTAMP
                    WHERE id = %s
                """, (new_level, new_progress, user_badge['id']))
                
                if new_level != current_level:
                    updates.append((badge_id, current_level, new_level))
                    print(f"Updated badge level: {current_level} -> {new_level}")
            
        else:
            # User doesn't have this badge yet, create it
            cur.execute("""
                INSERT INTO "userBadges" ("userId", "badgeId", "currentLevel", "currentProgress", "dateEarned")
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
            """, (user_id, badge_id, new_level, new_progress))
            
            if new_level > 1:
                updates.append((badge_id, 0, new_level))
            else:
                updates.append((badge_id, 0, 1))
        
        conn.commit()
        
    return updates

def update_action_badge(conn, user_id, action_type):
    """
    Update badges related to general actions
    
    Parameters:
    - action_type: The type of action (e.g., 'Review', 'ExtensiveReview')
    """
    updates = []
    with conn.cursor() as cur:
        # Find the general action badge for this action type
        cur.execute("""
            SELECT id FROM "badges"
            WHERE "badgeType" = 'Action' AND "relatedEntity" = %s
            ORDER BY "badgeLevel" ASC
            LIMIT 1
        """, (action_type,))
        
        badge_row = cur.fetchone()
        
        # If badge doesn't exist, skip it
        if not badge_row:
            print(f"No action badge exists for {action_type}, skipping")
            return []
            
        badge_id = badge_row['id']
        
        # Count actions for this type
        cur.execute("""
            SELECT COUNT(*) as count FROM "badgeActions"
            WHERE "userId" = %s AND "actionType" = %s
        """, (user_id, action_type))
        
        action_count = cur.fetchone()['count']
        print(f"User has {action_count} actions of type {action_type}")
        
        # Calculate the new level and progress
        new_level, new_progress = calculate_badge_level(conn, action_count, action_type)
        print(f"Calculated new level: {new_level}, new progress: {new_progress}")
        
        # Get current user badge status
        cur.execute("""
            SELECT id, "currentLevel", "currentProgress" FROM "userBadges"
            WHERE "userId" = %s AND "badgeId" = %s
        """, (user_id, badge_id))
        
        user_badge = cur.fetchone()
        
        # Update badge if necessary
        if user_badge:
            current_level = user_badge['currentLevel']
            current_progress = user_badge['currentProgress']
            
            # Only update if there's a change
            if new_level != current_level or new_progress != current_progress:
                cur.execute("""
                    UPDATE "userBadges"
                    SET "currentLevel" = %s, "currentProgress" = %s, "lastUpdated" = CURRENT_TIMESTAMP
                    WHERE id = %s
                """, (new_level, new_progress, user_badge['id']))
                
                if new_level != current_level:
                    updates.append((badge_id, current_level, new_level))
                    print(f"Updated badge level: {current_level} -> {new_level}")
            
        else:
            # User doesn't have this badge yet, create it
            cur.execute("""
                INSERT INTO "userBadges" ("userId", "badgeId", "currentLevel", "currentProgress", "dateEarned")
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
            """, (user_id, badge_id, new_level, new_progress))
            
            if new_level > 1:
                updates.append((badge_id, 0, new_level))
            else:
                updates.append((badge_id, 0, 1))
        
        conn.commit()
        
    return updates

def remove_badge_action(conn, user_id, action_type, related_entity=None, entity_id=None, entity_type=None):
    
    updates = []
    
    try:
        with conn.cursor() as cur:
            # Step 1: Delete the badge action
            print(f"Removing badge action: userId={user_id}, action={action_type}, entity={related_entity}, id={entity_id}")
            
            if entity_id and entity_type:
                if related_entity:
                    query = """
                        DELETE FROM "badgeActions"
                        WHERE "userId" = %s 
                        AND "actionType" = %s 
                        AND "relatedEntity" = %s 
                        AND "entityId" = %s 
                        AND "entityType" = %s
                    """
                    params = (user_id, action_type, related_entity, entity_id, entity_type)
                else:
                    query = """
                        DELETE FROM "badgeActions"
                        WHERE "userId" = %s 
                        AND "actionType" = %s 
                        AND "entityId" = %s 
                        AND "entityType" = %s
                    """
                    params = (user_id, action_type, entity_id, entity_type)
            else:
                if related_entity:
                    query = """
                        DELETE FROM "badgeActions"
                        WHERE "userId" = %s 
                        AND "actionType" = %s 
                        AND "relatedEntity" = %s
                    """
                    params = (user_id, action_type, related_entity)
                else:
                    query = """
                        DELETE FROM "badgeActions"
                        WHERE "userId" = %s 
                        AND "actionType" = %s
                    """
                    params = (user_id, action_type)
            
            cur.execute(query, params)
            deleted_count = cur.rowcount
            print(f"Deleted {deleted_count} badge actions")
            
            if deleted_count == 0:
                # No action was deleted, nothing to update
                return []
            
            # Step 2: Find affected badges
            affected_badges = []
            
            # Check different badge types that might be affected
            if action_type == 'Review':
                # This could affect country, drink type, category, or general review badges
                
                # Find country badge if applicable
                if related_entity:
                    # Check if it's a country
                    cur.execute("""
                        SELECT id FROM "badges"
                        WHERE "badgeType" = 'Country' AND "relatedEntity" = %s
                    """, (related_entity,))
                    country_badge = cur.fetchone()
                    if country_badge:
                        affected_badges.append(('Country', country_badge['id'], related_entity))
                    
                    # Check if it's a drink type
                    cur.execute("""
                        SELECT id FROM "badges"
                        WHERE "badgeType" = 'DrinkType' AND "relatedEntity" = %s
                    """, (related_entity,))
                    drink_type_badge = cur.fetchone()
                    if drink_type_badge:
                        affected_badges.append(('DrinkType', drink_type_badge['id'], related_entity))
                    
                    # Check if it's a category
                    cur.execute("""
                        SELECT id FROM "badges"
                        WHERE "badgeType" = 'Category' AND "relatedEntity" = %s
                    """, (related_entity,))
                    category_badge = cur.fetchone()
                    if category_badge:
                        affected_badges.append(('Category', category_badge['id'], related_entity))
                
                # Always check general review badge
                cur.execute("""
                    SELECT id FROM "badges"
                    WHERE "badgeType" = 'Action' AND "relatedEntity" = 'Review'
                """)
                review_badge = cur.fetchone()
                if review_badge:
                    affected_badges.append(('Action', review_badge['id'], 'Review'))
            else:
                # Action-specific badge
                cur.execute("""
                    SELECT id FROM "badges"
                    WHERE "badgeType" = 'Action' AND "relatedEntity" = %s
                """, (action_type,))
                action_badge = cur.fetchone()
                if action_badge:
                    affected_badges.append(('Action', action_badge['id'], action_type))
            
            print(f"Found {len(affected_badges)} affected badges: {affected_badges}")
            
            # Step 3: Process each affected badge
            for badge_type, badge_id, badge_entity in affected_badges:
                # Get user's current badge level
                cur.execute("""
                    SELECT id, "currentLevel" FROM "userBadges"
                    WHERE "userId" = %s AND "badgeId" = %s
                """, (user_id, badge_id))
                
                user_badge = cur.fetchone()
                if not user_badge:
                    continue
                
                old_level = user_badge['currentLevel']
                
                # Count remaining actions
                if badge_type in ['Country', 'DrinkType', 'Category']:
                    # For entity badges, count reviews for that entity
                    count_query = """
                        SELECT COUNT(*) FROM "badgeActions"
                        WHERE "userId" = %s AND "actionType" = 'Review' AND "relatedEntity" = %s
                    """
                    count_params = (user_id, badge_entity)
                else:
                    # For action badges, count actions of that type
                    count_query = """
                        SELECT COUNT(*) FROM "badgeActions"
                        WHERE "userId" = %s AND "actionType" = %s
                    """
                    count_params = (user_id, badge_entity)
                
                cur.execute(count_query, count_params)
                action_count = cur.fetchone()['count']
                
                print(f"Badge {badge_id} ({badge_type} - {badge_entity}) has {action_count} remaining actions")
                
                # CRITICAL FIX: Force badge deletion for zero actions
                if action_count == 0:
                    print(f"DELETING badge {badge_id} for user {user_id}")
                    # Force delete the badge
                    cur.execute('DELETE FROM "userBadges" WHERE id = %s', (user_badge['id'],))
                    updates.append((badge_id, old_level, 0))
                else:
                    # Recalculate level for non-zero counts (simplified)
                    # This could be expanded for more accurate level calculation
                    new_level = max(1, action_count // 2)  # Simple formula for demo
                    if new_level != old_level:
                        cur.execute("""
                            UPDATE "userBadges"
                            SET "currentLevel" = %s, "lastUpdated" = CURRENT_TIMESTAMP
                            WHERE id = %s
                        """, (new_level, user_badge['id']))
                        updates.append((badge_id, old_level, new_level))
            
            conn.commit()
            
    except Exception as e:
        conn.rollback()
        print(f"Error in remove_badge_action: {str(e)}")
        import traceback
        traceback.print_exc()
    
    return updates

def process_badges_for_review(conn, user_id, review_data, review_id):
    """Process all badges related to a review"""
    updates = []
    
    try:
        # 1. Get drink info for the review
        with conn.cursor() as cur:
            cur.execute("""
                SELECT l."drinkType", l."typeCategory", l."originCountry"
                FROM "listings" l
                WHERE l."id" = %s
            """, (review_data['reviewTarget'],))
            
            drink_info = cur.fetchone()
            if not drink_info:
                print(f"No drink info found for review target: {review_data['reviewTarget']}")
                return []
            
            print(f"Processing badges for drink: {drink_info}")
                
            # Record the review action for country badge
            if drink_info['originCountry']:
                country_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'Review',
                    drink_info['originCountry'], 
                    review_id, 
                    'review',
                    'Country'  # Explicitly specify badge type
                )
                updates.extend(country_updates)
            
            # Record the review action for drink type badge
            if drink_info['drinkType']:
                drink_type_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'Review',
                    drink_info['drinkType'],
                    review_id, 
                    'review',
                    'DrinkType'  # Explicitly specify badge type
                )
                updates.extend(drink_type_updates)
            
            # Record the review action for category badge
            if drink_info['typeCategory']:
                category_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'Review',
                    drink_info['typeCategory'], 
                    review_id, 
                    'review',
                    'Category'  # Explicitly specify badge type
                )
                updates.extend(category_updates)
            
            # General review action (no specific related entity)
            review_updates = check_and_award_badge(
                conn, 
                user_id, 
                'Review', 
                None, 
                review_id, 
                'review',
                'Action'  # Explicitly specify badge type
            )
            updates.extend(review_updates)
            
            # 2. Extensive Review badge
            if (review_data.get('finish') or review_data.get('colour') or 
                review_data.get('aroma') or review_data.get('taste')):
                extensive_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'ExtensiveReview', 
                    None, 
                    review_id, 
                    'review',
                    'Action'  # Explicitly specify badge type
                )
                updates.extend(extensive_updates)
            
            # 3. Photo badge
            if review_data.get('photo'):
                photo_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'PhotoAttached', 
                    None, 
                    review_id, 
                    'review',
                    'Action'  # Explicitly specify badge type
                )
                updates.extend(photo_updates)
                
            # 4. Location badge
            if review_data.get('location') or review_data.get('address'):
                location_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'LocationTagged', 
                    None, 
                    review_id, 
                    'review',
                    'Action'  # Explicitly specify badge type
                )
                updates.extend(location_updates)
                
            # 5. Friend tagged badge
            if review_data.get('taggedUsers'):
                friend_updates = check_and_award_badge(
                    conn, 
                    user_id, 
                    'FriendTagged', 
                    None, 
                    review_id, 
                    'review',
                    'Action'  # Explicitly specify badge type
                )
                updates.extend(friend_updates)
        
        conn.commit()
        return updates
    
    except Exception as e:
        conn.rollback()
        print(f"Error processing badges: {str(e)}")
        return []

def process_badges_for_review_edit(conn, user_id, old_review, new_review, review_id):
    """
    Process badge changes when a review is edited
    Returns list of badge updates
    """
    updates = []
    
    try:
        # Check for country change
        with conn.cursor() as cur:
            # Get old drink info
            cur.execute("""
                SELECT l."drinkType", l."typeCategory", l."originCountry"
                FROM "listings" l
                WHERE l."id" = %s
            """, (old_review['reviewTarget'],))
            
            old_drink = cur.fetchone()
            
            # Get new drink info
            cur.execute("""
                SELECT l."drinkType", l."typeCategory", l."originCountry"
                FROM "listings" l
                WHERE l."id" = %s
            """, (new_review['reviewTarget'],))
            
            new_drink = cur.fetchone()
            
            # If drink changed, update badges
            if old_drink['originCountry'] != new_drink['originCountry']:
                # Remove old country badge action
                remove_badge_action(
                    conn, user_id, 'Country', old_drink['originCountry'], review_id, 'review'
                )
                
                # Add new country badge action
                country_updates = check_and_award_badge(
                    conn, user_id, 'Country', new_drink['originCountry'], review_id, 'review'
                )
                updates.extend(country_updates)
            
            # Check for drink type change
            if old_drink['drinkType'] != new_drink['drinkType']:
                # Remove old drink type badge action
                remove_badge_action(
                    conn, user_id, 'DrinkType', old_drink['drinkType'], review_id, 'review'
                )
                
                # Add new drink type badge action
                type_updates = check_and_award_badge(
                    conn, user_id, 'DrinkType', new_drink['drinkType'], review_id, 'review'
                )
                updates.extend(type_updates)
            
            # Check for category change
            if old_drink['typeCategory'] != new_drink['typeCategory']:
                # Remove old category badge action
                remove_badge_action(
                    conn, user_id, 'Category', old_drink['typeCategory'], review_id, 'review'
                )
                
                # Add new category badge action
                category_updates = check_and_award_badge(
                    conn, user_id, 'Category', new_drink['typeCategory'], review_id, 'review'
                )
                updates.extend(category_updates)
            
            # Check for extensive review changes
            old_has_extensive = (
                old_review.get('finish') or old_review.get('colour') or 
                old_review.get('aroma') or old_review.get('taste')
            )
            
            new_has_extensive = (
                new_review.get('finish') or new_review.get('colour') or 
                new_review.get('aroma') or new_review.get('taste')
            )
            
            if old_has_extensive and not new_has_extensive:
                # Extensive review removed
                remove_badge_action(
                    conn, user_id, 'ExtensiveReview', None, review_id, 'review'
                )
            elif not old_has_extensive and new_has_extensive:
                # Extensive review added
                extensive_updates = check_and_award_badge(
                    conn, user_id, 'ExtensiveReview', None, review_id, 'review'
                )
                updates.extend(extensive_updates)
            
            # Check for photo changes
            old_has_photo = bool(old_review.get('photo'))
            new_has_photo = bool(new_review.get('photo'))
            
            if old_has_photo and not new_has_photo:
                # Photo removed
                remove_badge_action(
                    conn, user_id, 'PhotoAttached', None, review_id, 'review'
                )
            elif not old_has_photo and new_has_photo:
                # Photo added
                photo_updates = check_and_award_badge(
                    conn, user_id, 'PhotoAttached', None, review_id, 'review'
                )
                updates.extend(photo_updates)
            
            # Check for location changes
            old_has_location = (old_review.get('location') or old_review.get('address'))
            new_has_location = (new_review.get('location') or new_review.get('address'))
            
            if old_has_location and not new_has_location:
                # Location removed
                remove_badge_action(
                    conn, user_id, 'LocationTagged', None, review_id, 'review'
                )
            elif not old_has_location and new_has_location:
                # Location added
                location_updates = check_and_award_badge(
                    conn, user_id, 'LocationTagged', None, review_id, 'review'
                )
                updates.extend(location_updates)
            
            # Check for friend tag changes
            old_has_tags = bool(old_review.get('taggedUsers'))
            new_has_tags = bool(new_review.get('taggedUsers'))
            
            if old_has_tags and not new_has_tags:
                # Tags removed
                remove_badge_action(
                    conn, user_id, 'FriendTagged', None, review_id, 'review'
                )
            elif not old_has_tags and new_has_tags:
                # Tags added
                tag_updates = check_and_award_badge(
                    conn, user_id, 'FriendTagged', None, review_id, 'review'
                )
                updates.extend(tag_updates)
            
        conn.commit()
        return updates
    
    except Exception as e:
        conn.rollback()
        print(f"Error processing badge edits: {str(e)}")
        return []

def process_badges_for_vote(conn, user_id, review_id, vote_date):
    """Process upvote badges"""
    try:
        with conn.cursor() as cur:
            # Check if the review was posted within a week
            cur.execute("""
                SELECT r."userID", r."createdDate" 
                FROM "reviews" r
                WHERE r."id" = %s
            """, (review_id,))
            
            review = cur.fetchone()
            if not review:
                return []
            
            # Get the author of the review
            author_id = review['userID']
            
            # Check if the vote is within a week of the review
            review_date = review['createdDate']
            vote_datetime = datetime.strptime(vote_date, "%Y-%m-%d %H:%M:%S")
            
            # Check if vote is within a week of review
            if (vote_datetime - review_date) <= timedelta(days=7):
                # Award upvote badge to the author
                updates = check_and_award_badge(
                    conn, author_id, 'Upvote', None, review_id, 'review'
                )
                return updates
            
            return []
            
    except Exception as e:
        print(f"Error processing vote badges: {str(e)}")
        return []

def check_existing_badge_action(conn, user_id, action_type, entity_id=None, entity_type=None):
    """Check if a badge action already exists"""
    with conn.cursor() as cur:
        if entity_id and entity_type:
            cur.execute("""
                SELECT COUNT(*) FROM "badgeActions"
                WHERE "userId" = %s AND "actionType" = %s AND "entityId" = %s AND "entityType" = %s
            """, (user_id, action_type, entity_id, entity_type))
        else:
            cur.execute("""
                SELECT COUNT(*) FROM "badgeActions"
                WHERE "userId" = %s AND "actionType" = %s
            """, (user_id, action_type))
        
        count = cur.fetchone()[0]
        return count > 0