-- Insert color values into the "colours" table
INSERT INTO "colours" ("hexcode") VALUES
('#FFFFFF'),
('#FEED97'),
('#FBE166'),
('#FAD74A'),
('#F5C84B'),
('#F8C139'),
('#E79E12'),
('#E07D1F'),
('#D55530'),
('#B63426'),
('#AA1F22'),
('#702C1C'),
('#4A1C0C'),
('#000000');

-- Insert country values into the "countries" table
INSERT INTO "countries" ("originCountry", "legalAge") VALUES
('Afghanistan', 21),
('Åland Islands', 18),
('Albania', 18),
('Algeria', 18),
('Andorra', 18),
('Angola', 18),
('Anguilla', 18),
('Antigua', 16),
('Argentina', 18),
('Armenia', 18),
('Aruba', 18),
('Australia', 18),
('Austria', 16),
('Azerbaijan', 18),
('Bahamas', 18),
('Bahrain', 21),
('Bangladesh', 21),
('Barbados', 16),
('Belarus', 18),
('Belgium', 16),
('Belize', 18),
('Benin', 20),
('Bermuda', 18),
('Bhutan', 18),
('Bolivia', 18),
('Bosnia and Herzegovina', 18),
('Botswana', 18),
('Brazil', 18),
('British Virgin Islands', 16),
('Brunei', 21),
('Bulgaria', 18),
('Burkina Faso', 18),
('Burundi', 18),
('Cambodia', 18),
('Cameroon', 21),
('Canada', 19),
('Canary Islands', 18),
('Cape Verde', 18),
('Cayman Islands', 18),
('Central African Republic', 15),
('Chad', 18),
('Chile', 18),
('China', 18),
('Colombia', 18),
('Comoros', 18),
('Costa Rica', 18),
('Côte d’Ivoire', 18),
('Croatia', 18),
('Cuba', 16),
('Cyprus', 17),
('Czech Republic', 18),
('Democratic Republic of the Congo', 18),
('Denmark', 16),
('Djibouti', 18),
('Dominica', 16),
('Dominican Republic', 18),
('East Timor (Timor-Leste)', 18),
('Ecuador', 18),
('Egypt', 21),
('El Salvador', 18),
('Equatorial Guinea', 21),
('Eritrea', 18),
('Estonia', 18),
('Eswatini', 18),
('Ethiopia', 21),
('Faroe Islands', 18),
('Fiji', 18),
('Finland', 18),
('France', 18),
('French Polynesia', 18),
('Gabon', 18),
('Georgia', 18),
('Germany', 16),
('Ghana', 18),
('Greece', 18),
('Greenland', 18),
('Grenada', 18),
('Guadeloupe', 18),
('Guam', 21),
('Guatemala', 18),
('Guernsey', 18),
('Guinea', 18),
('Guyana', 18),
('Haiti', 16),
('Honduras', 18),
('Hong Kong', 18),
('Hungary', 18),
('Iceland', 20),
('India', 21),
('Indonesia', 21),
('Iran', 21),
('Iraq', 21),
('Ireland', 18),
('Isle of Man', 18),
('Israel', 18),
('Italy', 18),
('Jamaica', 18),
('Japan', 20),
('Jersey', 18),
('Jordan', 18),
('Kazakhstan', 21),
('Kenya', 18),
('Kiribati', 21),
('Kosovo', 18),
('Kuwait', 21),
('Kyrgyzstan', 18),
('Laos', 18),
('Latvia', 18),
('Lebanon', 18),
('Lesotho', 21),
('Liberia', 18),
('Libya', 21),
('Liechtenstein', 16),
('Lithuania', 20),
('Luxembourg', 16),
('Madagascar', 18),
('Madeira', 18),
('Malawi', 18),
('Malaysia', 21),
('Maldives', 18),
('Mali', 18),
('Malta', 17),
('Marie Galante', 18),
('Marshall Islands', 21),
('Martinique', 18),
('Mauritania', 21),
('Mauritius', 18),
('Mexico', 18),
('Moldova', 18),
('Monaco', 18),
('Mongolia', 18),
('Montenegro', 18),
('Morocco', 18),
('Mozambique', 18),
('Myanmar', 18),
('Namibia', 18),
('Nauru', 21),
('Nepal', 18),
('Netherlands', 18),
('New Zealand', 18),
('Nicaragua', 18),
('Niger', 18),
('Nigeria', 18),
('North Korea', 18),
('North Macedonia', 18),
('Northern Ireland', 18),
('Norway', 18),
('Oman', 21),
('Pakistan', 21),
('Palau', 21),
('Palestinian Territories', 16),
('Panama', 18),
('Papua New Guinea', 18),
('Paraguay', 20),
('Peru', 18),
('Philippines', 18),
('Poland', 18),
('Portugal', 18),
('Puerto Rico', 18),
('Qatar', 21),
('Réunion Island', 18),
('Romania', 18),
('Russia', 18),
('Rwanda', 18),
('Saint Barthelemy', 18),
('Saint Helena', 18),
('Saint Kitts and Nevis', 18),
('Saint Lucia', 16),
('Saint Martin', 18),
('Saint Vincent', 16),
('Samoa', 21),
('San Marino', 16),
('Sao Tome and Principe', 18),
('Scotland', 18),
('Senegal', 18),
('Serbia', 18),
('Seychelles', 18),
('Sierra Leone', 18),
('Singapore', 18),
('Slovakia', 18),
('Slovenia', 18),
('Solomon Islands', 21),
('Somalia', 21),
('South Africa', 18),
('South Korea', 19),
('Spain', 18),
('Sri Lanka', 21),
('Sudan', 21),
('Sudan, South', 18),
('Suriname', 16),
('Sweden', 18),
('Switzerland', 16),
('Syria', 21),
('Taiwan', 18),
('Tajikistan', 18),
('Tanzania', 18),
('Thailand', 20),
('The Gambia', 18),
('Togo', 18),
('Tonga', 21),
('Trinidad and Tobago', 18),
('Tunisia', 18),
('Turkey', 18),
('Turkmenistan', 21),
('Tuvalu', 18),
('Uganda', 18),
('Ukraine', 18),
('United Arab Emirates', 21),
('United Kingdom', 18),
('United States', 21),
('Uruguay', 18),
('US Virgin Islands', 18),
('Uzbekistan', 21),
('Vanuatu', 18),
('Vatican City', 18),
('Venezuela', 18),
('Vietnam', 18),
('Wales', 18),
('Yemen', 21),
('Zambia', 18),
('Zimbabwe', 18);

-- Insert serving type values into the "servingTypes" table
INSERT INTO "servingTypes" ("servingType") VALUES
('Glass'),
('Bottle'),
('Can'),
('Dram'),
('Pint'),
('Shot'),
('In A Cocktail'),
('Serving');

-- Insert special color values into the "specialColours" table
INSERT INTO "specialColours" ("hexList", "colour") VALUES
(ARRAY['#24FF00', '#074202'], 'green'),
(ARRAY['#FF0F0F', '#69140F'], 'red'),
(ARRAY['#8F8DF3', '#051B6B'], 'darkblue'),
(ARRAY['#82E3E9', '#0A7E97'], 'lightblue'),
(ARRAY['#FDC1FE', '#AD1181'], 'pink'),
(ARRAY['#CBA4E3', '#5B0E8A'], 'purple');

-- Insert flavor tag values into the "flavourTags" table
INSERT INTO "flavourTags" ("hexcode", "familyTag") VALUES
('#CE5858', 'Common'),
('#A6C4D5', 'Floral'),
('#E78181', 'Fruits'),
('#71966B', 'Green'),
('#C97ECB', 'Confectionary'),
('#DD9E54', 'Cereal'), 
('#774326', 'Earthy'),
('#9C7A52', 'Spices'),
('#6B9691', 'Mineral'),
('#CEC69F', 'Lactic'),
('#326A55', 'Umami'),
('#80839E', 'Smoky'),
('#BCAF35', 'Others');

-- Insert tags into the subTags table with familyTagId 1
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(1, 'Sweet'),
(1, 'Sour'),
(1, 'Salty'),
(1, 'Umami'),
(1, 'Bitter'),
(1, 'Rich'),
(1, 'Thin'),
(1, 'Light'),
(1, 'Thick'),
(1, 'Mellow'),
(1, 'Hot'),
(1, 'Juicy'),
(1, 'Candied'),
(1, 'Rounded'),
(1, 'Full-Bodied');

-- Insert tags into the subTags table with familyTagId 2
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(2, 'White Flowers'),
(2, 'Yellow Flowers'),
(2, 'Red Flowers'),
(2, 'Purple Flowers'),
(2, 'Field Flowers'),
(2, 'Dried Flowers'),
(2, 'Exotic Flowers'),
(2, 'Oriental Flowers'),
(2, 'Pine Forest'),
(2, 'Rainforest'),
(2, 'Potpourri'),
(2, 'Bouquet'),
(2, 'Beeswax'),
(2, 'Fruit Flowers'),
(2, 'Perfume');

-- Insert tags into the subTags table with familyTagId 3
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(3, 'Sweet Berries'),
(3, 'Tinned Fruit'),
(3, 'Orchard Fruits'),
(3, 'Stone Fruits'),
(3, 'Tropical Fruits'),
(3, 'Green Fruits'),
(3, 'Citrus'),
(3, 'Yellow Fruits'),
(3, 'Unripe Fruits'),
(3, 'Dried Fruits'),
(3, 'Stewed Fruits'),
(3, 'Melons'),
(3, 'Coconut'),
(3, 'Tart Fruits'),
(3, 'Sweet Wine');

-- Insert tags into the subTags table with familyTagId 4
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(4, 'Fresh Herbs'),
(4, 'Dried Herbs'),
(4, 'Vegetables'),
(4, 'Leafy'),
(4, 'Hay'),
(4, 'Meadow'),
(4, 'Grassy'),
(4, 'Minty'),
(4, 'Hops'),
(4, 'Succulent'),
(4, 'Olive'),
(4, 'Green Tea'),
(4, 'Pith'),
(4, 'Sugarcane'),
(4, 'Juniper');

-- Insert tags into the subTags table with familyTagId 5
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(5, 'Caramel'),
(5, 'Toffee'),
(5, 'Candy'),
(5, 'Syrup'),
(5, 'Treacle'),
(5, 'Brown Sugar'),
(5, 'Nougat'),
(5, 'Baked Goods'),
(5, 'Custard'),
(5, 'Milk Chocolate'),
(5, 'Fruit Cake'),
(5, 'Vanilla Cream'),
(5, 'Maple Syrup'),
(5, 'Honey'),
(5, 'Cola Syrup');

-- Insert tags into the subTags table with familyTagId 6
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(6, 'Sweet Grain'),
(6, 'Spicy Grain'),
(6, 'Husk'),
(6, 'Nutty'),
(6, 'Fresh Bread'),
(6, 'Burnt Toast'),
(6, 'Biscuits'),
(6, 'Rice'),
(6, 'Cooked Mash'),
(6, 'Steamed Rice'),
(6, 'Sweet Corn'),
(6, 'Cooked Barley'),
(6, 'Rustic'),
(6, 'Butter Cookies'),
(6, 'Porridge');

-- Insert tags into the subTags table with familyTagId 7
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(7, 'Old Wood'),
(7, 'Damp Wood'),
(7, 'Charred Wood'),
(7, 'Coffee'),
(7, 'Lacquer'),
(7, 'Musty'),
(7, 'Wood Shaving'),
(7, 'Soil'),
(7, 'Incense'),
(7, 'Tobacco'),
(7, 'Cacao'),
(7, 'Oaky'),
(7, 'Leather'),
(7, 'Vines'),
(7, 'Resinous');

-- Insert tags into the subTags table with familyTagId 8
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(8, 'Sweet Herbal'),
(8, 'Bitter Herbal'),
(8, 'Roots'),
(8, 'Pepper'),
(8, 'Baking Spices'),
(8, 'Cinnamon'),
(8, 'Black Tea'),
(8, 'Clove'),
(8, 'Anise'),
(8, 'Ginger'),
(8, 'Liquorice'),
(8, 'Nutmeg'),
(8, 'Chilli'),
(8, 'Oriental Spice'),
(8, 'Mediterranean Spice');

-- Insert tags into the subTags table with familyTagId 9
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(9, 'Antiseptic'),
(9, 'Wet Stone'),
(9, 'Chalk'),
(9, 'Concrete'),
(9, 'Briney'),
(9, 'Oysters'),
(9, 'Coastal'),
(9, 'Rainwater'),
(9, 'Mineral Water'),
(9, 'Clay'),
(9, 'Wax'),
(9, 'Asphalt'),
(9, 'Isotonic'),
(9, 'Gravel'),
(9, 'Crisp Water');

-- Insert tags into the subTags table with familyTagId 10
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(10, 'Farmhouse'),
(10, 'Sweat'),
(10, 'Yeasty'),
(10, 'Soft Cheese'),
(10, 'Yogurt'),
(10, 'Dough'),
(10, 'Koji'),
(10, 'Balsamic'),
(10, 'Fermented'),
(10, 'Butter'),
(10, 'Milky'),
(10, 'Sour Cream'),
(10, 'Sauerkraut'),
(10, 'Lees'),
(10, 'Pickled');

-- Insert tags into the subTags table with familyTagId 11
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(11, 'Hard Cheese'),
(11, 'Miso'),
(11, 'Mushroom'),
(11, 'Soy Sauce'),
(11, 'Seaweed'),
(11, 'Boiled Egg'),
(11, 'Bean Paste'),
(11, 'Charcuterie Meat'),
(11, 'Bonito Flakes'),
(11, 'Broth'),
(11, 'Black Olives'),
(11, 'Anchovy'),
(11, 'Oyster Sauce'),
(11, 'Marmite'),
(11, 'Sundried Tomatoes');

-- Insert tags into the subTags table with familyTagId 12
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(12, 'Industrial'),
(12, 'Barbecue'),
(12, 'Sweet Smoke'),
(12, 'Cold Ash'),
(12, 'Smoked Fish'),
(12, 'Bitter Ash'),
(12, 'Roasted Chestnuts'),
(12, 'Heavy Roast Coffee'),
(12, 'Burnt Vegetal'),
(12, 'Burnt Sugar'),
(12, 'Cigar'),
(12, 'Toasted Nuts'),
(12, 'Smoke'),
(12, 'Savoury'),
(12, 'Scented Candles');

-- Insert tags into the subTags table with familyTagId 13
INSERT INTO "subTags" ("familyTagId", "subTag") VALUES
(13, 'Tannic'),
(13, 'Solvent'),
(13, 'Plastic'),
(13, 'Coal Gas'),
(13, 'Shoe Polish'),
(13, 'Rubber'),
(13, 'Tar'),
(13, 'Skunky'),
(13, 'Metallic'),
(13, 'Glue'),
(13, 'Varnish'),
(13, 'Soap'),
(13, 'Sulphur'),
(13, 'Oxidized'),
(13, 'Cardboard');


-- Insert all language values into the "languages" table
INSERT INTO "languages" ("language") VALUES
('Corsican'),
('Aymara'),
('Croatian'),
('Czech'),
('Georgian'),
('Igbo'),
('Samoan'),
('Shona'),
('Western Frisian'),
('Estonian'),
('Romanian'),
('Sinhala'),
('Amharic'),
('Bhojpuri'),
('Catalan'),
('Filipino'),
('Hebrew'),
('Malayalam'),
('Hindi'),
('Irish'),
('Krio'),
('Malay'),
('Portuguese'),
('Tsonga'),
('Ukrainian'),
('Uyghur'),
('Xhosa'),
('Cebuano'),
('Divehi'),
('Guarani'),
('Khmer'),
('Kyrgyz'),
('Maithili'),
('Tigrinya'),
('Urdu'),
('Zulu'),
('Kazakh'),
('Korean'),
('Marathi'),
('Norwegian'),
('Southern Sotho'),
('Swahili'),
('Turkish'),
('Albanian'),
('Arabic'),
('Azerbaijani'),
('Bangla'),
('Bulgarian'),
('Greek'),
('Lao'),
('Somali'),
('Assamese'),
('Danish'),
('English'),
('Finnish'),
('Hawaiian'),
('Hungarian'),
('Icelandic'),
('Italian'),
('Japanese'),
('Kannada'),
('Kurdish'),
('Northern Sotho'),
('Nyanja'),
('Haitian Creole'),
('Latvian'),
('Scottish Gaelic'),
('Slovenian'),
('Uzbek'),
('Yoruba'),
('Basque'),
('Esperanto'),
('Gujarati'),
('Javanese'),
('Maltese'),
('Serbian'),
('Tajik'),
('Tamil'),
('Hausa'),
('Iloko'),
('Kinyarwanda'),
('Mongolian'),
('Russian'),
('Bambara'),
('Central Kurdish'),
('Chinese (Traditional)'),
('Ewe'),
('French'),
('Indonesian'),
('Luxembourgish'),
('Nepali'),
('Punjabi'),
('Sindhi'),
('Telugu'),
('Welsh'),
('Akan'),
('Bosnian'),
('Dogri'),
('Galician'),
('Ganda'),
('German'),
('Macedonian'),
('Māori'),
('Mizo'),
('Pashto'),
('Thai'),
('Turkmen'),
('Vietnamese'),
('Burmese'),
('Hmong'),
('Malagasy'),
('Odia'),
('Polish'),
('Sundanese'),
('Swedish'),
('Afrikaans'),
('Belarusian'),
('Chinese (Simplified)'),
('Dutch'),
('Goan Konkani'),
('Lingala'),
('Manipuri (Meitei Mayek)'),
('Spanish'),
('Tatar'),
('Armenian'),
('Latin'),
('Lithuanian'),
('Oromo'),
('Persian'),
('Quechua'),
('Sanskrit'),
('Slovak'),
('Yiddish');

-- Insert observation tags into the observationTags table
INSERT INTO "observationTags" ("observationTag") VALUES
('Beginner Friendly'),
('Recommended for Enthusiasts'),
('Good for Gifts 🎁'),
('Cool Packaging'),
('Acquired Taste 🤭'),
('Easy to Drink 😋'),
('Good for Cocktails 🍸'),
('Good for Sipping 🥃'),
('Good for Highballs 🍹'),
('More Complex Than Inception'),
('Sharp Like a Toothpick'),
('Hot Like Hell 🔥'),
('Ticket to Funkytown 🎟️'),
('Food Pairing Friendly 🥩'),
('Broke the Bank 💰'),
('Smooth Criminal 🕺🏻'),
('Grail 😇'),
('Unique Expression ⭐'),
('What Just Hit Me'),
('For My Worst Enemy 😡'),
('Overhyped! 🥸'),
('Try Once'),
('Is This Water?🚰'),
('Daily Drinker'),
('Netflix & Chill 🍆');


INSERT INTO "users" ("username","displayName","choiceDrinks","modType","photo","hashedPassword","joinDate","firstName","lastName","email","isAdmin","birthday","pin", "choiceFlavours", "preferences") VALUES
	 ('admin','admin','{}','{}','','-1522920846','2024-10-28 18:45:31.403','admin','admin','admin@drink-x.com',false,'2000-01-01 00:00:00','175029,2024-10-28 18:46:29', '{}', '{}'),
	 ('Lotusroot518','Lotusroot518','{}','{}','','-289780632','2024-10-29 01:31:56.379','Lotusroot518','Lotusroot518','Kailinchoo@gmail.com',false,'1995-08-11 00:00:00',NULL, '{}', '{}'),
	 ('charsiucharlie','charsiucharlie','{}','{beer}','','-65180891','2024-10-30 13:48:46.277','charsiucharlie','charsiucharlie','tzhehan@gmail.com',true,'1993-06-29 00:00:00',NULL, '{}', '{}'),
	 ('DumplingBoy','DumplingBoy','{}','{}','','2108394495','2024-11-03 09:49:51.179','DumplingBoy','DumplingBoy','jwleong.199@gmail.com',false,'1999-10-21 00:00:00',NULL, '{}', '{}'),
     ('cp', 'cp', '{}', '{}', '', '-301000982', '2024-11-03 09:49:51.179', 'cheng', 'pong', 'cpdeveloper101@gmail.com', false, '1999-10-21 00:00:00', NULL, '{}', '{}'),
     ('user1', 'User One', '{}', '{}', '', '-1799326735', '2024-02-02', 'John', 'Doe', 'user1@example.com', false, '1990-01-01', NULL, '{}', '{}'),
     ('user2', 'User Two', '{}', '{}', '', '-1670244015', '2024-02-02', 'Jane', 'Smith', 'user2@example.com', false, '1992-05-12', NULL, '{}', '{}'),
     ('user3', 'User Three', '{}', '{}', '', '-1541161295', '2024-02-02', 'Mike', 'Johnson', 'user3@example.com', false, '1988-07-24', NULL, '{}', '{}'),
     ('user4', 'User Four', '{}', '{}', '', '-1412078575', '2024-02-02', 'Emily', 'Davis', 'user4@example.com', false, '1995-09-14', NULL, '{}', '{}'),
     ('user5', 'User Five', '{}', '{}', '', '-1282995855', '2024-02-02', 'Chris', 'Brown', 'user5@example.com', false, '1987-03-08', NULL, '{}', '{}'),
     ('user6', 'User Six', '{}', '{}', '', '-1153913135', '2024-02-02', 'Sarah', 'Wilson', 'user6@example.com', false, '1991-06-30', NULL, '{}', '{}'),
     ('user7', 'User Seven', '{}', '{}', '', '-1024830415', '2024-02-02', 'David', 'Martinez', 'user7@example.com', false, '1994-12-10', NULL, '{}', '{}'),
     ('user8', 'User Eight', '{}', '{}', '', '-895747695', '2024-02-02', 'Laura', 'Anderson', 'user8@example.com', false, '1993-08-20', NULL, '{}', '{}'),
     ('user9', 'User Nine', '{}', '{}', '', '-766664975', '2024-02-02', 'James', 'Garcia', 'user9@example.com', false, '1986-04-15', NULL, '{}', '{}'),
     ('user10', 'User Ten', '{}', '{}', '', '-1500753877', '2024-02-02', 'Olivia', 'Taylor', 'user10@example.com', false, '1996-11-22', NULL, '{}', '{}'),
     ('user11', 'User Eleven', '{}', '{}', '', '-1371671157', '2024-02-02', 'Ethan', 'Harris', 'user11@example.com', false, '1990-10-05', NULL, '{}', '{}'),
     ('user12', 'User Twelve', '{}', '{}', '', '-1242588437', '2024-02-02', 'Sophia', 'Clark', 'user12@example.com', false, '1989-02-18', NULL, '{}', '{}'),
     ('user13', 'User Thirteen', '{}', '{}', '', '-1113505717', '2024-02-02', 'Daniel', 'Lewis', 'user13@example.com', false, '1997-07-07', NULL, '{}', '{}'),
     ('user14', 'User Fourteen', '{}', '{}', '', '-984422997', '2024-02-02', 'Isabella', 'Robinson', 'user14@example.com', false, '1998-01-25', NULL, '{}', '{}'),
     ('user15', 'User Fifteen', '{}', '{}', '', '-855340277', '2024-02-02', 'Matthew', 'Walker', 'user15@example.com', false, '1993-03-14', NULL, '{}', '{}'),
     ('user16', 'User Sixteen', '{}', '{}', '', '-726257557', '2024-02-02', 'Mia', 'Young', 'user16@example.com', false, '1994-06-28', NULL, '{}', '{}');

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Whisky',                           -- drinkType
    NULL,                                         -- badgePhoto (set a URL if available)
    ARRAY[
        'Single Malt',
        'Single Grain',
        'Blended',
        'Single Blended',
        'Irish Pot Still Whiskey',
        'Bourbon',
        'Tennessee Whiskey',
        'Rye Whiskey',
        'Malt Whisky',
        'Corn Whiskey',
        'Wheat Whiskey',
        'All Other American Whiskey',
        'Rice Whisky',
        'Flavoured',
        'New Make / Moonshine / White Dog',
        'Others'
    ]
    
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Ready-To-Drink Cocktails',                                 -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Ready-To-Drink Cocktails'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Agave +',                                 -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Sotol',
        'Bacanora',
        'Raicilla',
        'All Other Agave Spirit'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Rice + (Soju, etc.)',                                 -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Soju',
        'Makgeolli'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Tequila',                                   -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Blanco (Unaged / White)',
        'Joven / Oro (Young / Gold)',
        'Reposado (Aged)',
        'Añejo (Extra Aged)',
        'Extra Añejo (Ultra Aged)',
        'Cristalino',
        'Curado (Flavoured)',
        'Others (Including Mixto)'
    ]
);


INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Mezcal',                                   -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Joven (Unaged / Young)',
        'Reposado (Aged)',
        'Añejo (Extra Aged)',
        'Extra Añejo (Ultra Aged)',
        'En Vidrio (Aged in Glass)',
        'Destilado Con (Pechuga, Conejos, etc)',
        'Curado / Abocado Con (Flavoured)',
        'Cristalino',
        'Others',
        'Destilado de Agave'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Rum',                                -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Juice - Agricultural (Column Still)',
        'Juice - Pure Single Rum (Pot Still)',
        'Juice - Single Blended Rum (Pot & Column Still)',
        'Juice - All Others (Excluding White Unaged and Including Multi-Distillery Blend, Excluding Clairin / Cachaca / Aguardiente)',
        'Juice - White Unaged',
        'Syrup - Traditional Rum (Column Still)',
        'Syrup - Pure Single Rum (Pot Still)',
        'Syrup - Single Blended Rum (Pot & Column Still)',
        'Syrup - All Others (Excluding White Unaged and Including Multi-Distillery Blend)',
        'Syrup - White / Unaged',
        'Syrup / Juice - Clairin / Cachaça / Aguardiente / Grogue',
        'Molasses - Traditional Rum (Column Still)',
        'Molasses - Pure Single Rum (Pot Still)',
        'Molasses - Single Blended Rum (Pot & Column Still)',
        'Molasses - All Others (Excluding White Unaged and Including Multi-Distillery Blend)',
        'Molasses - White Unaged',
        'Others/Undisclosed',
        'Flavoured / Spiced',
        'Aged Blend of Molasses, Juice, and/or Syrup',
        'White Unaged Blend of Molasses, Juice, and/or Syrup'
    ]
);


INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Cocktails',                                   -- drinkType
    NULL,                                        -- badgePhoto (set a URL if available)
    ARRAY[
        'Beer- And Cider-Based Mixed Drinks',
        'Bottled Cocktails',
        'Champagne Cocktails',
        'Cobblers',
        'Duos and Trios',
        'French-Italian Drinks',
        'Frozen Drinks',
        'Highballs',
        'Hot Drinks',
        'Juleps',
        'Milanese Drinks',
        'Muddle Drinks',
        'Pousse-Cafes',
        'Punches',
        'Snappers',
        'Sours',
        'Tropical Drinks',
        'Shots'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Beer', -- drinkType
    NULL, -- badgePhoto (replace with a URL if applicable)
    ARRAY[
        'Aged Beer',
        'Altbier',
        'Barleywine',
        'Belgian Style',
        'Bitter Ale',
        'Brett Beer',
        'Brown Ale',
        'Cider',
        'Corn Beer / Chicha de Jora',
        'Cream Ale',
        'Dark Ale',
        'Farmhouse Ale',
        'Field Beer',
        'Flavored Malt Beverage',
        'Freeze-Distilled Beer',
        'Fruit Beer',
        'German Style',
        'Ginger Beer / Hard Ginger Beer',
        'Blonde / Golden Ale',
        'Grape Ale',
        'Happoshu',
        'Hard Kombucha',
        'Hard Seltzer',
        'Historical Beer',
        'Honey Beer',
        'Hybrid Beer',
        'IPA (India Pale Ale)',
        'Koji Beer / Ginjo Beer / Sake Yeast Beer',
        'Kvass',
        'Lager',
        'Lambic',
        'Malt Beverage',
        'Mead',
        'Mild Ale',
        'Non-Alcoholic',
        'Old Ale',
        'Pale Ale',
        'Pilsner',
        'Porter',
        'Stout',
        'Pumpkin Beer',
        'Red Ale',
        'Root Beer',
        'Rye Beer',
        'Scotch Ale',
        'Shandy / Radler',
        'Smoked Beer',
        'Sorghum / Millet Beer',
        'Sour',
        'Specialty Beer',
        'Squash Beer',
        'Strong Ale',
        'Summer Ale',
        'Table Beer / Small Beer',
        'Wheat Beer',
        'Wild Beer / Wild Ale',
        'Yam Beer'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Shochu', -- drinkType
    NULL, -- badgePhoto (replace with a URL if applicable)
    ARRAY[
        'Mugi (Barley)',
        'Imo (Sweet Potato)',
        'Kome (Rice)',
        'Soba (Buckwheat)',
        'Kokuto (Brown Sugar)',
        'Kuri (Chestnut)',
        'Awamori (Jasmine Rice Okinawan Shochu)',
        'Kasutori (Sake lees)',
        'Flavoured',
        'Kusu (Aged Awamori)',
        'Shisho (Perilla)',
        'Kasu (Sake Lees)',
        'All Others (Undisclosed)'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Sake', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Futsushu (Table sakes)',
        'Honjozo (Alcohol added)',
        'Junmai',
        'Ginjo (Alcohol added)',
        'Junmai Ginjo',
        'Daiginjo (Alcohol added)',
        'Junmai Daiginjo',
        'Nigori',
        'Sparkling',
        'Sparkling Nigori',
        'All Kijoshu',
        'Amazake',
        'Doburoku',
        'Flavoured',
        'Taru / Komodaru'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Soju', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Modern (Grocery store soju, usually in green glass bottles)',
        'Craft (Small batch distilled, not matured)',
        'Flavoured',
        'Traditional (Onggi Matured)',
        'Barrel Aged'
    ]
);


INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Wine', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Red Wine',
        'White Wine',
        'Rosé Wine',
        'Sparkling Wine',
        'Fortified Wine',
        'Dessert Wine',
        'All Other Fruit Wine'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Brandy', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Armagnac',
        'Cognac',
        'Grappa / Pomace / Marc Brandy',
        'Pisco',
        'Calvados',
        'All Others - Aged',
        'All Others - Unaged',
        'All Others - Flavoured'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Baijiu', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Strong Aroma (Nong Xiang)',
        'Light Aroma (Qing Xiang)',
        'Sauce Aroma (Jiang Xiang)',
        'Rice Aroma (Mi Xiang)',
        'Sesame Aroma (Zhima Xiang)',
        'Phoenix Aroma (Feng Xiang)',
        'Fat Aroma (Zhi Xiang)',
        'Medicinal Aroma (Yao Xiang)',
        'Mixed Aroma (Jian Xiang)',
        'All Others (Including Baijiu Liqueur)'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Gin', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'London Dry',
        'Contemporary',
        'Genever',
        'Plymouth Gin',
        'Old Tom',
        'Sloe Gin',
        'Barrel Aged',
        'Flavoured Gin',
        'Distilled Gin',
        'Navy Strength'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Vodka', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Classic',
        'Infused',
        'Flavoured',
        'Barrel Aged'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Liqueurs & Bitters', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Cream',
        'Coffee',
        'Chocolate',
        'Fruit',
        'Herbs & Spices',
        'Floral',
        'Nuts',
        'Others'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Umeshu', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Umeshu'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Absinthe', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Absinthe'
    ]
);

INSERT INTO "drinkTypes" ("drinkType", "badgePhoto", "typeCategory")
VALUES (
    'Arrack', -- drinkType
    NULL, -- badgePhoto (replace with a URL if needed)
    ARRAY[
        'Arrack'
    ]
);

-- Fetch the ID of the "Whisky" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Whisky'
)
-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Single Malt', ARRAY[
        'Highland',
        'Lowland',
        'Speyside',
        'Islay',
        'Campbeltown',
        'Islands'
    ]),
    ((SELECT id FROM drink_type), 'Single Grain', ARRAY[
        'Highland',
        'Lowland',
        'Speyside',
        'Islay',
        'Campbeltown',
        'Islands'
    ]),
    ((SELECT id FROM drink_type), 'Blended', ARRAY[
        'Highland',
        'Lowland',
        'Speyside',
        'Islay',
        'Campbeltown',
        'Islands',
        'World Blend'
    ]),
    ((SELECT id FROM drink_type), 'Single Blended', ARRAY[
        'Highland',
        'Lowland',
        'Speyside',
        'Islay',
        'Campbeltown',
        'Islands'
    ]);

-- Fetch the ID of the "Rum" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Rum'
)
-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Juice - Agricultural (Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Juice - Pure Single Rum (Pot Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Juice - Single Blended Rum (Pot & Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Juice - All Others', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Juice - White Unaged', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup - Traditional Rum (Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup - Pure Single Rum (Pot Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup - Single Blended Rum (Pot & Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup - All Others', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup - White / Unaged', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Syrup / Juice - Clairin / Cachaça / Aguardiente / Grogue', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Molasses - Traditional Rum (Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Molasses - Pure Single Rum (Pot Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Molasses - Single Blended Rum (Pot & Column Still)', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Molasses - All Others', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Molasses - White Unaged', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Others / Undisclosed', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Flavoured / Spiced', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'Aged Blend of Molasses, Juice, and/or Syrup', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]),
    ((SELECT id FROM drink_type), 'White Unaged Blend of Molasses, Juice, and/or Syrup', ARRAY[
        'British Style Rum',
        'French Style Rhum',
        'Spanish Style Ron',
        'Navy Rum Blend',
        'Rhum Agricole',
        'Jamaican High Ester',
        'Trinidad Heavy',
        'Reunion Island Grand Arome',
        'Barbados Long Fermentation',
        'High Ester',
        'Central America',
        'South America',
        'Indian Jaggery',
        'Japanese Kokuto (Brown Sugar)'
    ]);

    -- Fetch the ID of the "Tequila" drinkType
    WITH drink_type AS (
        SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Tequila'
    )
    -- Insert corresponding type categories
    INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
    VALUES
        ((SELECT id FROM drink_type), 'Blanco (Unaged / White)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Joven / Oro (Young / Gold)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Reposado (Aged)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Añejo (Extra Aged)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Extra Añejo (Ultra Aged)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Cristalino', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Curado (Flavoured)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]),
        ((SELECT id FROM drink_type), 'Others (Including Mixto)', ARRAY[
            'Jalisco',
            'Nayarit',
            'Guanajuato',
            'Michoaćan',
            'Tamaulipas'
        ]);

-- Fetch the ID of the "Mezcal" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Mezcal'
)
-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Joven (Unaged / Young)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Reposado (Aged)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Añejo (Extra Aged)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Extra Añejo (Ultra Aged)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'En Vidrio (Aged in Glass)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Destilado Con (Pechuga, Conejos, etc)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Curado / Abocado Con (Flavoured)', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Cristalino', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Others', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]),
    ((SELECT id FROM drink_type), 'Destilado de Agave', ARRAY[
        'Oaxaca',
        'Guerrero',
        'Michoaćan',
        'Puebla',
        'Durango',
        'San Luís Potosí',
        'Zacatecas',
        'Guanajuato',
        'Tamaulipas'
    ]);


-- Fetch the ID of the "Sake" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Sake'
)
-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Futsushu (Table sakes)', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Honjozo (Alcohol added)', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Junmai', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Ginjo (Alcohol added)', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Junmai Ginjo', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Daiginjo (Alcohol added)', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Junmai Daiginjo', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Nigori', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Sparkling', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Sparkling Nigori', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'All Kijoshu', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Amazake', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Doburoku', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Flavoured', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]),
    ((SELECT id FROM drink_type), 'Taru / Komodaru', ARRAY[
        'Niigata', 'Aichi', 'Hyogo', 'Fukushima', 'Kyoto', 'Ishikawa', 'Kumamoto', 'Saga', 'Shiga', 'Iwate', 
        'Osaka', 'Gunma', 'Yamaguchi', 'Akita', 'Shizuoka', 'Mie', 'Yamagata', 'Hokkaido', 'Saitama', 'Ibaraki', 
        'Nara', 'Chiba', 'Okayama', 'Tottori', 'Shimane', 'Kochi', 'Hiroshima', 'Nagano', 'Miyagi', 'Fukuoka'
    ]);

-- Fetch the ID of the "Brandy" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Brandy'
)
-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Armagnac', ARRAY[
        'Bas-Armagnac',
        'Haut-Armagnac',
        'Ténarèze',
        'Armagnac Blend',
        'Armagnac - All Others / Undisclosed Region'
    ]),
    ((SELECT id FROM drink_type), 'Cognac', ARRAY[
        'Single Estate',
        'Cognac Blend',
        'All Others / Undisclosed Region'
    ]),
    ((SELECT id FROM drink_type), 'Grappa / Pomace / Marc Brandy', ARRAY[
        'Mono-Varietal',
        'Poli-Varietal',
        'All Others / Undisclosed Varietal'
    ]),
    ((SELECT id FROM drink_type), 'Pisco', ARRAY[
        'Puro',
        'Acholado',
        'Mosto Verde',
        'All Others / Undisclosed Varietal'
    ]),
    ((SELECT id FROM drink_type), 'Calvados', ARRAY[
        'Pays d''Auge',
        'Domfrontais',
        'Blend',
        'All Others / Undisclosed Region'
    ]);




-- Fetch the ID of the "Beer" drinkType
    WITH drink_type AS (
        SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Beer'
    )
    -- Insert corresponding type categories
    INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
    VALUES
        ((SELECT id FROM drink_type), 'Aged Beer', ARRAY[
            'Wood- and Barrel-Aged Beer',
            'Aged Beer - Other Styles'
        ]),
        ((SELECT id FROM drink_type), 'Altbier', ARRAY[
            'Altbier - Sticke',
            'Altbier - Traditional'
        ]),
        ((SELECT id FROM drink_type), 'Barleywine', ARRAY[
            'Barleywine - American',
            'Barleywine - English',
            'Barleywine - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Belgian Style', ARRAY[
            'Belgian Style - Blonde / Golden Ale',
            'Belgian Style - Contemporary Spontaneous Fermented',
            'Belgian Style - Dubbel',
            'Belgian Style - Quadrupel',
            'Belgian Style - Saison',
            'Belgian Style - Tripel',
            'Belgian Style - All Others',
            'Belgian Style - Brown',
            'Belgian Style - Dark Ale',
            'Belgian Style - Enkel / Patersbier',
            'Belgian Style - Bière de Champagne / Bière Brut'
        ]),
        ((SELECT id FROM drink_type), 'Bitter Ale', ARRAY[
            'Bitter Ale - Best',
            'Bitter Ale - Extra Special / Strong (ESB)',
            'Bitter Ale - Session / Ordinary'
        ]),
        ((SELECT id FROM drink_type), 'Brown Ale', ARRAY[
            'Brown Ale - American',
            'Brown Ale - Belgian',
            'Brown Ale - English',
            'Brown Ale - Imperial / Double',
            'Brown Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Cider', ARRAY[
            'Cider - Aged / Barrel Aged',
            'Cider - Apfelwein / German Style',
            'Cider - Cidre / French Style',
            'Cider - Dry',
            'Cider - Fruited / Flavoured',
            'Cider - Graff',
            'Cider - Herbed / Spiced',
            'Cider - Hopped',
            'Cider - Ice',
            'Cider - Mulled',
            'Cider - Perry / Poiré',
            'Cider - Pommeau',
            'Cider - Rosé',
            'Cider - Sitra / Spanish Style',
            'Cider - Sour',
            'Cider - Sweet',
            'Cider - Traditional',
            'Cider - All Others',
            'Cider - Other Fruit'
        ]),
        ((SELECT id FROM drink_type), 'Cream Ale', ARRAY[
            'Cream Ale - Imperial / Double',
            'Cream Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Farmhouse Ale', ARRAY[
            'Farmhouse Ale - Bière de Coupage',
            'Farmhouse Ale - Bière de Garde',
            'Farmhouse Ale - Bière de Mars',
            'Farmhouse Ale - Classic French & Belgian Style',
            'Farmhouse Ale - Finnish Style Sahti',
            'Farmhouse Ale - Grisette',
            'Farmhouse Ale - Saison',
            'Farmhouse Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'German Style', ARRAY[
            'German Style - Bock (Single / Traditional)',
            'German Style - Doppelbock',
            'German Style - Eisbock',
            'German Style - Helles Bock / Maibock / Lentebock',
            'German Style - Weizenbock',
            'German Style - Weizendoppelbock',
            'German Style - Kellerbier / Zwickelbier',
            'German Style - Kölsch / Koelsch',
            'German Style - Märzen',
            'German Style - Oktoberfestbier/Wiesn',
            'German Style - Rauchbier',
            'German Style - Roggenbier',
            'German Style - Rotbier',
            'German Style - Schwarzbier',
            'German Style - All Others',
            'German Style - Festbier'
        ]),
        ((SELECT id FROM drink_type), 'Blonde / Golden Ale', ARRAY[
            'Blonde / Golden Ale - Belgian Style',
            'Blonde / Golden Ale - American',
            'Blonde / Golden Ale - English',
            'Blonde / Golden Ale - Ukrainian',
            'Blonde / Golden Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Grape Ale', ARRAY[
            'Grape Ale - Italian',
            'Grape Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Historical Beer', ARRAY[
            'Historical Beer - California Common / Steam Beer',
            'Historical Beer - Adambier',
            'Historical Beer - Berliner Braunbier',
            'Historical Beer - Broyhan',
            'Historical Beer - Burton Ale',
            'Historical Beer - Dampfbier',
            'Historical Beer - Gruit / Ancient Herbed Ale',
            'Historical Beer - Kentucky Common',
            'Historical Beer - Kottbusser',
            'Historical Beer - Kuit / Kuyt / Koyt',
            'Historical Beer - Lichtenhainer',
            'Historical Beer - Mumme',
            'Historical Beer - Steinbier',
            'Historical Beer - Zoigl',
            'Historical Beer - Australian Sparkling Ale',
            'Historical Beer - All Others',
            'Historical Beer - Grodziskie / Grätzer',
            'Historical Beer - Roggenbier'
        ]),
        ((SELECT id FROM drink_type), 'Hybrid Beer', ARRAY[
            'Hybrid Lager',
            'Hybrid Ale',
            'Hybrid Beer - All Others'
        ]),
        ((SELECT id FROM drink_type), 'IPA (India Pale Ale)', ARRAY[
            'IPA - American Style (All)',
            'IPA - Barrel Aged',
            'IPA - Belgian Style',
            'IPA - Black / Cascadian Dark Ale',
            'IPA - Brett',
            'IPA - Brown',
            'IPA - Brut',
            'IPA - Cold',
            'IPA - Double (DIPA) / Imperial',
            'IPA - Double Dry Hopped (DDH)',
            'IPA - Dry Hopped',
            'IPA - Fruited',
            'IPA - New England / Hazy / Juicy',
            'IPA - Hazy Double (DIPA)',
            'IPA - Hazy Triple (TIPA)',
            'IPA - Milkshake / Double Milkshake / Imperial',
            'IPA - Quadruple',
            'IPA - Red',
            'IPA - Rye',
            'IPA - Session',
            'IPA - Single Hop',
            'IPA - Sour',
            'IPA - Triple (TIPA)',
            'IPA - Triple Dry Hopped (TDH)',
            'IPA - West Coast',
            'IPA - White / Wheat',
            'IPA - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Lager', ARRAY[
            'Lager - Amber / Red',
            'Lager - American Style (All Styles)',
            'Lager - Dark',
            'Lager - Dortmunder / Export',
            'Lager - Dunkel',
            'Lager - European Style',
            'Lager - Helles',
            'Lager - IPL (India Pale Lager)',
            'Lager - Japanese Rice / All Rice',
            'Lager - Leichtbier',
            'Lager - Mexican',
            'Lager - Pale',
            'Lager - Strong',
            'Lager - Vienna Style',
            'Lager - Winter',
            'Lager - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Lambic', ARRAY[
            'Lambic - Framboise',
            'Lambic - Other Fruit',
            'Lambic - Gueuze',
            'Lambic - Kriek',
            'Lambic - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Mead', ARRAY[
            'Mead - Acerglyn / Maple Wine',
            'Mead - Bochet',
            'Mead - Braggot',
            'Mead - Cyser',
            'Mead - Melomel',
            'Mead - Metheglin',
            'Mead - Pyment',
            'Mead - Session / Short',
            'Mead - Sack',
            'Mead - Great / Spiced',
            'Mead - Imperial',
            'Mead - Herbed & Spiced',
            'Mead - Fruited',
            'Mead - Traditional',
            'Mead - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Mild Ale', ARRAY[
            'Mild Ale - Dark',
            'Mild Ale - Light',
            'Mild Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Non-Alcoholic', ARRAY[
            'Non-Alcohlic - Lager',
            'Non-Alcoholic - Beer',
            'Non-Alcoholic - Cider',
            'Non-Alcoholic - IPA',
            'Non-Alcoholic - Malt Beverage',
            'Non-Alcoholic - Mead',
            'Non-Alcoholic - Pale Ale',
            'Non-Alcoholic - Porter',
            'Non-Alcoholic - Sour',
            'Non-Alcoholic - Stout',
            'Non-Alcoholic - Wheat Beer',
            'Non-Alcoholic - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Pale Ale', ARRAY[
            'Pale Ale - All American Styles',
            'Pale Ale - All Australian Styles',
            'Pale Ale - Barrel Aged',
            'Pale Ale - All Belgian Styles',
            'Pale Ale - English Style',
            'Pale Ale - New England / Hazy / Juicy',
            'Pale Ale - Milkshake',
            'Pale Ale - New Zealand',
            'Pale Ale - XPA (Extra Pale)',
            'Pale Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Pilsner', ARRAY[
            'Pilsner - Czech / Bohemian',
            'Pilsner - German',
            'Pilsner - Imperial / Double',
            'Pilsner - Italian',
            'Pilsner - New Zealand',
            'Pilsner - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Porter', ARRAY[
            'Porter - American',
            'Porter - Baltic',
            'Porter - Coffee',
            'Porter - English',
            'Porter - Imperial / Double',
            'Porter - Imperial / Double Baltic',
            'Porter - Imperial / Double Coffee',
            'Porter - Smoked',
            'Porter - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Stout', ARRAY[
            'Stout - All Others',
            'Stout - American',
            'Stout - Belgian',
            'Stout - Coffee',
            'Stout - English',
            'Stout - Imperial / Double Coffee',
            'Stout - Imperial / Double Milk',
            'Stout - Imperial / Double Oatmeal',
            'Stout - Imperial / Double White / Golden',
            'Stout - Irish Dry',
            'Stout - Milk / Sweet',
            'Stout - Oatmeal',
            'Stout - Russian Imperial',
            'Stout - White / Golden',
            'Stout - Barrel Aged',
            'Stout - Foreign / Export',
            'Stout - Imperial / Double',
            'Stout - Imperial / Double Pastry',
            'Stout - Oyster',
            'Stout - Pastry'
        ]),
        ((SELECT id FROM drink_type), 'Red Ale', ARRAY[
            'Red Ale - American Style / American Amber',
            'Red Ale - Imperial / Double',
            'Red Ale - Irish',
            'Red Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Scotch Ale', ARRAY[
            'Scotch Ale - Export',
            'Scotch Ale - Heavy / Wee Heavy',
            'Scotch Ale - Light'
        ]),
        ((SELECT id FROM drink_type), 'Sour', ARRAY[
            'Sour - American Style (All)',
            'Sour - Barrel Aged',
            'Sour - Berliner Weisse',
            'Sour - Fruited Berliner Weisse',
            'Sour - Flanders Oud Bruin',
            'Sour - Oud Red Ale',
            'Sour - Fruited',
            'Sour - Fruited Gose',
            'Sour - Traditional Gose',
            'Sour - Tomato / Vegetable Gose',
            'Sour - All Other Gose',
            'Sour - Smoothie / Pastry',
            'Sour - Catharina',
            'Sour - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Specialty Beer', ARRAY[
            'Specialty Grain',
            'Specialty Beer - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Strong Ale', ARRAY[
            'Strong Ale - American',
            'Strong Ale - English',
            'Strong Ale - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Wheat Beer', ARRAY[
            'Wheat Beer - American Pale Wheat',
            'Wheat Beer - Dunkelweizen',
            'Wheat Beer - Fruited',
            'Wheat Beer - Hefeweizen',
            'Wheat Beer - Hefeweizen Light / Leicht',
            'Wheat Beer - Hopfenweisse',
            'Wheat Beer - Kristallweizen',
            'Wheat Beer - Other German / Bavarian Style',
            'Wheat Beer - Wheat Wine',
            'Wheat Beer - Witbier / Blanche',
            'Wheat Beer - All Others'
        ]),
        ((SELECT id FROM drink_type), 'Wild Beer / Wild Ale', ARRAY[
            'Wild Beer / Wild Ale - American',
            'Wild Beer / Wild Ale - All Others'
        ]);

-- Fetch the ID of the "Wine" drinkType
WITH drink_type AS (
    SELECT id FROM "drinkTypes" WHERE "drinkType" = 'Wine'
)

-- Insert corresponding type categories
INSERT INTO "typeCategories" ("drinkType_id", "typeCategory", "drinkStyle")
VALUES
    ((SELECT id FROM drink_type), 'Red Wine', ARRAY[
        'Alsace Pinot Noir',
        'Amyndeon Red',
        'Argentinian Agrelo Malbec Red',
        'Argentinian Bonarda',
        'Argentinian Bordeaux Blend',
        'Argentinian Cabernet Sauvignon',
        'Argentinian Cabernet Sauvignon - Malbec',
        'Argentinian Lujan de Cuyo Malbec Red',
        'Argentinian Malbec',
        'Argentinian Malbec Red Blend',
        'Argentinian Mendoza Cabernet Franc Red',
        'Argentinian Mendoza Malbec Red',
        'Argentinian Merlot',
        'Argentinian Petit Verdot Red',
        'Argentinian Pinot Noir',
        'Argentinian Salta Malbec Red',
        'Argentinian Syrah',
        'Argentinian Syrah - Viognier',
        'Argentinian Tempranillo Red',
        'Argentinian Tupungato Cabernet Franc Red',
        'Argentinian Tupungato Malbec Red',
        'Argentinian Uco Valley Cabernet Franc Red',
        'Argentinian Uco Valley Malbec Red',
        'Arizona Red',
        'Australian Adelaide Hills Shiraz',
        'Australian Barossa Valley Shiraz',
        'Australian Bordeaux Blend',
        'Australian Cabernet - Shiraz',
        'Australian Cabernet Sauvignon',
        'Australian Canberra District Shiraz',
        'Australian Clare Valley Shiraz',
        'Australian Coonawarra Shiraz',
        'Australian Eden Valley Shiraz',
        'Australian Heathcote Shiraz',
        'Australian Hunter Valley Shiraz',
        'Australian Malbec',
        'Australian McLaren Vale Shiraz',
        'Australian Merlot',
        'Australian Nebbiolo Red',
        'Australian New South Wales Shiraz',
        'Australian Pinot Noir',
        'Australian Red Blend',
        'Australian Rhône Blend Red',
        'Australian Sangiovese Red',
        'Australian Shiraz',
        'Australian Syrah - Viognier',
        'Australian Victoria Shiraz',
        'Australian Yarra Valley Shiraz',
        'Austrian Blaufränkisch',
        'Austrian Pinot Noir',
        'Austrian Red',
        'Austrian St. Laurent Red',
        'Austrian Zweigelt',
        'Beaujolais Nouveau Red',
        'Beaujolais Red',
        'Bordeaux Graves Red',
        'Bordeaux Haut-Médoc Red',
        'Bordeaux Libournais Red',
        'Bordeaux Listrac-Médoc Red',
        'Bordeaux Margaux',
        'Bordeaux Médoc',
        'Bordeaux Moulis-en-Médoc Red',
        'Bordeaux Pauillac',
        'Bordeaux Pessac-Léognan',
        'Bordeaux Pomerol',
        'Bordeaux Red',
        'Bordeaux Saint-Émilion',
        'Bordeaux Saint-Estèphe',
        'Bordeaux Saint-Julien',
        'Brazilian Cabernet Franc',
        'Brazilian Merlot',
        'Brazilian Pinot Noir',
        'Burgundy Côte Chalonnaise Red',
        'Burgundy Côte de Beaune Red',
        'Burgundy Côte de Nuits Red',
        'Burgundy Red',
        'Californian Alexander Valley Cabernet Sauvignon Red',
        'Californian Anderson Valley Pinot Noir Red',
        'Californian Barbera Red',
        'Californian Bordeaux Blend',
        'Californian Cabernet Franc',
        'Californian Cabernet Sauvignon',
        'Californian Carignan Red',
        'Californian Grenache Red',
        'Californian Knights Valley Cabernet Sauvignon Red',
        'Californian Los Carneros Pinot Noir Red',
        'Californian Malbec',
        'Californian Meritage',
        'Californian Merlot',
        'Californian Paso Robles Cabernet Sauvignon Red',
        'Californian Petite Sirah',
        'Californian Pinot Noir',
        'Californian Red Blend',
        'Californian Rhône Blend Red',
        'Californian Russian River Valley Pinot Noir Red',
        'Californian Sangiovese',
        'Californian Santa Lucia Highlands Pinot Noir Red',
        'Californian Santa Maria Valley Pinot Noir Red',
        'Californian Sierra Foothills Barbera Red',
        'Californian Sonoma Coast Pinot Noir Red',
        'Californian Sonoma County Cabernet Sauvignon Red',
        'Californian Sta. Rita Hills Pinot Noir Red',
        'Californian Syrah',
        'Californian Tempranillo Red',
        'Californian Zinfandel',
        'Canadian Cabernet Franc',
        'Canadian Cabernet Sauvignon',
        'Canadian Merlot',
        'Canadian Pinot Noir',
        'Canadian Syrah',
        'Central Italy Red',
        'Central Portugal Red',
        'Chilean Bordeaux Blend',
        'Chilean Cabernet - Syrah',
        'Chilean Cabernet Sauvignon',
        'Chilean Carménère',
        'Chilean Malbec',
        'Chilean Merlot',
        'Chilean Pinot Noir',
        'Chilean Syrah',
        'Chinese Red',
        'Connecticut Red',
        'Croatian Cabernet Sauvignon Red',
        'Croatian Dalmatian Coast Plavac Mali Red',
        'Croatian Plavac Mali Red',
        'Croatian Red',
        'French Atlantique Red',
        'French Comtés Rhodaniens Red',
        'French Corsica Red',
        'French Jura Red',
        'French Méditerranée Red',
        'French Middle Loire Cabernet Franc Red',
        'French Middle Loire Red',
        'French Provence Red',
        'French Red',
        'French Savoie Red',
        'German Blauer Portugieser Red',
        'German Blaufränkisch Red',
        'German Cabernet Sauvignon Red',
        'German Dornfelder',
        'German Merlot Red',
        'German Pinot Noir Précoce Red',
        'German Red',
        'German Schwarzriesling Red',
        'German Spätburgunder',
        'German St. Laurent Red',
        'German Trollinger Red',
        'Goumenissa Red',
        'Greek Nemea Red',
        'Greek Red',
        'Hungarian Blaufränkisch Red',
        'Hungarian Bordeaux Blend',
        'Hungarian Pinot Noir Red',
        'Hungarian Red',
        'Idaho red',
        'Israeli Cabernet Franc Red',
        'Israeli Cabernet Sauvignon',
        'Israeli Merlot',
        'Israeli Red',
        'Israeli Red Blend',
        'Israeli Syrah',
        'Italian Amarone',
        'Italian Barbaresco',
        'Italian Barbera',
        'Italian Barolo',
        'Italian Bolgheri',
        'Italian Brunello',
        'Italian Chianti',
        'Italian Chianti Classico Red',
        'Italian Montepulciano d''Abruzzo',
        'Italian Nebbiolo',
        'Italian Red',
        'Italian Ripasso',
        'Italian Valpolicella Red',
        'Italian Vino Nobile Di Montepulciano',
        'Japanese Cabernet Sauvignon Red',
        'Languedoc-Roussillon Grenache',
        'Languedoc-Roussillon Red',
        'Lebanese Red',
        'Maryland Red',
        'Michigan Red',
        'Minnesota Red',
        'Missouri Red',
        'Naoussa Red',
        'Napa Valley Bordeaux Blend',
        'Napa Valley Cabernet Sauvignon',
        'New Jersey Red',
        'New Mexico Red',
        'New York Cabernet Franc Red',
        'New York Pinot Noir Red',
        'New Zealand Bordeaux Blend',
        'New Zealand Cabernet Sauvignon',
        'New Zealand Central Otago Pinot Noir Red',
        'New Zealand Martinborough Pinot Noir Red',
        'New Zealand Merlot',
        'New Zealand Pinot Noir',
        'New Zealand Red',
        'New Zealand Syrah',
        'New Zealand Wairarapa Pinot Noir Red',
        'North Carolina Red',
        'Northern Italy Pinot Noir',
        'Northern Italy Red',
        'Northern Portugal Red',
        'Northern Rhône Cornas',
        'Northern Rhône Côte-Rotie',
        'Northern Rhône Crozes-Hermitage',
        'Northern Rhône Hermitage',
        'Northern Rhône Red',
        'Northern Rhône Saint-Joseph',
        'Oregon Cabernet Franc Red',
        'Oregon Cabernet Sauvignon',
        'Oregon Grenache Red',
        'Oregon Merlot Red',
        'Oregon Petite Sirah Red',
        'Oregon Pinot Noir',
        'Oregon Red',
        'Oregon Syrah Red',
        'Oregon Tannat Red',
        'Oregon Tempranillo Red',
        'Oregon Zinfandel Red',
        'Pennsylvania Red',
        'Portuguese Alentejo Red',
        'Portuguese Azores Red',
        'Portuguese Dão Red',
        'Portuguese Douro Red',
        'Portuguese Red',
        'Rapsani Red',
        'Sardinian Cannonau',
        'South African Bordeaux Blend',
        'South African Cabernet - Syrah',
        'South African Cabernet Franc',
        'South African Cabernet Sauvignon',
        'South African Cinsault Red',
        'South African Grenache Red',
        'South African Malbec',
        'South African Merlot',
        'South African Pinot Noir',
        'South African Pinotage',
        'South African Pinotage Blend',
        'South African Red',
        'South African Rhône Blend Red',
        'South African Syrah',
        'South African Syrah - Viognier',
        'South Australia Grenache Red',
        'South Australia Shiraz',
        'South Australia Tempranillo Red',
        'South Eastern Australia Shiraz',
        'Southern Italy Primitivo',
        'Southern Italy Red',
        'Southern Portugal Red',
        'Southern Rhône Châteauneuf-du-Pape Red',
        'Southern Rhône Red',
        'Southwest France Madiran Red',
        'Southwest France Malbec',
        'Southwest France Red',
        'Spanish Cabernet Sauvignon',
        'Spanish Grenache',
        'Spanish Mencia',
        'Spanish Merlot',
        'Spanish Monastrell',
        'Spanish Montsant Red',
        'Spanish Priorat Red',
        'Spanish Red',
        'Spanish Rhône Blend Red',
        'Spanish Ribera Del Duero Red',
        'Spanish Rioja Red',
        'Spanish Syrah',
        'Spanish Tempranillo',
        'Spanish Toro Red',
        'Swiss Gamay Red',
        'Swiss Merlot',
        'Swiss Pinot Noir',
        'Swiss Syrah',
        'Swiss Valais Dôle Red',
        'Swiss Valais Humagne Rouge Red',
        'Texas Cabernet Sauvignon Red',
        'Texas Red',
        'Tuscan Red',
        'Upper Loire Red',
        'Virginia Red',
        'Washington State Cabernet Franc Red',
        'Washington State Cabernet Sauvignon',
        'Washington State Columbia Valley Bordeaux Red Blend',
        'Washington State Merlot',
        'Washington State Pinot Noir',
        'Washington State Red Blend',
        'Washington State Syrah',
        'Western Australia Shiraz'
    ]),
    ((SELECT id FROM drink_type), 'White Wine', ARRAY[
        'Alsace Gewürztraminer',
        'Alsace Pinot Blanc',
        'Alsace Pinot Gris',
        'Alsace Riesling',
        'Argentinian Chardonnay',
        'Argentinian Chardonnay - Torrontés White Blend',
        'Argentinian Pinot Gris',
        'Argentinian Sauvignon Blanc',
        'Argentinian Sémillon White',
        'Argentinian Torrontés',
        'Argentinian Viognier',
        'Argentinian White',
        'Arizona White',
        'Australian Chardonnay',
        'Australian Gewürztraminer White',
        'Australian Grüner Veltliner White',
        'Australian Hunter Valley Sémillon White',
        'Australian New South Wales Verdelho White',
        'Australian Pinot Gris',
        'Australian Riesling',
        'Australian Sauvignon Blanc',
        'Australian Viognier',
        'Austrian Chardonnay',
        'Austrian Grüner Veltliner',
        'Austrian Pinot Blanc',
        'Austrian Pinot Gris',
        'Austrian Riesling',
        'Austrian Sauvignon Blanc',
        'Austrian White',
        'Bordeaux White',
        'Burgundy Chablis',
        'Burgundy Côte Chalonnaise White',
        'Burgundy Côte de Beaune White',
        'Burgundy Mâconnais White',
        'Burgundy White',
        'Californian Chardonnay',
        'Californian Chenin Blanc',
        'Californian Gewürztraminer',
        'Californian Pinot Gris',
        'Californian Riesling',
        'Californian Russian River Valley Chardonnay White',
        'Californian Santa Barbara County Chardonnay White',
        'Californian Sauvignon Blanc',
        'Californian Sonoma Coast Chardonnay White',
        'Californian Viognier',
        'Californian White',
        'Californian White Blend',
        'Canadian Chardonnay',
        'Canadian Pinot Gris',
        'Canadian Riesling',
        'Central Italy White',
        'Central Portugal White',
        'Chilean Chardonnay',
        'Chilean Riesling',
        'Chilean Sauvignon Blanc',
        'Chilean Viognier',
        'Colorado White',
        'Connecticut White',
        'Croatian Chardonnay White',
        'Croatian Malvazija Istarska White',
        'Croatian Welschriesling White',
        'Croatian White',
        'French Alsace Muscat White',
        'French Alsace Sylvaner White',
        'French Alsace White Blend',
        'French Atlantique White',
        'French Beaujolais White',
        'French Comtés Rhodaniens White',
        'French Corsica Vermentino White',
        'French Corsica White',
        'French Côtes de Gascogne White',
        'French Méditerranée White',
        'French Provence White',
        'French Savoie White',
        'French White',
        'German Auxerrois White',
        'German Chardonnay',
        'German Gewürztraminer',
        'German Grauburgunder',
        'German Müller Thurgau',
        'German Muscat White',
        'German Pinot Blanc',
        'German Pinot Noir White',
        'German Riesling',
        'German Sauvignon Blanc',
        'German Scheurebe White',
        'German Silvaner',
        'German White',
        'Greek Malagouzia',
        'Hungarian Chardonnay White',
        'Hungarian Furmint White',
        'Hungarian Hárslevelű White',
        'Hungarian Welschriesling White',
        'Hungarian White',
        'Idaho White',
        'Israeli Chardonnay White',
        'Israeli Sauvignon Blanc White',
        'Israeli White',
        'Italian Gavi',
        'Italian Soave',
        'Italian White',
        'Japanese Koshu',
        'Jura Vin Jaune',
        'Jura White',
        'Languedoc-Roussillon Viognier',
        'Languedoc-Roussillon White',
        'Lebanese White',
        'Loire Chenin Blanc',
        'Loire Muscadet',
        'Loire Touraine Sauvignon Blanc',
        'Maryland White',
        'Massachusetts White',
        'Michigan White',
        'Minnesota White',
        'Missouri White',
        'Napa Valley Chardonnay',
        'New Jersey White',
        'New Mexico White',
        'New York Finger Lakes Riesling White',
        'New York Riesling White',
        'New Zealand Chardonnay',
        'New Zealand Gewürztraminer White',
        'New Zealand Grüner Veltliner White',
        'New Zealand Pinot Gris',
        'New Zealand Riesling',
        'New Zealand Sauvignon Blanc',
        'New Zealand Viognier White',
        'North Carolina White',
        'Northern Italy Gewürztraminer',
        'Northern Italy Müller Thurgau',
        'Northern Italy Pinot Blanc',
        'Northern Italy Pinot Grigio',
        'Northern Italy White',
        'Northern Portugal White',
        'Northern Rhône Condrieu',
        'Northern Rhône Saint-Péray',
        'Northern Rhône White',
        'Ohio White',
        'Oregon Chardonnay',
        'Oregon Gewürztraminer',
        'Oregon Pinot Gris',
        'Oregon Riesling',
        'Oregon Roussanne White',
        'Oregon Sauvignon Blanc White',
        'Oregon Viognier White',
        'Oregon White',
        'Pennsylvania White',
        'Portuguese Azores White',
        'Portuguese Dão White',
        'Portuguese Vinho Verde White',
        'Portuguese White',
        'Santorini White',
        'South African Chardonnay',
        'South African Chenin Blanc',
        'South African Pinot Gris',
        'South African Riesling White',
        'South African Sauvignon Blanc',
        'South African Sauvignon Blanc - Sémillon White',
        'South African Sémillon White',
        'South African Viognier',
        'Southern Italy White',
        'Southern Portugal White',
        'Southern Rhône White',
        'Southwest France White',
        'Spanish Albariño',
        'Spanish Castilla Airén White',
        'Spanish Catalunya Grenache Blanc White',
        'Spanish Chardonnay',
        'Spanish Galicia Godello White',
        'Spanish Islas Canarias White',
        'Spanish País Vasco Txakoli White',
        'Spanish Rioja White',
        'Spanish Sauvignon Blanc',
        'Spanish Verdejo',
        'Spanish White',
        'Swiss Chardonnay',
        'Swiss Chasselas',
        'Swiss Petite Arvine White',
        'Swiss Savagnin White',
        'Tennessee White',
        'Texas Viognier White',
        'Texas White',
        'Texas White Blend',
        'Upper Loire White',
        'Virginia White',
        'Washington State Chardonnay',
        'Washington State Columbia Valley Pinot Gris White',
        'Washington State Gewürztraminer',
        'Washington State Riesling',
        'Washington State Sauvignon Blanc',
        'Western Australia Sauvignon Blanc - Sémillon White',
        'Wisconsin White'
    ]),
        ((SELECT id FROM drink_type), 'Rosé Wine', ARRAY[
            'Argentinian Malbec Rosé',
            'Argentinian Rosé',
            'Arizona Rosé',
            'Australian Grenache Rosé',
            'Australian Pinot Noir Rosé',
            'Australian Rosé',
            'Australian Sangiovese Rosé',
            'Australian Shiraz Rosé',
            'Austrian Rosé',
            'Californian Rosé',
            'Central Italy Rosé',
            'Chilean Rosé',
            'French Bordeaux Rosé',
            'French Loire Rosé',
            'French Méditerranée Rosé',
            'French Rosé',
            'German Pinot Noir Rosé',
            'German Rosé',
            'Hungarian Rosé',
            'Italian Cerasuolo d''Abruzzo Rosé',
            'Languedoc-Roussillon Rosé',
            'Michigan Rosé',
            'New York Long Island Rosé',
            'New Zealand Pinot Noir Rosé',
            'New Zealand Rosé',
            'Northern Italy Rosé',
            'Northern Portugal Rosé',
            'Oregon Pinot Noir Rosé',
            'Provence Rosé',
            'South African Rosé',
            'Southern Italy Rosé',
            'Southern Rhône Rosé',
            'Southwest France Rosé',
            'Spanish Grenache Rosé',
            'Spanish Rosé',
            'Spanish Tempranillo Rosé',
            'Texas Rosé',
            'Virginia Rosé',
            'Washington State Rosé'
    ]),
        ((SELECT id FROM drink_type), 'Sparkling Wine', ARRAY[
            'Argentinian Mendoza Sparkling',
            'Australian Adelaide Hills Sparkling',
            'Australian Sparkling',
            'Australian Sparkling Shiraz',
            'Australian Tasmania Sparkling',
            'Australian Victoria Sparkling',
            'Austrian Sparkling',
            'Brazilian Sparkling',
            'Californian Sparkling',
            'Chilean Sparkling',
            'English Sparkling',
            'French Champagne',
            'French Crémant',
            'French Sparkling',
            'German Sekt',
            'Hungarian Sparkling',
            'Italian Asti',
            'Italian Emilia-Romagna Lambrusco Sparkling',
            'Italian Franciacorta Sparkling',
            'Italian Moscato d''Asti',
            'Italian Prosecco',
            'Italian Sparkling',
            'Italian Trentino-Alto Adige Sparkling',
            'Japanese Sparkling',
            'New Mexico Sparkling',
            'New Zealand Sparkling',
            'Oregon Sparkling',
            'Portuguese Sparkling',
            'South African Sparkling',
            'South Australia Sparkling',
            'Spanish Cava',
            'Spanish Sparkling',
            'Washington State Sparkling'
    ]),
        ((SELECT id FROM drink_type), 'Fortified Wine', ARRAY[
            'Colheita Port',
            'Crusted Port',
            'French Languedoc-Roussillon Fortified',
            'Late Bottled Vintage Port',
            'Portuguese Madeira',
            'Portuguese Moscatel',
            'Portuguese Port',
            'Ruby Port',
            'Single Quinta Vintage Port',
            'South African Fortified',
            'Spanish Amontillado Sherry Fortified',
            'Spanish Cream Sherry Fortified',
            'Spanish Fino Sherry Fortified',
            'Spanish Manzanilla Sherry Fortified',
            'Spanish Montilla-Moriles Fortified',
            'Spanish Oloroso Sherry Fortified',
            'Spanish Palo Cortado Sherry Fortified',
            'Spanish Pedro Ximenez',
            'Spanish Sherry',
            'Tawny Port',
            'Vintage Port',
            'White Port'
    ]),
    ((SELECT id FROM drink_type), 'Dessert Wine', ARRAY[
        'Australian Dessert',
        'Australian Sémillon Dessert',
        'Austrian Dessert',
        'Bordeaux Sauternes',
        'Californian Dessert',
        'Canadian Ice Wine',
        'French Alsace Gewürztraminer Dessert',
        'French Alsace Pinot Gris Dessert',
        'French Alsace Riesling Dessert',
        'French Bordeaux Dessert',
        'French Loire Chenin Blanc Dessert',
        'Hungarian Tokaji Aszú',
        'Italian Tuscany Vin Santo Dessert',
        'South African Dessert',
        'Southwest France Dessert'
    ]);

INSERT INTO "producers" ("producerName", "producerDesc", "originCountry", "mainDrinks", "photo", "hashedPassword", "claimStatus", "claimStatusCheckDate", "statusOB", "username", "producerLink", "stripeCustomerId"
) VALUES 
    ('Hennessy', 'This is Hennessy', 'France', '{}', NULL, '-6552510', true, NULL, NULL, 'Hennessy', '', NULL),
    ('Jack Daniel''s', 'Famous Tennessee whiskey brand known for its smooth, charcoal-mellowed whiskey.', 'United States', '{}', NULL, '-1469695901', false, NULL, NULL, 'jackdaniels', '', NULL),
    ('Johnnie Walker', 'One of the most iconic Scotch whisky brands, known for its blended whiskies.', 'Scotland', '{}', NULL, '640032836', false, NULL, NULL, 'johnniewalker', '', NULL),
    ('Jameson', 'The most famous Irish whiskey, triple-distilled for smoothness.', 'Ireland', '{}', NULL, '-152907913', false, NULL, NULL, 'jameson', '', NULL),
    ('Chivas Regal', 'A well-known brand of blended Scotch whisky.', 'Scotland', '{}', NULL, '1650366560', false, NULL, NULL, 'chivasregal', '', NULL),
    ('Glenfiddich', 'One of the most famous single malt Scotch whisky brands.', 'Scotland', '{}', NULL, '626732607', false, NULL, NULL, 'glenfiddich', '', NULL),
    ('Bacardi', 'World-famous rum brand, known for white and dark rums.', 'Cuba', '{}', NULL, '1396448963', false, NULL, NULL, 'bacardi', '', NULL),
    ('Captain Morgan', 'Popular spiced rum brand, known for its smooth taste.', 'Jamaica', '{}', NULL, '-1018979690', false, NULL, NULL, 'captainmorgan', '', NULL),
    ('Don Julio', 'Premium tequila brand, known for its smooth and high-quality tequila.', 'Mexico', '{}', NULL, '2038084859', false, NULL, NULL, 'donjulio', '', NULL),
    ('Patrón', 'A high-end tequila brand, famous for its handcrafted production process.', 'Mexico', '{}', NULL, '462830215', false, NULL, NULL, 'patron', '', NULL),
    ('Jose Cuervo', 'One of the oldest and most famous tequila brands in the world.', 'Mexico', '{}', NULL, '-2090820217', false, NULL, NULL, 'josecuervo', '', NULL),
    ('Tanqueray', 'One of the world’s most popular gin brands, known for its London Dry Gin.', 'United Kingdom', '{}', NULL, '1792363181', false, NULL, NULL, 'tanqueray', '', NULL),
    ('Hendrick''s', 'Scottish gin brand, famous for its cucumber and rose-infused flavors.', 'Scotland', '{}', NULL, '1458970391', false, NULL, NULL, 'hendricks', '', NULL),
    ('Bombay Sapphire', 'A premium gin brand known for its smooth taste and botanicals.', 'United Kingdom', '{}', NULL, '-938116355', false, NULL, NULL, 'bombaysapphire', '', NULL),
    ('Suntory', 'Japanese whisky and spirits brand, known for Hibiki and Yamazaki.', 'Japan', '{}', NULL, '-345359732', false, NULL, NULL, 'suntory', '', NULL),
    ('Nikka', 'Japanese whisky brand, known for its high-quality single malts and blends.', 'Japan', '{}', NULL, '505268853', false, NULL, NULL, 'nikka', '', NULL),
    ('Tito''s Handmade Vodka', 'An American vodka brand made from corn and distilled in Texas.', 'United States', '{}', NULL, '2016735326', false, NULL, NULL, 'titosvodka', '', NULL),
    ('Grey Goose', 'A premium French vodka brand, made with high-quality wheat.', 'France', '{}', NULL, '-1636822077', false, NULL, NULL, 'greygoose', '', NULL),
    ('Absolut', 'One of the most famous vodka brands, known for its pure Swedish vodka.', 'Sweden', '{}', NULL, '-1030449104', false, NULL, NULL, 'absolut', '', NULL),
    ('Tiger Beer', 'A popular Asian beer brand, brewed in Singapore.', 'Singapore', '{}', NULL, '165298405', false, NULL, NULL, 'tigerbeer', '', NULL);

INSERT INTO "venues" (
    "venueName", 
    "address", 
    "venueType", 
    "originLocation", 
    "venueDesc", 
    "hashedPassword", 
    "photo", 
    "claimStatus", 
    "claimStatusCheckDate", 
    "reservationDetails", 
    "username", 
    "publicHolidays", 
    "stripeCustomerId", 
    "pin"
) VALUES (
    'Orh Gao Taproom', 
    'Singapore', 
    'Bar', 
    'Singapore', 
    'Best venue for drinks', 
    '-1918297408', 
    NULL, 
    true, 
    NULL, 
    'Cannot reserve anything', 
    'orhgaotaproom', 
    'Not open on Christmas', 
    NULL, 
    NULL
);

INSERT INTO "producersQuestionAnswers" (
    "question", "answer", "date", "userId", "producerId")
    VALUES ('When are you going to release the next promotion?', 'SOON! CHECK FOR UPDATES!', '2024-10-04 16:08:59.899', 1, 1);

INSERT INTO "listings" (
    "listingName", "producerID", "bottler", "originCountry", "drinkType", "abv", "officialDesc", "allowMod", "addedDate", "typeCategory", "age", "reviewLink", "sourceLink", "photo", "drinkStyle")
	VALUES 
    ('Hennessy VS', 1, 'OB', 'Japan', 'Whiskey', 12, 'BEST EVEERRRR', true, '2024-10-05 00:14:37.661786', 'Spirit', 12, '', '', '', ''),
    ('Jack Daniel''s Old No. 7', 2, 'Jack Daniel''s', 'United States', 'Whiskey', 40, 'The classic Tennessee whiskey with a smooth, charcoal-mellowed flavor.', true, '2024-02-02', 'Bourbon', NULL, '', '', '', ''),
    ('Jack Daniel''s Single Barrel Select', 2, 'Jack Daniel''s', 'United States', 'Whiskey', 47, 'A richer and more complex version of the classic Jack Daniel’s.', true, '2024-02-02', 'Bourbon', NULL, '', '', '', ''),
    ('Jack Daniel''s Tennessee Honey', 2, 'Jack Daniel''s', 'United States', 'Whiskey', 35, 'A smooth blend of Jack Daniel’s and honey liqueur.', true, '2024-02-02', 'Flavored Whiskey', NULL, '', '', '', ''),
    ('Jack Daniel''s Sinatra Select', 2, 'Jack Daniel''s', 'United States', 'Whiskey', 45, 'A premium whiskey honoring Frank Sinatra, aged in specially designed barrels.', true, '2024-02-02', 'Bourbon', NULL, '', '', '', ''),
    ('Jack Daniel''s Bonded', 2, 'Jack Daniel''s', 'United States', 'Whiskey', 50, 'Bottled-in-bond whiskey with a bolder, richer flavor.', true, '2024-02-02', 'Bourbon', NULL, '', '', '', ''),
    ('Johnnie Walker Black Label', 3, 'Johnnie Walker', 'Scotland', 'Whiskey', 40, 'A smooth, well-balanced blended Scotch aged 12 years.', true, '2024-02-02', 'Blended Scotch', 12, '', '', '', ''),
    ('Johnnie Walker Blue Label', 3, 'Johnnie Walker', 'Scotland', 'Whiskey', 43, 'An ultra-premium blend featuring rare, aged Scotch whiskies.', true, '2024-02-02', 'Blended Scotch', NULL, '', '', '', ''),
    ('Johnnie Walker Red Label', 3, 'Johnnie Walker', 'Scotland', 'Whiskey', 40, 'A bold, fiery blend ideal for mixing in cocktails.', true, '2024-02-02', 'Blended Scotch', NULL, '', '', '', ''),
    ('Johnnie Walker Green Label', 3, 'Johnnie Walker', 'Scotland', 'Whiskey', 43, 'A rich, green blend of malt whisky for a fresh taste.', true, '2024-02-02', 'Blended Scotch', NULL, '', '', '', ''),
    ('Jameson Irish Whiskey', 4, 'Jameson', 'Ireland', 'Whiskey', 40, 'A triple-distilled, smooth Irish whiskey with hints of vanilla and spice.', true, '2024-02-02', 'Irish Whiskey', NULL, '', '', '', ''),
    ('Jameson Black Barrel', 4, 'Jameson', 'Ireland', 'Whiskey', 40, 'A rich, intense version of Jameson aged in charred barrels.', true, '2024-02-02', 'Irish Whiskey', NULL, '', '', '', ''),
    ('Jameson Caskmates Stout Edition', 4, 'Jameson', 'Ireland', 'Whiskey', 40, 'Jameson finished in craft beer stout barrels for a deeper taste.', true, '2024-02-02', 'Irish Whiskey', NULL, '', '', '', ''),
    ('Jameson Crested', 4, 'Jameson', 'Ireland', 'Whiskey', 40, 'A rich, smooth blend of Jameson whiskey with a creamy finish.', true, '2024-02-02', 'Irish Whiskey', NULL, '', '', '', ''),
    ('Chivas Regal 12', 5, 'Chivas Regal', 'Scotland', 'Whiskey', 40, 'A smooth, honeyed Scotch whisky aged for 12 years.', true, '2024-02-02', 'Blended Scotch', 12, '', '', '', ''),
    ('Chivas Regal 18', 5, 'Chivas Regal', 'Scotland', 'Whiskey', 40, 'A more complex, rich Scotch aged 18 years.', true, '2024-02-02', 'Blended Scotch', 18, '', '', '', ''),
    ('Chivas Regal Extra', 5, 'Chivas Regal', 'Scotland', 'Whiskey', 40, 'A rich, indulgent Scotch whisky with a warm, fruity flavor.', true, '2024-02-02', 'Blended Scotch', NULL, '', '', '', ''),
    ('Glenfiddich 12', 6, 'Glenfiddich', 'Scotland', 'Whiskey', 40, 'A light and fruity single malt aged for 12 years.', true, '2024-02-02', 'Single Malt Scotch', 12, '', '', '', ''),
    ('Glenfiddich 18', 6, 'Glenfiddich', 'Scotland', 'Whiskey', 43, 'A richer, sherry-aged single malt aged 18 years.', true, '2024-02-02', 'Single Malt Scotch', 18, '', '', '', ''),
    ('Glenfiddich 21', 6, 'Glenfiddich', 'Scotland', 'Whiskey', 40, 'A rare single malt aged for 21 years with rich oak notes.', true, '2024-02-02', 'Single Malt Scotch', 21, '', '', '', ''),
    ('Hennessy VS', 7, 'Hennessy', 'France', 'Cognac', 40, 'A smooth and bold cognac with notes of oak and fruit.', true, '2024-02-02', 'Cognac', NULL, '', '', '', ''),
    ('Hennessy XO', 7, 'Hennessy', 'France', 'Cognac', 40, 'An extra-aged blend with a rich, complex flavor.', true, '2024-02-02', 'Cognac', NULL, '', '', '', ''),
    ('Hennessy Paradis', 7, 'Hennessy', 'France', 'Cognac', 40, 'A luxurious, multi-layered cognac with deep, smooth flavors.', true, '2024-02-02', 'Cognac', NULL, '', '', '', ''),
    ('Bacardi Superior', 8, 'Bacardi', 'Cuba', 'Rum', 40, 'A light, smooth white rum perfect for cocktails.', true, '2024-02-02', 'White Rum', NULL, '', '', '', ''),
    ('Bacardi Gold', 8, 'Bacardi', 'Cuba', 'Rum', 40, 'A smooth, mellow gold rum with hints of vanilla.', true, '2024-02-02', 'Gold Rum', NULL, '', '', '', ''),
    ('Captain Morgan Original Spiced Rum', 9, 'Captain Morgan', 'Jamaica', 'Rum', 35, 'A smooth, spiced rum with hints of vanilla and cinnamon.', true, '2024-02-02', 'Spiced Rum', NULL, '', '', '', ''),
    ('Captain Morgan Private Stock', 9, 'Captain Morgan', 'Jamaica', 'Rum', 40, 'A premium spiced rum with a bold, rich flavor.', true, '2024-02-02', 'Spiced Rum', NULL, '', '', '', ''),
    ('Don Julio Blanco', 10, 'Don Julio', 'Mexico', 'Tequila', 40, 'A fresh, crisp silver tequila with a smooth agave finish.', true, '2024-02-02', 'Tequila Blanco', NULL, '', '', '', ''),
    ('Patrón Silver', 10, 'Patrón', 'Mexico', 'Tequila', 40, 'A smooth, premium silver tequila with citrus and agave notes.', true, '2024-02-02', 'Tequila Blanco', NULL, '', '', '', ''),
    ('Patrón Añejo', 10, 'Patrón', 'Mexico', 'Tequila', 40, 'Aged tequila with rich, oak and vanilla flavors.', true, '2024-02-02', 'Tequila Añejo', NULL, '', '', '', ''),
    ('Tanqueray London Dry Gin', 12, 'Tanqueray', 'United Kingdom', 'Gin', 47.3, 'A classic gin with a crisp, juniper-forward taste.', true, '2024-02-02', 'London Dry Gin', NULL, '', '', '', ''),
    ('Hendrick''s Gin', 13, 'Hendrick''s', 'Scotland', 'Gin', 44, 'A unique gin infused with cucumber and rose petals.', true, '2024-02-02', 'Gin', NULL, '', '', '', ''),
    ('Bombay Sapphire Gin', 14, 'Bombay Sapphire', 'United Kingdom', 'Gin', 40, 'A smooth gin with a rich blend of 10 botanicals.', true, '2024-02-02', 'Gin', NULL, '', '', '', ''),
    ('Suntory Hibiki', 15, 'Suntory', 'Japan', 'Whiskey', 43, 'A harmonious blend of malt and grain whiskies aged in various casks.', true, '2024-02-02', 'Blended Whisky', NULL, '', '', '', ''),
    ('Nikka From The Barrel', 16, 'Nikka', 'Japan', 'Whiskey', 51.4, 'A bold, rich whisky with complex flavors of fruit and spice.', true, '2024-02-02', 'Blended Whisky', NULL, '', '', '', ''),
    ('Tito''s Handmade Vodka', 17, 'Tito''s', 'United States', 'Vodka', 40, 'A premium American vodka distilled from corn for a smooth finish.', true, '2024-02-02', 'Vodka', NULL, '', '', '', ''),
    ('Grey Goose Vodka', 18, 'Grey Goose', 'France', 'Vodka', 40, 'A premium French vodka made from high-quality wheat.', true, '2024-02-02', 'Vodka', NULL, '', '', '', ''),
    ('Absolut Vodka', 19, 'Absolut', 'Sweden', 'Vodka', 40, 'A famous Swedish vodka made with 100% natural ingredients.', true, '2024-02-02', 'Vodka', NULL, '', '', '', ''),
    ('Tiger Beer', 20, 'Tiger Brewery', 'Singapore', 'Beer', 5, 'A crisp, refreshing lager brewed in Singapore.', true, '2024-02-02', 'Lager - All Styles', NULL, '', '', '', 'Pilsner'),
    ('Tiger Crystal', 20, 'Tiger Brewery', 'Singapore', 'Beer', 4.6, 'A smooth, lighter version of the classic Tiger Beer.', true, '2024-02-02', 'Lager - All Styles', NULL, '', '', '', 'Helles'),
    ('Tiger Black', 20, 'Tiger Brewery', 'Singapore', 'Beer', 6.9, 'A full-bodied, stronger version of Tiger Beer.', true, '2024-02-02', 'Lager - All Styles', NULL, '', '', '', 'Vienna Lager');

INSERT INTO "usersFollowLists" (
    "userId", "users", "producers", "venues")
    VALUES 
    (1, '{}', '{}', '{}'), 
    (2, '{}', '{}', '{}'), 
    (3, '{}', '{}', '{}'), 
    (4, '{}', '{}', '{}'),
    (5, '{1}', '{}', '{1}');


INSERT INTO "usersDrinkLists" (
    "userId", "listName")
    VALUES 
    (1, 'Drinks I Have Tried'), 
    (1, 'Drinks I Want To Try'), 
    (2, 'Drinks I Have Tried'), 
    (2, 'Drinks I Want To Try'), 
    (3, 'Drinks I Have Tried'), 
    (3, 'Drinks I Want To Try'), 
    (4, 'Drinks I Have Tried'), 
    (4, 'Drinks I Want To Try');

INSERT INTO "venuesMenu" (
    "sectionName", "sectionOrder","venueId")
    VALUES('Created1', '0', 1);
    
INSERT INTO "menuItems"(
    "itemOrder", "itemPrice", "itemAvailability", "itemID", "itemServingType", "sectionId")
VALUES(0, 12.00, true, 1, 1, 1);

-- Removed insert query for "reviews" and "reviewsUserVotes". "reviewsUserVotes" insert query removed because it is related to thre reviews
-- INSERT INTO "reviews" (
--     "userID", "reviewTarget", "rating", "reviewDesc", "reviewType", "createdDate", 
--     "language", "finish", "willRecommend", "wouldBuyAgain", "taggedUsers", "flavourTag", 
--     "photo", "colour", "aroma", "location", "taste", "observationTag", "address"
-- ) VALUES 
-- (3, 5, 8.1, 'Amazing taste, very smooth.', 'Listing', '2024-02-01 14:32:00', 'English', 'long', TRUE, TRUE, ARRAY[2,3], ARRAY['oak', 'vanilla'], null, '#A52A2A', 'woody', 1, 'rich', ARRAY['mellow', 'deep'], '123 Street A'),
-- (3, 12, 3.8, 'Good but a little harsh.', 'Listing', '2024-02-02 16:45:00', 'English', 'medium', FALSE, TRUE, ARRAY[4], ARRAY['caramel'], null, '#8B0000', 'spicy', 1, 'bold', ARRAY['sharp'], '456 Street B'),
-- (3, 8, 4.2, 'Smooth and enjoyable.', 'Listing', '2024-02-03 19:10:00', 'English', 'short', TRUE, TRUE, ARRAY[3,5], ARRAY['honey'], null, '#FFD700', 'sweet', 1, 'balanced', ARRAY['fruity'], '789 Street C'),
-- (3, 15, 2.9, 'Too bitter for my taste.', 'Listing', '2024-02-04 11:23:00', 'English', 'long', FALSE, FALSE, ARRAY[2], ARRAY['hops'], null, '#000000', 'earthy', 1, 'bitter', ARRAY['strong'], '321 Street D'),
-- (3, 6, 4.9, 'Incredible complexity, highly recommend!', 'Listing', '2024-02-05 20:30:00', 'English', 'long', TRUE, TRUE, ARRAY[5], ARRAY['chocolate'], null, '#4B0082', 'rich', 1, 'deep', ARRAY['complex'], '567 Street E'),
-- (3, 18, 9.3, 'Average experience, decent aftertaste.', 'Listing', '2024-02-06 09:15:00', 'English', 'medium', TRUE, FALSE, ARRAY[4,2], ARRAY['berry'], null, '#DC143C', 'fruity', 1, 'dry', ARRAY['light'], '890 Street F'),
-- (3, 10, 4.0, 'Good balance of flavors.', 'Listing', '2024-02-07 13:05:00', 'English', 'medium', TRUE, TRUE, ARRAY[5], ARRAY['spice'], null, '#8B4513', 'warm', 1, 'smooth', ARRAY['balanced'], '234 Street G'),
-- (3, 3, 3.0, 'A bit too strong for me.', 'Listing', '2024-02-08 17:40:00', 'English', 'short', FALSE, FALSE, ARRAY[2,3], ARRAY['citrus'], null, '#ADD8E6', 'sharp', 1, 'intense', ARRAY['burn'], '678 Street H'),
-- (3, 14, 9.7, 'Very refreshing and crisp.', 'Listing', '2024-02-09 22:10:00', 'English', 'short', TRUE, TRUE, ARRAY[4], ARRAY['floral'], null, '#00FF00', 'fresh', 1, 'light', ARRAY['crisp'], '101 Street I'),
-- (3, 9, 3.2, 'A bit underwhelming, expected more.', 'Listing', '2024-02-10 08:55:00', 'English', 'medium', FALSE, FALSE, ARRAY[3], ARRAY['oak'], null, '#800000', 'dry', 1, 'muted', ARRAY['flat'], '202 Street J'),
-- (1, 5, 5, 'This was absolutely fantastic!', 'Listing', '2025-01-13 18:27:38.498', 'English', 'Long, alittle more oaky now', true, false, '{}', '{2, 3, 36, 37}', '', '', '', null, '', '{Beginner Friendly, OverHyped!}', ''),
-- (2, 12, 4, 'gooooooood goooooooodgooooooood', 'Listing', '2025-01-08 04:52:10.957', 'English', '', false, false, '{2}', '{23, 35, 36, 77}', '', '', '', null, '', '{Beginner Friendly, Good for Gifts}', ''),
-- (3, 5, 5, 'An absolute masterpiece. Smooth and well-balanced.', 'Listing', '2025-01-15 12:34:56.789', 'English', 'Rich, lingering with subtle spice', true, true, '{}', '{1, 2, 3, 47}', '', '', '', null, '', '{Cool Packaging, Recommended for Enthusiasts}', ''),
-- (4, 5, 3, 'It was okay, but I expected more depth.', 'Listing', '2025-01-14 09:18:32.112', 'English', 'Short, slightly bitter', false, false, '{}', '{2, 45, 47, 77}', '', '', '', null, '', '{What Just Hit Me, Recommended for Enthusiasts}', ''),
-- (1, 5, 4, 'Really enjoyable with friends. Would buy again!', 'Listing', '2025-01-12 20:45:22.674', 'English', 'Mellow and warm', true, true, '{}', '{44, 56, 78}', '', '', '', null, '', '{Social Drink, Recommended for Enthusiasts}', ''),
-- (2, 5, 2, 'Not to my taste, too strong on the finish.', 'Listing', '2025-01-10 16:50:10.389', 'English', 'Harsh and overpowering', false, false, '{}', '{12, 23, 35}', '', '', '', null, '', '{Acquired Taste}', ''),
-- (3, 5, 5, 'Absolutely delightful! A must-try.', 'Listing', '2025-01-09 11:30:45.876', 'English', 'Long, smooth caramel notes', true, true, '{}', '{56, 78, 135}', '', '', '', null, '', '{Daily Drinker}', ''),
-- (4, 5, 3, 'A bit too complex for me, but I can appreciate the craftsmanship.', 'Listing', '2025-01-07 14:20:30.654', 'English', 'Layered and evolving', true, false, '{}', '{1, 35, 77}', '', '', '', null, '', '{More Complex Than Inception}', ''),
-- (4, 5, 4, 'Unexpectedly sharp, but it grows on you.', 'Listing', '2025-01-06 10:55:18.908', 'English', 'Sharp and intense', false, false, '{}', '{2, 3, 7, 24, 26}', '', '', '', null, '', '{Sharp Like a Toothpick}', ''),
-- (3, 5, 5, 'Great for a one-time experience, very unique.', 'Listing', '2025-01-05 19:38:50.782', 'English', 'Medium, balanced', true, false, '{}', '{1, 22, 25, 67}', '', '', '', null, '', '{Try Once, More Complex Than Inception}', ''),
-- (1, 5, 4, 'Surprisingly fresh, makes me feel healthy drinking it.', 'Listing', '2025-01-04 08:22:16.543', 'English', 'Crisp and refreshing', true, true, '{}', '{4, 5, 12}', '', '', '', null, '', '{Healthy}', ''),
-- (3, 5, 5, 'Absolutely delightful! A must-try.', 'Listing', '2025-01-09 11:30:45.876', 'English', 'Long, smooth caramel notes', true, true, '{}', '{23, 26, 27, 55}', '', '', '', null, '', '{Daily Drinker, OverHyped!, More Complex Than Inception}', ''),
-- (4, 5, 3, 'A bit too complex for me, but I can appreciate the craftsmanship.', 'Listing', '2025-01-07 14:20:30.654', 'English', 'Layered and evolving', true, false, '{}', '{1, 13, 15, 26, 47}', '', '', '', null, '', '{More Complex Than Inception}', ''),
-- (4, 8, 4, 'Unexpectedly sharp, but it grows on you.', 'Listing', '2025-01-06 10:55:18.908', 'English', 'Sharp and intense', false, false, '{}', '{2, 4, 47}', '', '', '', null, '', '{Sharp Like a Toothpick, OverHyped!}', ''),
-- (3, 8, 5, 'Great for a one-time experience, very unique.', 'Listing', '2025-01-05 19:38:50.782', 'English', 'Medium, balanced', true, false, '{}', '{2, 47}', '', '', '', null, '', '{Try Once}', ''),
-- (1, 8, 4, 'Surprisingly fresh, makes me feel healthy drinking it.', 'Listing', '2025-01-04 08:22:16.543', 'English', 'Crisp and refreshing', true, true, '{}', '{47, 59, 112}', '', '', '', null, '', '{Healthy, Recommended for Enthusiasts}', ''),
-- (1, 8, 5, 'This was absolutely fantastic!', 'Listing', '2025-01-13 18:27:38.498', 'English', 'Long, alittle more oaky now', true, false, '{}', '{}', '', '', '', null, '', '{Beginner Friendly, OverHyped!}', ''),
-- (2, 8, 4, 'gooooooood goooooooodgooooooood', 'Listing', '2025-01-08 04:52:10.957', 'English', '', false, false, '{2}', '{1, 2, 33, 78}', '', '', '', null, '', '{Beginner Friendly, Good for Gifts}', ''),
-- (3, 8, 5, 'An absolute masterpiece. Smooth and well-balanced.', 'Listing', '2025-01-15 12:34:56.789', 'English', 'Rich, lingering with subtle spice', true, true, '{}', '{2, 23, 24, 55}', '', '', '', null, '', '{Cool Packaging}', ''),
-- (4, 8, 3, 'It was okay, but I expected more depth.', 'Listing', '2025-01-14 09:18:32.112', 'English', 'Short, slightly bitter', false, false, '{}', '{1, 12, 15, 23}', '', '', '', null, '', '{What Just Hit Me, OverHyped!}', ''),
-- (1, 8, 4, 'Really enjoyable with friends. Would buy again!', 'Listing', '2025-01-12 20:45:22.674', 'English', 'Mellow and warm', true, true, '{}', '{6, 78, 142}', '', '', '', null, '', '{Social Drink, OverHyped!}', ''),
-- (2, 8, 2, 'Not to my taste, too strong on the finish.', 'Listing', '2025-01-10 16:50:10.389', 'English', 'Harsh and overpowering', false, false, '{}', '{4, 7, 27}', '', '', '', null, '', '{Acquired Taste}', ''),
-- (3, 8, 5, 'Absolutely delightful! A must-try.', 'Listing', '2025-01-09 11:30:45.876', 'English', 'Long, smooth caramel notes', true, true, '{}', '{2, 56}', '', '', '', null, '', '{Daily Drinker, Recommended for Enthusiasts, More Complex Than Inception}', ''),
-- (4, 6, 4, 'Unexpectedly sharp, but it grows on you.', 'Listing', '2025-01-06 10:55:18.908', 'English', 'Sharp and intense', false, false, '{}', '{53, 82}', '', '', '', null, '', '{Sharp Like a Toothpick}', ''),
-- (3, 12, 5, 'Great for a one-time experience, very unique.', 'Listing', '2025-01-05 19:38:50.782', 'English', 'Medium, balanced', true, false, '{}', '{2, 5, 23}', '', '', '', null, '', '{Try Once, More Complex Than Inception}', ''),
-- (1, 5, 4, 'Surprisingly fresh, makes me feel healthy drinking it.', 'Listing', '2025-01-04 08:22:16.543', 'English', 'Crisp and refreshing', true, true, '{}', '{7, 12, 46}', '', '', '', null, '', '{Healthy}', ''),
-- (3, 10, 5, 'Absolutely delightful! A must-try.', 'Listing', '2025-01-09 11:30:45.876', 'English', 'Long, smooth caramel notes', true, true, '{}', '{45, 73, 88}', '', '', '', null, '', '{Daily Drinker, OverHyped!, More Complex Than Inception}', ''),
-- (4, 18, 3, 'A bit too complex for me, but I can appreciate the craftsmanship.', 'Listing', '2025-01-07 14:20:30.654', 'English', 'Layered and evolving', true, false, '{}', '{1, 2, 6, 36}', '', '', '', null, '', '{More Complex Than Inception}', ''),
-- (4, 12, 4, 'Unexpectedly sharp, but it grows on you.', 'Listing', '2025-01-06 10:55:18.908', 'English', 'Sharp and intense', false, false, '{}', '{34}', '', '', '', null, '', '{Sharp Like a Toothpick, OverHyped!}', ''),
-- (3, 6, 5, 'Great for a one-time experience, very unique.', 'Listing', '2025-01-05 19:38:50.782', 'English', 'Medium, balanced', true, false, '{}', '{22, 45, 73}', '', '', '', null, '', '{Try Once}', ''),
-- (1, 14, 4, 'Surprisingly fresh, makes me feel healthy drinking it.', 'Listing', '2025-01-04 08:22:16.543', 'English', 'Crisp and refreshing', true, true, '{}', '{5, 56, 62}', '', '', '', null, '', '{Healthy, Recommended for Enthusiasts}', ''),
-- (1, 9, 5, 'This was absolutely fantastic!', 'Listing', '2025-01-13 18:27:38.498', 'English', 'Long, alittle more oaky now', true, false, '{}', '{}', '', '', '', null, '', '{Beginner Friendly, OverHyped!}', ''),
-- (2, 18, 4, 'gooooooood goooooooodgooooooood', 'Listing', '2025-01-08 04:52:10.957', 'English', '', false, false, '{2}', '{3, 66}', '', '', '', null, '', '{Beginner Friendly, Good for Gifts}', ''),
-- (3, 12, 5, 'An absolute masterpiece. Smooth and well-balanced.', 'Listing', '2025-01-15 12:34:56.789', 'English', 'Rich, lingering with subtle spice', true, true, '{}', '{4, 56}', '', '', '', null, '', '{Cool Packaging}', ''),
-- (4, 5, 3, 'It was okay, but I expected more depth.', 'Listing', '2025-01-14 09:18:32.112', 'English', 'Short, slightly bitter', false, false, '{}', '{3, 87}', '', '', '', null, '', '{What Just Hit Me, OverHyped!}', ''),
-- (1, 14, 4, 'Really enjoyable with friends. Would buy again!', 'Listing', '2025-01-12 20:45:22.674', 'English', 'Mellow and warm', true, true, '{}', '{4, 56}', '', '', '', null, '', '{Social Drink, OverHyped!}', ''),
-- (2, 3, 2, 'Not to my taste, too strong on the finish.', 'Listing', '2025-01-10 16:50:10.389', 'English', 'Harsh and overpowering', false, false, '{}', '{2, 25, 28}', '', '', '', null, '', '{Acquired Taste}', ''),
-- (3, 10, 5, 'Absolutely delightful! A must-try.', 'Listing', '2025-01-09 11:30:45.876', 'English', 'Long, smooth caramel notes', true, true, '{}', '{4, 6}', '', '', '', null, '', '{Daily Drinker, Recommended for Enthusiasts, More Complex Than Inception}', '');

-- INSERT INTO "reviewsUserVotes" ("upvotes", "downvotes", "reviewId") VALUES
-- (
--     '[{"userId": 2, "date": "2025-03-03T12:00:00Z"}, {"userId": 1, "date": "2025-03-02T14:30:00Z"}, {"userId": 4, "date": "2025-03-01T18:45:00Z"}]'::jsonb,
--     '[{"userId": 5, "date": "2025-03-02T10:15:00Z"}]'::jsonb,
--     1
-- ),
-- (
--     '[{"userId": 1, "date": "2025-03-03T15:20:00Z"}, {"userId": 4, "date": "2025-03-01T08:10:00Z"}]'::jsonb,
--     '[{"userId": 2, "date": "2025-03-03T16:45:00Z"}, {"userId": 5, "date": "2025-03-02T12:30:00Z"}]'::jsonb,
--     2
-- ),
-- (
--     '[{"userId": 2, "date": "2025-03-02T20:05:00Z"}, {"userId": 5, "date": "2025-03-01T19:00:00Z"}]'::jsonb,
--     '[{"userId": 1, "date": "2025-03-03T18:30:00Z"}]'::jsonb,
--     3
-- ),
-- (
--     '[{"userId": 4, "date": "2025-03-02T09:50:00Z"}]'::jsonb,
--     '[{"userId": 2, "date": "2025-03-03T14:15:00Z"}, {"userId": 1, "date": "2025-03-01T11:20:00Z"}, {"userId": 5, "date": "2025-03-01T13:40:00Z"}]'::jsonb,
--     4
-- ),
-- (
--     '[{"userId": 1, "date": "2025-03-01T22:00:00Z"}, {"userId": 5, "date": "2025-03-02T08:15:00Z"}]'::jsonb,
--     '[{"userId": 2, "date": "2025-03-03T11:25:00Z"}, {"userId": 4, "date": "2025-03-02T18:30:00Z"}]'::jsonb,
--     5
-- ),
-- (
--     '[{"userId": 2, "date": "2025-03-03T10:45:00Z"}, {"userId": 4, "date": "2025-03-02T17:20:00Z"}, {"userId": 5, "date": "2025-03-01T15:30:00Z"}]'::jsonb,
--     '[{"userId": 1, "date": "2025-03-03T20:10:00Z"}]'::jsonb,
--     6
-- ),
-- (
--     '[{"userId": 1, "date": "2025-03-02T19:40:00Z"}, {"userId": 5, "date": "2025-03-03T09:15:00Z"}]'::jsonb,
--     '[{"userId": 2, "date": "2025-03-01T10:30:00Z"}, {"userId": 4, "date": "2025-03-02T14:45:00Z"}]'::jsonb,
--     7
-- ),
-- (
--     '[{"userId": 2, "date": "2025-03-03T12:30:00Z"}, {"userId": 1, "date": "2025-03-01T16:10:00Z"}]'::jsonb,
--     '[{"userId": 4, "date": "2025-03-02T08:00:00Z"}, {"userId": 5, "date": "2025-03-03T17:25:00Z"}]'::jsonb,
--     8
-- ),
-- (
--     '[{"userId": 4, "date": "2025-03-01T14:05:00Z"}, {"userId": 5, "date": "2025-03-02T21:20:00Z"}]'::jsonb,
--     '[{"userId": 2, "date": "2025-03-03T13:40:00Z"}, {"userId": 1, "date": "2025-03-02T10:55:00Z"}]'::jsonb,
--     9
-- ),
-- (
--     '[{"userId": 2, "date": "2025-03-03T08:20:00Z"}, {"userId": 1, "date": "2025-03-02T11:50:00Z"}, {"userId": 4, "date": "2025-03-01T22:35:00Z"}]'::jsonb,
--     '[{"userId": 5, "date": "2025-03-03T15:55:00Z"}]'::jsonb,
--     10
-- );

INSERT INTO "badgeRules" ("actionType", "levelStart", "levelEnd", "actionsRequired") VALUES
-- Reviews (any review)
('Review', 1, 5, 1),
('Review', 6, 10, 2),
('Review', 11, 20, 3),
('Review', 21, 30, 3),
('Review', 31, 40, 4),
('Review', 41, 50, 4),
('Review', 51, 60, 5),
('Review', 61, 70, 5),
('Review', 71, 80, 6),
('Review', 81, 90, 7),
('Review', 91, 100, 10),

-- Extensive reviews
('ExtensiveReview',    1,   5, 1),
('ExtensiveReview',    6,  10, 2),
('ExtensiveReview',   11,  20, 3),
('ExtensiveReview',   21,  30, 3),
('ExtensiveReview',   31,  40, 4),
('ExtensiveReview',   41,  50, 4),
('ExtensiveReview',   51,  60, 5),
('ExtensiveReview',   61,  70, 5),
('ExtensiveReview',   71,  80, 6),
('ExtensiveReview',   81,  90, 7),
('ExtensiveReview',   91, 100,10),

-- Photo attachments
('PhotoAttached',    1,   5, 1),
('PhotoAttached',    6,  10, 2),
('PhotoAttached',   11,  20, 3),
('PhotoAttached',   21,  30, 3),
('PhotoAttached',   31,  40, 4),
('PhotoAttached',   41,  50, 4),
('PhotoAttached',   51,  60, 5),
('PhotoAttached',   61,  70, 5),
('PhotoAttached',   71,  80, 6),
('PhotoAttached',   81,  90, 7),
('PhotoAttached',   91, 100,10),

-- Location tags
('LocationTagged',    1,   5, 1),
('LocationTagged',    6,  10, 2),
('LocationTagged',   11,  20, 3),
('LocationTagged',   21,  30, 3),
('LocationTagged',   31,  40, 4),
('LocationTagged',   41,  50, 4),
('LocationTagged',   51,  60, 5),
('LocationTagged',   61,  70, 5),
('LocationTagged',   71,  80, 6),
('LocationTagged',   81,  90, 7),
('LocationTagged',   91, 100,10),

-- Friend tags
('FriendTagged',    1,   5, 1),
('FriendTagged',    6,  10, 2),
('FriendTagged',   11,  20, 3),
('FriendTagged',   21,  30, 3),
('FriendTagged',   31,  40, 4),
('FriendTagged',   41,  50, 4),
('FriendTagged',   51,  60, 5),
('FriendTagged',   61,  70, 5),
('FriendTagged',   71,  80, 6),
('FriendTagged',   81,  90, 7),
('FriendTagged',   91, 100,10),

-- Comment and Club Post badges
('Comment', 1, 5, 1),
('Comment', 6, 10, 2),
('Comment', 11, 20, 3),
('Comment', 21, 30, 4),
('Comment', 31, 40, 5),
('Comment', 41, 50, 5),
('Comment', 51, 60, 10),
('Comment', 61, 70, 10),
('Comment', 71, 80, 10),
('Comment', 81, 90, 20),
('Comment', 91, 100, 20),

-- Upvote badges
('Upvote', 1, 1, 1),
('Upvote', 2, 10, 2),
('Upvote', 11, 20, 5),
('Upvote', 21, 50, 10),
('Upvote', 51, 70, 20),
('Upvote', 71, 80, 25),
('Upvote', 81, 90, 35),
('Upvote', 91, 100, 50),

-- Club Posts
('ClubPost',   1,   5, 1),
('ClubPost',   6,  10, 2),
('ClubPost',  11,  20, 3),
('ClubPost',  21,  30, 4),
('ClubPost',  31,  40, 5),
('ClubPost',  41,  50, 5),
('ClubPost',  51,  60,10),
('ClubPost',  61,  70,10),
('ClubPost',  71,  80,10),
('ClubPost',  81,  90,20),
('ClubPost',  91, 100,20),

-- One-per-action badges
-- PublicList, FriendInvite, EventAttendance, NewDrink and Question
('PublicList', 1, 10, 1),
('FriendInvite', 1, 100, 1),
('EventAttendance', 1, 100, 1),
('NewDrink', 1, 100, 1),
('Question', 1, 100, 1);

-- ========= Seed badges table (Action Badges) =========
INSERT INTO "badges" ("badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity", "badgeLevel") VALUES
-- Extensive Reviews
('Shakespeare Ain''t Got Nothin''', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/1_User+submits+extensive+review_Shakespeare+Ain_t+Got+Nothin_.png', 'User is awarded a badge for extended reviews completed for ANY review.', 'Action', 'ExtensiveReview', 1),
-- Photo Reviews
('Lord Shutterbug', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/2_User+attaches+Photos+To+Review_Lord+Shutterbug.png', 'User is awarded a badge for photos attached for ANY review.', 'Action', 'PhotoAttached', 1),
-- Location Tags
('Checkpoint Collector', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/3_User+tags+Location+in+review_Checkpoint+Collector.png', 'User is awarded a badge for location tagged for ANY review.', 'Action', 'LocationTagged', 1),
-- Friend Tags
('Social Butterfly', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/4_User+tags+Friends+in+review_Social+Butterfly.png', 'User is awarded a badge for ANY number of friends tagged for ANY review.', 'Action', 'FriendTagged', 1),
-- Comments
('Rising Contributor', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/5_User+Comments_Rising+Contributor.png', 'User is awarded a badge for comments anywhere.', 'Action', 'Comment', 1),
-- Upvotes
('DrinkGPT', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/6_User+Upvotes+a+review_DrinkGPT.png', 'User is awarded a badge for Upvotes anywhere within 1 week of Post.', 'Action', 'Upvote', 1),
-- Public Lists
('List-o-mania', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/7_User+createa+a+drink+list_List-o-mania.png', 'User is awarded a badge for lists created that stay active for 1 week.', 'Action', 'PublicList', 1),
-- Club Posts
('In Da Club We All Fam', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/8_user+posts+in+any+Clubs_In+Da+Club+We+All+Fam.png', 'User is awarded a badge for posts made in ANY club.', 'Action', 'ClubPost', 1),
-- Friend Invites
('Get Me On The Guest List!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/9_user+invites+Friends.png', 'User is awarded a badge for each friend invited.', 'Action', 'FriendInvite', 1),
-- Event Attendance
('Master Of The RSVP', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/10_user+clicks+RSVP+on+any+Event_Master+Of+The+RSVP.png', 'User is awarded a badge for each event RSVP-ed and attended.', 'Action', 'EventAttendance', 1),
-- New Drink Listings
('Brew-tiful Mind', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/11_User+Requests+New+Drink+Listing+_+Suggests+Edit+for+Drink+Listing_Brew-tiful+Mind.png', 'User is awarded a badge for each Drink Listing added and approved / Edit suggested and approved.', 'Action', 'NewDrink', 1),
-- Questions for Producers/Venues
('Shoot Your Shot', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Action+Badges/12_User+Submits+Qns+For+Producers_Venues_Shoot+Your+Shot.png', 'User is awarded a badge for each Qn asked.', 'Action', 'Question', 1);

-- ========= Seed Country Badges =========
INSERT INTO "badges" ("badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity", "badgeLevel") VALUES
('The Rug Of A Lifetime', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/1_Afghanistan_The+Rug+Of+A+Lifetime.png', 'User is awarded a badge for reviews of drinks from Afghanistan.', 'Country', 'Afghanistan', 1),
('To The Peaks Of Ararat We Go', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/10_Armenia_To+The+Peaks+Of+Ararat+We+Go.png', 'User is awarded a badge for reviews of drinks from Armenia.', 'Country', 'Armenia', 1),
('Through The Dunes Of Petra', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/100_Jordan_Through+The+Dunes+Of+Petra.png', 'User is awarded a badge for reviews of drinks from Jordan.', 'Country', 'Jordan', 1),
('Find Me On The Silk Road', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/101_Kazakhstan_Find+Me+On+The+Silk+Road.png', 'User is awarded a badge for reviews of drinks from Kazakhstan.', 'Country', 'Kazakhstan', 1),
('Sunsets In The Serengeti', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/102_Kenya_Sunsets+In+The+Serengeti.png', 'User is awarded a badge for reviews of drinks from Kenya.', 'Country', 'Kenya', 1),
('One Country Two Clocks','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/103_Kiribati_One+Country+Two+Clocks.png', 'User is awarded a badge for reviews of drinks from Kiribati.', 'Country', 'Kiribati', 1),
('Check Out That Pristina', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/104_Kosovo_Check+Out+That+Pristina.png', 'User is awarded a badge for reviews of drinks from Kosovo.', 'Country', 'Kosovo', 1),
('614 Feet To The Persian Gulf','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/105_Kuwait_614+Feet+To+The+Persian+Gulf.png', 'User is awarded a badge for reviews of drinks from Kuwait.', 'Country', 'Kuwait', 1),
('Yurt Dreams On The Steppes','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/106_Kyrgyzstan_Yurt+Dreams+On+The+Steppes.png', 'User is awarded a badge for reviews of drinks from Kyrgyzstan.', 'Country', 'Kyrgyzstan', 1),
('Ain''t No Jar Like The Plains Of Jar','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/107_Laos_Ain_t+No+Jar+Like+The+Plains+Of+Jar.png', 'User is awarded a badge for reviews of drinks from Laos.', 'Country', 'Laos', 1),
('Into The Latvian Forests','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/108_Latvia_Into+The+Latvian+Forests.png', 'User is awarded a badge for reviews of drinks from Latvia.', 'Country', 'Latvia', 1),
('Meet Me In Beirut','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/109_Lebanon_Meet+Me+In+Beirut.png', 'User is awarded a badge for reviews of drinks from Lebanon.', 'Country', 'Lebanon', 1),
('Do The Divi Divi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/11_Aruba_Do+The+Divi+Divi.png', 'User is awarded a badge for reviews of drinks from Aruba.', 'Country', 'Aruba', 1),
('1,000 Meters Sky Up','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/110_Lesotho_1%2C000+Meters+Sky+Up.png', 'User is awarded a badge for reviews of drinks from Lesotho.', 'Country', 'Lesotho', 1),
('Turn Up The Radio','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/111_Liberia_Turn+Up+The+Radio.png', 'User is awarded a badge for reviews of drinks from Liberia.', 'Country', 'Liberia', 1),
('One Foot Forward In Leptis Magna','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/112_Libya_One+Foot+Forward+In+Leptis+Magna.png', 'User is awarded a badge for reviews of drinks from Libya.', 'Country', 'Libya', 1),
('Pre-Drinks In The Principality','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/113_Liechtenstein_Pre-Drinks+In+The+Principality.png', 'User is awarded a badge for reviews of drinks from Liechtenstein.', 'Country', 'Liechtenstein', 1),
('It''s Lit-huania','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/114_Lithuania_It_s+Lit-huania.png', 'User is awarded a badge for reviews of drinks from Lithuania.', 'Country', 'Lithuania', 1),
('Grand Duchy Gang','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/115_Luxembourg_Grand+Duchy+Gang.png', 'User is awarded a badge for reviews of drinks from Luxembourg.', 'Country', 'Luxembourg', 1),
('All Hail King Julien','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/116_Madagascar_All+Hail+King+Julien.png', 'User is awarded a badge for reviews of drinks from Madagascar.', 'Country', 'Madagascar', 1),
('Where To Cable Cars?','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/117_Madeira_Where+To+Cable+Cars.png', 'User is awarded a badge for reviews of drinks from Madeira.', 'Country', 'Madeira', 1),
('Kalimba Echoes From Nyasa To Mulanje','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/118_Malawi_Kalimba+Echoes+From+Nyasa+To+Mulanje.png', 'User is awarded a badge for reviews of drinks from Malawi.', 'Country', 'Malawi', 1),
('Roti Canai Makes For A Good Pairing','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/119_Malaysia_Roti+Canai+Makes+For+A+Good+Pairing.png', 'User is awarded a badge for reviews of drinks from Malaysia.', 'Country', 'Malaysia', 1),
('Kangaroos Out Where?','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/12_Australia_Kangaroos+Out+Where.png', 'User is awarded a badge for reviews of drinks from Australia.', 'Country', 'Australia', 1),
('Mas Huni First Thing In the Morn','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/120_Maldives_Mas+Huni+First+Thing+In+the+Morn.png', 'User is awarded a badge for reviews of drinks from Maldives.', 'Country', 'Maldives', 1),
('Get Me On The First Flight To Timbuktu','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/121_Mali_Get+Me+On+The+First+Flight+To+Timbuktu.png', 'User is awarded a badge for reviews of drinks from Mali.', 'Country', 'Mali', 1),
('The Knights Of Malta','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/122_Malta_The+Knights+Of+Malta.png', 'User is awarded a badge for reviews of drinks from Malta.', 'Country', 'Malta', 1),
('Windmills By The Grand Bourg','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/123_Marie+Galante_Windmills+By+The+Grand+Bourg.png', 'User is awarded a badge for reviews of drinks from Marie Galante.', 'Country', 'Marie Galante', 1),
('Whip Out The Pokedex','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/124_Marshall+Islands_Whip+Out+The+Pokedex.png', 'User is awarded a badge for reviews of drinks from Marshall Islands.', 'Country', 'Marshall Islands', 1),
('Have No Fear Mount Pelee','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/125_Martinique_Have+No+Fear+Mount+Pelee.png', 'User is awarded a badge for reviews of drinks from Martinique.', 'Country', 'Martinique', 1),
('Mint Tea At Oualata Will Do','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/126_Mauritania_Mint+Tea+At+Oualata+Will+Do.png', 'User is awarded a badge for reviews of drinks from Mauritania.', 'Country', 'Mauritania', 1),
('On The Hunt For A Dodo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/127_Mauritius_On+The+Hunt+For+A+Dodo.png', 'User is awarded a badge for reviews of drinks from Mauritius.', 'Country', 'Mauritius', 1),
('Aztec Avengers Assemble','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/128_Mexico+Lucha+Libre+Legend.png', 'User is awarded a badge for reviews of drinks from Mexico.', 'Country', 'Mexico', 1),
('Walnuts Cracking In Chisinau','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/129_Moldova_Walnuts+Cracking+In+Chisinau.png', 'User is awarded a badge for reviews of drinks from Moldova.', 'Country', 'Moldova', 1),
('Channeling Mozart','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/13_Austria_Channeling+Mozart.png', 'User is awarded a badge for reviews of drinks from Austria.', 'Country', 'Austria', 1),
('High Rolling At Monte Carlo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/130_Monaco_High+Rolling+At+Monte+Carlo.png', 'User is awarded a badge for reviews of drinks from Monaco.', 'Country', 'Monaco', 1),
('A Swig Of The Arkhi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/131_Mongolia_A+Swig+Of+The+Arkhi.png', 'User is awarded a badge for reviews of drinks from Mongolia.', 'Country', 'Mongolia', 1),
('Pounding The Walls Of Budva','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/132_Montenegro_Pounding+The+Walls+Of+Budva.png', 'User is awarded a badge for reviews of drinks from Montenegro.', 'Country', 'Montenegro', 1),
('Tagines And Souks At Chefchaouen','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/133_Morocco_Tagines+And+Souks+At+Chefchaouen.png', 'User is awarded a badge for reviews of drinks from Morocco.', 'Country', 'Morocco', 1),
('The Lost Eden Of Gorongosa','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/134_Mozambique_The+Lost+Eden+Of+Gorongosa.png', 'User is awarded a badge for reviews of drinks from Mozambique.', 'Country', 'Mozambique', 1),
('Reflections Of A Mirror At Inle','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/135_Myanmar_Reflections+Of+A+Mirror+At+Inle.png', 'User is awarded a badge for reviews of drinks from Myanmar.', 'Country', 'Myanmar', 1),
('Lost in the Namibian Sands','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/136_Namibia_Lost+in+the+Namibian+Sands.png', 'User is awarded a badge for reviews of drinks from Namibia.', 'Country', 'Namibia', 1),
('Moonwalking To Anibare','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/137_Nauru_Moonwalking+To+Anibare.png', 'User is awarded a badge for reviews of drinks from Nauru.', 'Country', 'Nauru', 1),
('Say Namaskar To The Sherpas','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/138_Nepal_Say+Namaskar+To+The+Sherpas.png', 'User is awarded a badge for reviews of drinks from Nepal.', 'Country', 'Nepal', 1),
('Orange Army','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/139_Netherlands_Orange+Army.png', 'User is awarded a badge for reviews of drinks from Netherlands.', 'Country', 'Netherlands', 1),
('Where''s That Petroglyph Again?','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/14_Azerbaijan_Where_s+That+Petroglyph+Again.png', 'User is awarded a badge for reviews of drinks from Azerbaijan.', 'Country', 'Azerbaijan', 1),
('Running Through The Rotorua','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/140_New+Zealand_Running+Through+The+Rotorua.png', 'User is awarded a badge for reviews of drinks from New Zealand.', 'Country', 'New Zealand', 1),
('On The Trail Of Laguna De Apoyo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/141_Nicaragua_On+The+Trail+Of+Laguna+De+Apoyo.png', 'User is awarded a badge for reviews of drinks from Nicaragua.', 'Country', 'Nicaragua', 1),
('Sacred Handshakes','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/142_Niger_Sacred+Handshakes.png', 'User is awarded a badge for reviews of drinks from Niger.', 'Country', 'Niger', 1),
('Jollof On Lagos Streets','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/143_Nigeria_Jollof+On+Lagos+Streets.png', 'User is awarded a badge for reviews of drinks from Nigeria.', 'Country', 'Nigeria', 1),
('Give Me That TDG','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/144_North+Korea_Give+Me+That+TDG.png', 'User is awarded a badge for reviews of drinks from North Korea.', 'Country', 'North Korea', 1),
('The Water''s Nice At Ohrid','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/145_North+Macedonia_The+Water_s+Nice+At+Ohrid.png', 'User is awarded a badge for reviews of drinks from North Macedonia.', 'Country', 'North Macedonia', 1),
('Make Haste, Belfast Waits','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/146_Northern+Ireland_Make+Haste%2C+Belfast+Waits.png', 'User is awarded a badge for reviews of drinks from Northern Ireland.', 'Country', 'Northern Ireland', 1),
('The Stuff Of Viking Legends','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/147_Norway_The+Stuff+Of+Viking+Legends.png', 'User is awarded a badge for reviews of drinks from Norway.', 'Country', 'Norway', 1),
('A Dab Of Frankincense','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/148_Oman_A+Dab+Of+Frankincense.png', 'User is awarded a badge for reviews of drinks from Oman.', 'Country', 'Oman', 1),
('Midnight in Karachi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/149_Pakistan_Midnight+in+Karachi.png', 'User is awarded a badge for reviews of drinks from Pakistan.', 'Country', 'Pakistan', 1),
('Do The Kokomo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/15_Bahamas_Do+The+Kokomo.png', 'User is awarded a badge for reviews of drinks from Bahamas.', 'Country', 'Bahamas', 1),
('That Is One Jelly (Fish) Too Many','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/150_Palau_That+Is+One+Jelly+(Fish)+Too+Many.png', 'User is awarded a badge for reviews of drinks from Palau.', 'Country', 'Palau', 1),
('May The Force Be With You','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/151_Palestinian+Territories_May+The+Force+Be+With+You.png', 'User is awarded a badge for reviews of drinks from Palestinian Territories.', 'Country', 'Palestinian Territories', 1),
('A Cruise Down The Canal','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/152_Panama_A+Cruise+Down+The+Canal.png', 'User is awarded a badge for reviews of drinks from Panama.', 'Country', 'Panama', 1),
('From Itaipú To The Iguazu','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/154_Paraguay_From+Itaip%C3%BA+To+The+Iguazu.png', 'User is awarded a badge for reviews of drinks from Paraguay.', 'Country', 'Paraguay', 1),
('Inca-hoots','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/155_Peru_Inca-hoots.png', 'User is awarded a badge for reviews of drinks from Peru.', 'Country', 'Peru', 1),
('Bayanihan Spirit','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/156_Philippines_Bayanihan+Spirit.png', 'User is awarded a badge for reviews of drinks from Philippines.', 'Country', 'Philippines', 1),
('Fuelled By Pierogi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/157_Poland_Fuelled+By+Pierogi.png', 'User is awarded a badge for reviews of drinks from Poland.', 'Country', 'Poland', 1),
('Following The Porto Trail','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/158_Portugal_Following+The+Porto+Trail.png', 'User is awarded a badge for reviews of drinks from Portugal.', 'Country', 'Portugal', 1),
('San Juan Cooler Shakedown','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/159_Puerto+Rico_San+Juan+Cooler+Shakedown.png', 'User is awarded a badge for reviews of drinks from Puerto Rico.', 'Country', 'Puerto Rico', 1),
('Free Diving For Pearls In The Gulf','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/16_Bahrain_Free+Diving+For+Pearls+In+The+Gulf.png', 'User is awarded a badge for reviews of drinks from Bahrain.', 'Country', 'Bahrain', 1),
('A Date Over Gahwa','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/160_Qatar_A+Date+Over+Gahwa.png', 'User is awarded a badge for reviews of drinks from Qatar.', 'Country', 'Qatar', 1),
('Crashing Leu Tempo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/161_R%C3%A9union+Island_Crashing+Leu+Tempo.png', 'User is awarded a badge for reviews of drinks from Réunion Island.', 'Country', 'Réunion Island', 1),
('Drinking Like Dracula','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/162_Romania_Drinking+Like+Dracula.png', 'User is awarded a badge for reviews of drinks from Romania.', 'Country', 'Romania', 1),
('Just Chillin'' In Siberia','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/163_Russia_Just+Chillin_+In+Siberia.png', 'User is awarded a badge for reviews of drinks from Russia.', 'Country', 'Russia', 1),
('Kigali Kings','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/164_Rwanda_Kigali+Kings.png', 'User is awarded a badge for reviews of drinks from Rwanda.', 'Country', 'Rwanda', 1),
('The Who''s Who Of Gustavia','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/165_Saint+Barthelemy_The+Who_s+Who+Of+Gustavia.png', 'User is awarded a badge for reviews of drinks from Saint Barthelemy.', 'Country', 'Saint Barthelemy', 1),
('Gumwood, Plovers And A Saint Helena Latte','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/166_Saint+Helena_Gumwood%2C+Plovers+And+A+Saint+Helena+Latte.png', 'User is awarded a badge for reviews of drinks from Saint Helena.', 'Country', 'Saint Helena', 1),
('Between Basseterre And Brimstone','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/167_Saint+Kitts+and+Nevis_Between+Basseterre+And+Brimstone.png', 'User is awarded a badge for reviews of drinks from Saint Kitts and Nevis.', 'Country', 'Saint Kitts and Nevis', 1),
('Drive-Thru Volcano 70 Meters Ahead','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/168_Saint+Lucia_Drive-Thru+Volcano+70+Meters+Ahead.png', 'User is awarded a badge for reviews of drinks from Saint Lucia.', 'Country', 'Saint Lucia', 1),
('Two More Sunrises At La Samanna','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/169_Saint+Martin_Two+More+Sunrises+At+La+Samanna.png', 'User is awarded a badge for reviews of drinks from Saint Martin.', 'Country', 'Saint Martin', 1),
('Turn On Them Calypso Tunes','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/170_Saint+Vincent_Turn+On+Them+Calypso+Tunes.png', 'User is awarded a badge for reviews of drinks from Saint Vincent.', 'Country', 'Saint Vincent', 1),
('Manumea''s Last Seen At Afu Aau','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/171_Samoa_Manumea_s+Last+Seen+At+Afu+Aau.png', 'User is awarded a badge for reviews of drinks from Samoa.', 'Country', 'Samoa', 1),
('Three Towers At Dusk','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/172_San+Marino_Three+Towers+At+Dusk.png', 'User is awarded a badge for reviews of drinks from San Marino.', 'Country', 'San Marino', 1),
('The Return Of The Cacao','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/173_Sao+Tome+and+Principe_The+Return+Of+The+Cacao.png', 'User is awarded a badge for reviews of drinks from Sao Tome and Principe.', 'Country', 'Sao Tome and Principe', 1),
('You''re Kilting It!','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/174_Scotland_You%E2%80%99re+Kilting+It!.png', 'User is awarded a badge for reviews of drinks from Scotland.', 'Country', 'Scotland', 1),
('No Braking From Paris To Dakar','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/175_Senegal_No+Braking+From+Paris+To+Dakar.png', 'User is awarded a badge for reviews of drinks from Senegal.', 'Country', 'Senegal', 1),
('Three Drinks With Novak','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/176_Serbia_Three+Drinks+With+Novak.png', 'User is awarded a badge for reviews of drinks from Serbia.', 'Country', 'Serbia', 1),
('Seven Coco De Mer, Four Giant Tortoises','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/177_Seychelles_Seven+Coco+De+Mer%2C+Four+Giant+Tortoises.png', 'User is awarded a badge for reviews of drinks from Seychelles.', 'Country', 'Seychelles', 1),
('A Most Prized Cotton','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/178_Sierra+Leone_A+Most+Prized+Cotton.png', 'User is awarded a badge for reviews of drinks from Sierra Leone.', 'Country', 'Sierra Leone', 1),
('In Search Of Merlions','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/179_Singapore_In+Search+Of+Merlions.png', 'User is awarded a badge for reviews of drinks from Singapore.', 'Country', 'Singapore', 1),
('Bratislava Squad','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/180_Slovakia_Bratislava+Squad.png', 'User is awarded a badge for reviews of drinks from Slovakia.', 'Country', 'Slovakia', 1),
('Legends Are Made In Ljubljana', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/181_Slovenia_Legends+Are+Made+In+Ljubljana.png', 'User is awarded a badge for reviews of drinks from Slovenia.', 'Country', 'Slovenia', 1),
('Is That Ship Alright?','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/182_Solomon+Islands_Is+That+Ship+Alright.png', 'User is awarded a badge for reviews of drinks from Solomon Islands.', 'Country', 'Solomon Islands', 1),
('Deciphering Laas Geel''s Dinner Order','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/183_Somalia_Deciphering+Laas+Geel_s+Dinner+Order.png', 'User is awarded a badge for reviews of drinks from Somalia.', 'Country', 'Somalia', 1),
('I''m Getting Notes Of Springbok','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/184_South+Africa_I_m+Getting+Notes+Of+Springbok.png', 'User is awarded a badge for reviews of drinks from South Africa.', 'Country', 'South Africa', 1),
('Kimchi Chowdown','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/185_South+Korea_Kimchi+Chowdown.png', 'User is awarded a badge for reviews of drinks from South Korea.', 'Country', 'South Korea', 1),
('Siesta Sounds About Right','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/186_Spain_Siesta+Sounds+About+Right.png', 'User is awarded a badge for reviews of drinks from Spain.', 'Country', 'Spain', 1),
('Elephants Love A Good Par-Tea Too','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/187_Sri+Lanka_Elephants+Love+A+Good+Par-Tea+Too.png', 'User is awarded a badge for reviews of drinks from Sri Lanka.', 'Country', 'Sri Lanka', 1),
('Blue Meets White On The Nile','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/188_Sudan_Blue+Meets+White+On+The+Nile.png', 'User is awarded a badge for reviews of drinks from Sudan.', 'Country', 'Sudan', 1),
('The Start Of Something New','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/189_Sudan%2C+South_The+Start+Of+Something+New.png', 'User is awarded a badge for reviews of drinks from South Sudan.', 'Country', 'South Sudan', 1),
('Saoto Soup Along The Saramacca','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/190_Suriname_Saoto+Soup+Along+The+Saramacca.png', 'User is awarded a badge for reviews of drinks from Suriname.', 'Country', 'Suriname', 1),
('ABBA All Stars','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/191_Sweden+Self-Assemble+the+Good+times.png', 'User is awarded a badge for reviews of drinks from Sweden.', 'Country', 'Sweden', 1),
('It''s The Matterhorn Or Broke','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/192_Switzerland_It_s+The+Matterhorn+Or+Broke192_Switzerland_It_s+The+Matterhorn+Or+Broke.png', 'User is awarded a badge for reviews of drinks from Switzerland.', 'Country', 'Switzerland', 1),
('Damascus Come Out At Dusk','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/193_Syria_Damascus+Come+Out+At+Dusk.png', 'User is awarded a badge for reviews of drinks from Syria.', 'Country', 'Syria', 1),
('A Road Leading To Domoda', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/198_The+Gambia_A+Road+Leading+To+Domoda.png', 'User is awarded a badge for reviews of drinks from The Gambia.', 'Country', 'Gambia', 1),
('Drop That Bubble Tea','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/194_Taiwan_Drop+That+Bubble+Tea.png', 'User is awarded a badge for reviews of drinks from Taiwan.', 'Country', 'Taiwan', 1),
('Golden Days Of Saffron','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/195_Tajikistan_Golden+Days+Of+Saffron+(2).png', 'User is awarded a badge for reviews of drinks from Tajikistan.', 'Country', 'Tajikistan', 1),
('Tom Yum For The Soul','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/197_Thailand_Tom+Yum+For+The+Soul.png', 'User is awarded a badge for reviews of drinks from Thailand.', 'Country', 'Thailand', 1),
('Head First Into Lake Togo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/199_Togo_Head+First+Into+Lake+Togo.png', 'User is awarded a badge for reviews of drinks from Togo.', 'Country', 'Togo', 1),
('Long Live The Rye','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/2_%C3%85land+Islands_Long+Live+The+Rye.png', 'User is awarded a badge for reviews of drinks from Åland Islands.', 'Country', 'Åland Islands', 1),
('Brugge-licious','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/20_Belgium_Brugge-licious.png', 'User is awarded a badge for reviews of drinks from Belgium.', 'Country', 'Belgium', 1),
('No Party Without Ha''amonga A Maui','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/200_Tonga_No+Party+Without+Ha_amonga+A+Maui.png', 'User is awarded a badge for reviews of drinks from Tonga.', 'Country', 'Tonga', 1),
('Of Bitters And Myths','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/201_Trinidad+and+Tobago_Of+Bitters+And+Myths.png', 'User is awarded a badge for reviews of drinks from Trinidad and Tobago.', 'Country', 'Trinidad and Tobago', 1),
('Adventures In The Medina','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/202_Tunisia_Adventures+In+The+Medina.png', 'User is awarded a badge for reviews of drinks from Tunisia.', 'Country', 'Tunisia', 1),
('Do The Ottoman','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/203_Turkey_Do+The+Ottoman.png', 'User is awarded a badge for reviews of drinks from Turkey.', 'Country', 'Turkey', 1),
('Tunnelling Through Time At Merv','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/204_Turkmenistan_Tunnelling+Through+Time+At+Merv.png', 'User is awarded a badge for reviews of drinks from Turkmenistan.', 'Country', 'Turkmenistan', 1),
('Atolls A Many','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/205_Tuvalu_Atolls+A+Many.png', 'User is awarded a badge for reviews of drinks from Tuvalu.', 'Country', 'Tuvalu', 1),
('Kampala Crew','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/206_Uganda_Kampala+Crew.png', 'User is awarded a badge for reviews of drinks from Uganda.', 'Country', 'Uganda', 1),
('Running On Borscht','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/207_Ukraine_Running+On+Borscht.png', 'User is awarded a badge for reviews of drinks from Ukraine.', 'Country', 'Ukraine', 1),
('1,001 Arabian Nights','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/208_United+Arab+Emirates_1001+Arabian+Nights.png', 'User is awarded a badge for reviews of drinks from United Arab Emirates.', 'Country', 'United Arab Emirates', 1),
('Rocking With Some Royals','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/209_United+Kingdom_Rocking+With+Some+Royals.png', 'User is awarded a badge for reviews of drinks from United Kingdom.', 'Country', 'United Kingdom', 1),
('The All American Dream Team','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/210_United+States_The+All+American+Dream+Team.png', 'User is awarded a badge for reviews of drinks from United States.', 'Country', 'United States', 1),
('A Tango In Montevideo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/211_Uruguay_A+Tango+In+Montevideo.png', 'User is awarded a badge for reviews of drinks from Uruguay.', 'Country', 'Uruguay', 1),
('More Life At St. Thomas','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/212_US+Virgin+Islands_More+Life+At+St.+Thomas.png', 'User is awarded a badge for reviews of drinks from US Virgin Islands.', 'Country', 'US Virgin Islands', 1),
('2 PM In Registan Square','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/213_Uzbekistan_2+PM+In+Registan+Square.png', 'User is awarded a badge for reviews of drinks from Uzbekistan.', 'Country', 'Uzbekistan', 1),
('The Hibiscus Are In Full Bloom','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/214_Vanuatu_The+Hibiscus+Are+In+Full+Bloom.png', 'User is awarded a badge for reviews of drinks from Vanuatu.', 'Country', 'Vanuatu', 1),
('Possibly The Best Sacramental Wine','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/215_Vatican+City_Possibly+The+Best+Sacramental+Wine.png', 'User is awarded a badge for reviews of drinks from Vatican City.', 'Country', 'Vatican City', 1),
('Two More Arepas, Good Sir!','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/216_Venezuela_Two+More+Arepas%2C+Good+Sir!.png', 'User is awarded a badge for reviews of drinks from Venezuela.', 'Country', 'Venezuela', 1),
('In The Shade Of The Mekong','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/217_Vietnam_In+The+Shade+Of+The+Mekong+_+Honk+If+You_re+Happy.png', 'User is awarded a badge for reviews of drinks from Vietnam.', 'Country', 'Vietnam', 1),
('The Red Dragon Troop','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/218_Wales_The+Red+Dragon+Troop.png', 'User is awarded a badge for reviews of drinks from Wales.', 'Country', 'Wales', 1),
('Dragon''s Blood Is The Secret Ingredient','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/219_Yemen_Dragon_s+Blood+Is+The+Secret+Ingredient.png', 'User is awarded a badge for reviews of drinks from Yemen.', 'Country', 'Yemen', 1),
('Three Tickets To Zinzou','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/22_Benin_Three+Tickets+To+Zinzou.png', 'User is awarded a badge for reviews of drinks from Benin.', 'Country', 'Benin', 1),
('Biltongs On The Zambezi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/220_Zambia_Biltongs+On+The+Zambezi.png', 'User is awarded a badge for reviews of drinks from Zambia.', 'Country', 'Zambia', 1),
('Kudu Spotting Under Victoria Falls','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/221_Zimbabwe_Kudu+Spotting+Under+Victoria+Falls.png', 'User is awarded a badge for reviews of drinks from Zimbabwe.', 'Country', 'Zimbabwe', 1),
('Did My Drink Disappear Again?','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/23_Bermuda_Did+My+Drink+Disappear+Again.png', 'User is awarded a badge for reviews of drinks from Bermuda.', 'Country', 'Bermuda', 1),
('Himalayan Hustle','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/24_Bhutan_Himalayan+Hustle.png', 'User is awarded a badge for reviews of drinks from Bhutan.', 'Country', 'Bhutan', 1),
('Saltenas In La Paz','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/25_Bolivia_Saltenas+In+La+Paz.png', 'User is awarded a badge for reviews of drinks from Bolivia.', 'Country', 'Bolivia', 1),
('Romping Through Sarajevo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/26_Bosnia+and+Herzegovina_Romping+Through+Sarajevo.png', 'User is awarded a badge for reviews of drinks from Bosnia and Herzegovina.', 'Country', 'Bosnia and Herzegovina', 1),
('Happy Hours On At The Kalahari','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/27_Botswana_Happy+Hours+On+At+The+Kalahari.png', 'User is awarded a badge for reviews of drinks from Botswana.', 'Country', 'Botswana', 1),
('Rio Rockstar','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/28_Brazil_Rio+Rockstar.png', 'User is awarded a badge for reviews of drinks from Brazil.', 'Country', 'Brazil', 1),
('Foxy''s Bar Here I Come','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/29_British+Virgin+Islands_Foxy_s+Bar+Here+I+Come.png', 'User is awarded a badge for reviews of drinks from British Virgin Islands.', 'Country', 'British Virgin Islands', 1),
('No Window Shopping At Berat','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/3_Albania_No+Window+Shopping+At+Berat.png', 'User is awarded a badge for reviews of drinks from Albania.', 'Country', 'Albania', 1),
('One Billion Barrels Needs A Monument','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/30_Brunei_One+Billion+Barrels+Needs+A+Monument.png', 'User is awarded a badge for reviews of drinks from Brunei.', 'Country', 'Brunei', 1),
('Giving My Balkan Best','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/31_Bulgaria_Giving+My+Balkan+Best.png', 'User is awarded a badge for reviews of drinks from Bulgaria.', 'Country', 'Bulgaria', 1),
('The Finest Faso Dan Fani At The Grand Marche','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/32_Burkina+Faso_The+Finest+Faso+Dan+Fani+At+The+Grand+Marche.png', 'User is awarded a badge for reviews of drinks from Burkina Faso.', 'Country', 'Burkina Faso', 1),
('Big Steps Of Urunani','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/33_Burundi_Big+Steps+Of+Urunani.png', 'User is awarded a badge for reviews of drinks from Burundi.', 'Country', 'Burundi', 1),
('Temple Running Through Angkor Wat','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/34_Cambodia_Temple+Running+Through+Angkor+Wat_Cameroon_The+Fufu+Of+It+All.png', 'User is awarded a badge for reviews of drinks from Cambodia.', 'Country', 'Cambodia', 1),
('The Fufu Of It All','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/35_Cameroon_The+Fufu+Of+It+All.png', 'User is awarded a badge for reviews of drinks from Cameroon.', 'Country', 'Cameroon', 1),
('Poutine Pairing','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/36_Canada_Poutine+Pairing.png', 'User is awarded a badge for reviews of drinks from Canada.', 'Country', 'Canada', 1),
('Mojo Sauce Reigns Supreme','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/37_Canary+Islands_Mojo+Sauce+Reigns+Supreme.png', 'User is awarded a badge for reviews of drinks from Canary Islands.', 'Country', 'Canary Islands', 1),
('Morabeza Vibes Down Mount Fogo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/38_Cape+Verde_Morabeza+Vibes+Down+Mount+Fogo.png', 'User is awarded a badge for reviews of drinks from Cape Verde.', 'Country', 'Cape Verde', 1),
('All''s Fair Under The Cayman Sun','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/39_Cayman+Islands_All_s+Fair+Under+The+Cayman+Sun.png', 'User is awarded a badge for reviews of drinks from Cayman Islands.', 'Country', 'Cayman Islands', 1),
('Visions Of The Casbah','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/4_Algeria_Visions+Of+The+Casbah.png', 'User is awarded a badge for reviews of drinks from Algeria.', 'Country', 'Algeria', 1),
('The Game Lives On In Dzongli-Mounga','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/40_Central+African+Republic_The+Game+Lives+On+In+Dzongli-Mounga.png', 'User is awarded a badge for reviews of drinks from Central African Republic.', 'Country', 'Central African Republic', 1),
('Warwm Bidi On The Tibesti Way','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/41_Chad_Warwm+Bidi+On+The+Tibesti+Way.png', 'User is awarded a badge for reviews of drinks from Chad.', 'Country', 'Chad', 1),
('Santiago Sensibilities','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/42_Chile_Santiago+Sensibilities.png', 'User is awarded a badge for reviews of drinks from Chile.', 'Country', 'Chile', 1),
('Guardians Of The Great Wall','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/43_China_Guardians+Of+The+Great+Wall.png', 'User is awarded a badge for reviews of drinks from China.', 'Country', 'China', 1),
('Hot Tamales In Cartagena','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/44_Colombia_Hot+Tamales+In+Cartagena.png', 'User is awarded a badge for reviews of drinks from Colombia.', 'Country', 'Colombia', 1),
('A Most Sparkling Madhyouni Dance','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/45_Comoros_A+Most+Sparkling+Madhyouni+Dance.png', 'User is awarded a badge for reviews of drinks from Comoros.', 'Country', 'Comoros', 1),
('Coffee Beans & Pura Vida','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/46_Costa+Rica_Coffee+Beans+%26+Pura+Vida.png', 'User is awarded a badge for reviews of drinks from Costa Rica.', 'Country', 'Costa Rica', 1),
('Cocoa Got Me Dancing The Yacouba','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/47_C%C3%B4te+d%E2%80%99Ivoire_Cocoa+Got+Me+Dancing+The+Yacouba.png', 'User is awarded a badge for reviews of drinks from Côte d’Ivoire.', 'Country', 'Côte d’Ivoire', 1),
('Quaffing Down The Adriatic','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/48_Croatia_Quaffing+Down+The+Adriatic.png', 'User is awarded a badge for reviews of drinks from Croatia.', 'Country', 'Croatia', 1),
('One More Tostone For The Road','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/49_Cuba_One+More+Tostone+For+The+Road.png', 'User is awarded a badge for reviews of drinks from Cuba.', 'Country', 'Cuba', 1),
('Halloumi Heroes','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/50_Cyprus_Halloumi+Heroes.png', 'User is awarded a badge for reviews of drinks from Cyprus.', 'Country', 'Cyprus', 1),
('A Grandvalira Match Up On Snow Polo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/5+Andorra_A+Grandvalira+Match+Up+On+Snow+Polo.png', 'User is awarded a badge for reviews of drinks from Andorra.', 'Country', 'Andorra', 1),
('Czechmate!','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/51_Czech+Republic_Czechmate!.png', 'User is awarded a badge for reviews of drinks from Czech Republic.', 'Country', 'Czech Republic', 1),
('Silverbacks Take Pints Too','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/52_Democratic+Republic+of+the+Congo_Silverbacks+Take+Pints+Too.png', 'User is awarded a badge for reviews of drinks from Democratic Republic of the Congo.', 'Country', 'Democratic Republic of the Congo', 1),
('Lego Grab Some Drinks','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/53_Denmark_Lego+Grab+Some+Drinks.png', 'User is awarded a badge for reviews of drinks from Denmark.', 'Country', 'Denmark', 1),
('Elks Passing The Arta','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/54_Djibouti_Elks+Passing+The+Arta.png', 'User is awarded a badge for reviews of drinks from Djibouti.', 'Country', 'Djibouti', 1),
('Just Simmering At Morne Trois Pitons','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/55_Dominica_Just+Simmering+At+Morne+Trois+Pitons.png', 'User is awarded a badge for reviews of drinks from Dominica.', 'Country', 'Dominica', 1),
('Salsa Dancing In Santo Domingo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/56_Dominican+Republic_Salsa+Dancing+In+Santo+Domingo.png', 'User is awarded a badge for reviews of drinks from Dominican Republic.', 'Country', 'Dominican Republic', 1),
('Sabuko Down To The Last Slurp','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/57_East+Timor+(Timor-Leste)_Sabuko+Down+To+The+Last+Slurp.png', 'User is awarded a badge for reviews of drinks from East Timor (Timor-Leste).', 'Country', 'East Timor (Timor-Leste)', 1),
('Galapagos Diaries','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/58_Ecuador_Galapagos+Diaries.png', 'User is awarded a badge for reviews of drinks from Ecuador.', 'Country', 'Ecuador', 1),
('Sipping On The Nile','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/59_Egypt_Sipping+On+The+Nile.png', 'User is awarded a badge for reviews of drinks from Egypt.', 'Country', 'Egypt', 1),
('Mind The (Tundavala) Gap','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/6_Angola_Mind+The+(Tundavala)+Gap.png', 'User is awarded a badge for reviews of drinks from Angola.', 'Country', 'Angola', 1),
('Salud In The Land Of Volcano','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/60_El+Salvador_Salud+In+The+Land+Of+Volcano.png', 'User is awarded a badge for reviews of drinks from El Salvador.', 'Country', 'El Salvador', 1),
('A Night In Mongomo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/61_Equatorial+Guinea_A+Night+In+Mongomo.png', 'User is awarded a badge for reviews of drinks from Equatorial Guinea.', 'Country', 'Equatorial Guinea', 1),
('It''s A Real Architectural Digest Here','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/62_Eritrea_It_s+A+Real+Architectural+Digest+Here.png', 'User is awarded a badge for reviews of drinks from Eritrea.', 'Country', 'Eritrea', 1),
('Folklores In Tallinn','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/63_Estonia_Folklores+In+Tallinn.png', 'User is awarded a badge for reviews of drinks from Estonia.', 'Country', 'Estonia', 1),
('Check In At The Royal Swazi','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/64_Eswatini_Check+In+At+The+Royal+Swazi.png', 'User is awarded a badge for reviews of drinks from Eswatini.', 'Country', 'Eswatini', 1),
('Thank Kaldi We Have Caffeine','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/65_Ethiopia_Thank+Kaldi+We+Have+Caffeine.png', 'User is awarded a badge for reviews of drinks from Ethiopia.', 'Country', 'Ethiopia', 1),
('Puffin Power Up','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/66_Faroe+Islands_Puffin+Power+Up.png', 'User is awarded a badge for reviews of drinks from Faroe Islands.', 'Country', 'Faroe Islands', 1),
('Bula All Around At Viti Levu','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/67_Fiji_Bula+All+Around+At+Viti+Levu.png', 'User is awarded a badge for reviews of drinks from Fiji.', 'Country', 'Fiji', 1),
('Sauna Stunnin','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/68_Finland_Sauna+Stunnin_.png', 'User is awarded a badge for reviews of drinks from Finland.', 'Country', 'Finland', 1),
('The Baguette Brigade','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/69_France_The+Baguette+Brigade.png', 'User is awarded a badge for reviews of drinks from France.', 'Country', 'France', 1),
('Every Turtle Has Its Day','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/7_Anguilla_Every+Turtle+Has+Its+Day.png', 'User is awarded a badge for reviews of drinks from Anguilla.', 'Country', 'Anguilla', 1),
('The Spirit Of Heiva','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/70_French+Polynesia_The+Spirit+Of+Heiva.png', 'User is awarded a badge for reviews of drinks from French Polynesia.', 'Country', 'French Polynesia', 1),
('Roar Of The Black Panther','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/71_Gabon_Roar+Of+The+Black+Panther.png', 'User is awarded a badge for reviews of drinks from Gabon.', 'Country', 'Gabon', 1),
('Say Tbilisi!','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/72_Georgia_Say+Tbilisi!.png', 'User is awarded a badge for reviews of drinks from Georgia.', 'Country', 'Georgia', 1),
('One Night In Cologne','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/73_Germany_One+Night+In+Cologne.png', 'User is awarded a badge for reviews of drinks from Germany.', 'Country', 'Germany', 1),
('Banku Makes Anything Taste Good','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/74_Ghana_Banku+Makes+Anything+Taste+Good.png', 'User is awarded a badge for reviews of drinks from Ghana.', 'Country', 'Ghana', 1),
('Hellenistic State Of Mind','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/75_Greece_Hellenistic+State+Of+Mind.png', 'User is awarded a badge for reviews of drinks from Greece.', 'Country', 'Greece', 1),
('Disko Bay To The Northern Lights','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/76_Greenland_Disko+Bay+To+The+Northern+Lights.png', 'User is awarded a badge for reviews of drinks from Greenland.', 'Country', 'Greenland', 1),
('The Nutmeg Side Of Things','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/77_Grenada_The+Nutmeg+Side+Of+Things.png', 'User is awarded a badge for reviews of drinks from Grenada.', 'Country', 'Grenada', 1),
('Gwoka Dance And Gwoka Sing','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/78_Guadeloupe_Gwoka+Dance+And+Gwoka+Sing.png', 'User is awarded a badge for reviews of drinks from Guadeloupe.', 'Country', 'Guadeloupe', 1),
('Hafa Adai, Islander Pride','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/79_Guam_Hafa+Adai%2C+Islander+Pride.png', 'User is awarded a badge for reviews of drinks from Guam.', 'Country', 'Guam', 1),
('A Cargo Of Black Pineapples By Nelson''s','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/8_Antigua_A+Cargo+Of+Black+Pineapples+By+Nelson_s.png', 'User is awarded a badge for reviews of drinks from Antigua.', 'Country', 'Antigua', 1),
('1, 2, 3, Say Quetzal!','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/80_Guatemala_1%2C+2%2C+3%2C+Say+Quetzal!.png', 'User is awarded a badge for reviews of drinks from Guatemala.', 'Country', 'Guatemala', 1),
('Golden Milk At The Little Chapel','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/81_Guernsey_Golden+Milk+At+The+Little+Chapel.png', 'User is awarded a badge for reviews of drinks from Guernsey.', 'Country', 'Guernsey', 1),
('Rifts On The Balafon','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/82_Guinea_Rifts+On+The+Balafon.png', 'User is awarded a badge for reviews of drinks from Guinea.', 'Country', 'Guinea', 1),
('Greenheart Down The Essequibo','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/83_Guyana_Greenheart+Down+The+Essequibo.png', 'User is awarded a badge for reviews of drinks from Guyana.', 'Country', 'Guyana', 1),
('Have Some Griot On The Side','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/84_Haiti_Have+Some+Griot+On+The+Side.png', 'User is awarded a badge for reviews of drinks from Haiti.', 'Country', 'Haiti', 1),
('At Copan Take A Left','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/85_Honduras_At+Copan+Take+A+Left.png', 'User is awarded a badge for reviews of drinks from Honduras.', 'Country', 'Honduras', 1),
('Lan Kwai Fong Hopping','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/86_Hong+Kong_Lan+Kwai+Fong+Hopping.png', 'User is awarded a badge for reviews of drinks from Hong Kong.', 'Country', 'Hong Kong', 1),
('Budapest Bound','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/87_Hungary_Budapest+Bound.png', 'User is awarded a badge for reviews of drinks from Hungary.', 'Country', 'Hungary', 1),
('Northern Light Chasers','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/88_Iceland_Northern+Light+Chasers.png', 'User is awarded a badge for reviews of drinks from Iceland.', 'Country', 'Iceland', 1),
('Sitar Superstar','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/89_India_Sitar+Superstar.png', 'User is awarded a badge for reviews of drinks from India.', 'Country', 'India', 1),
('Cheers To The Gaucho','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/9_Argentina_Cheers+To+The+Gaucho.png', 'User is awarded a badge for reviews of drinks from Argentina.', 'Country', 'Argentina', 1),
('Sumatra Sensibilities','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/90_Indonesia_Sumatra+Sensibilities.png', 'User is awarded a badge for reviews of drinks from Indonesia.', 'Country', 'Indonesia', 1),
('Footsteps Through Persepolis','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/91_Iran_Footsteps+Through+Persepolis+(2).png', 'User is awarded a badge for reviews of drinks from Iran.', 'Country', 'Iran', 1),
('Daydreaming Of Babylon Glory','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/92_Iraq_Daydreaming+Of+Babylon+Glory.png', 'User is awarded a badge for reviews of drinks from Iraq.', 'Country', 'Iraq', 1),
('Shamrock Til'' You Make It','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/93_Ireland_Shamrock+Til_+You+Make+It.png', 'User is awarded a badge for reviews of drinks from Ireland.', 'Country', 'Ireland', 1),
('Racing Through The TT','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/94_Isle+of+Man_Racing+Through+The+TT.png', 'User is awarded a badge for reviews of drinks from Isle.', 'Country', 'Isle', 1),
('You''re the Falafel to My Pita','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/95_Israel_You%E2%80%99re+the+Falafel+to+My+Pita.png', 'User is awarded a badge for reviews of drinks from Israel.', 'Country', 'Israel', 1),
('Just Roman Around','https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/96_Italy_Just+Roman+Around_Iraq_Daydreaming+Of+Babylon+Glory.png', 'User is awarded a badge for reviews of drinks from Italy.', 'Country', 'Italy', 1),
('Run It Like Bolt', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/97_Jamaica_Run+It+Like+Bolt.png', 'User is awarded a badge for reviews of drinks from Jamaica.', 'Country', 'Jamaica', 1),
('Breakfast In Kyoto', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/98_Japan_Breakfast+In+Kyoto.png', 'User is awarded a badge for reviews of drinks from Japan.', 'Country', 'Japan', 1),
('A Cab Ride To La Corbiere', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Country+Badges/99_Jersey_A+Cab+Ride+To+La+Corbiere.png', 'User is awarded a badge for reviews of drinks from Jersey.', 'Country', 'Jersey', 1);

-- ========= Seed Category Badges =========
-- Drink Type badges
INSERT INTO "badges" ("badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity", "badgeLevel") VALUES
-- Main Drink Types
('Whisky Explorer', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/1+Whisky+Explorer.png', 'For all reviews under the Drink Type Whisky.', 'DrinkType', 'Whisky', 1),
('El Tequila Supremo', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/5+El+Tequila+Supremo.png', 'For all reviews under the Drink Type Tequila.', 'DrinkType', 'Tequila', 1),
('A-Gave It All', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/6+A-gave-it+All!.png', 'For all reviews under the Drink Type Mezcal.', 'DrinkType', 'Mezcal', 1),
('Botanical Gin-ius!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/7+Botanical+Gin-ius!.png', 'For all reviews under the Drink Type Gin.', 'DrinkType', 'Gin', 1),
('Rumaniac', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/8+Rumaniac.png', 'For all reviews under the Drink Type Rum.', 'DrinkType', 'Rum', 1),
('Hop Head', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/9+Hop+Head.png', 'For all reviews under the Drink Type Beer.', 'DrinkType', 'Beer', 1),
('Sho-chu Love Shochu', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/21+Sho-chu+Love+Shochu.png', 'For all reviews under the Drink Type Shochu.', 'DrinkType', 'Shochu', 1),
('The Rice Of The Party', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/22+The+Rice+of+The+Party.png', 'For all reviews under the Drink Type Sake.', 'DrinkType', 'Sake', 1),
('Grape Expectations', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/26+Grape+Expectations.png', 'For all reviews under the Drink Type Wine.', 'DrinkType', 'Wine', 1),
('All Fruit Can Be Distilled, I''ll Prove It', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/34+All+Fruit+Can+Be+Distilled%2C+I_ll+Prove+It.png', 'For all reviews under the Drink Type Brandy.', 'DrinkType', 'Brandy', 1),
('Chasing The Dragon', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/39+Chasing+the+Dragon.png', 'For all reviews under the Drink Type Baijiu.', 'DrinkType', 'Baijiu', 1),
('Vodka Makes Everything Better', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/40+Vodka+Makes+Everything+Better.png', 'For all reviews under the Drink Type Vodka.', 'DrinkType', 'Vodka', 1),
('The MSG Of Every Drink', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/41+MSG+of+Every+Drink.png', 'For all reviews under the Drink Type Liqueurs & Bitters.', 'DrinkType', 'Liqueurs & Bitters', 1),
('Ume Me Happy', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/42+Ume+Me+Happy.png', 'For all reviews under the Drink Type Umeshu.', 'DrinkType', 'Umeshu', 1),
('Absinthe Makes The Heart Grow Fonder', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/43+Absinthe+Makes+The+Heart+Grow+Fonder.png', 'For all reviews under the Drink Type Absinthe.', 'DrinkType', 'Absinthe', 1),
('I''ll Have A-rrack Of That', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/44+I_ll+Have+A-rrack+Of+That.png', 'For all reviews under the Drink Type Arrack.', 'DrinkType', 'Arrack', 1),
('Who Knew Asparagus Tasted This Good', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/45+Who+Knew+Asparagus+Tasted+This+Good.png', 'For all reviews under the Drink Type Sotol.', 'DrinkType', 'Sotol', 1),
('Seoul Searching…', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/46+Seoul+Searching%E2%80%A6.png', 'For all reviews under the Drink Type Soju and Drink Type Makgeolli.', 'DrinkType', 'Rice + (Soju, etc.)', 1),
('Sips & Giggles', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/47+Sips+%26+Giggles.png', 'For all reviews under the Drink Type Cocktails.', 'DrinkType', 'Cocktails', 1);

-- Drink Category badges
INSERT INTO "badges" ("badgeName", "badgePhoto", "badgeDesc", "badgeType", "relatedEntity", "badgeLevel") VALUES
-- Whisky Categories
('Master of Malt', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/2+Master+of+Malt.png', 'For all reviews under the Drink Category Single Malt (Whisky).', 'Category', 'Single Malt', 1),
('Bourbon Baron', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/3+Bourbon+Baron.png', 'For all reviews under the Drink Category Bourbon (Whisky).', 'Category', 'Bourbon', 1),
('Symphony Harmonic', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/4+Symphony+Harmonic.png', 'For all reviews under the Drink Category Blended Whisky (Whisky).', 'Category', 'Blended', 1),

-- Beer Categories
('Ale-ficionado', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/10+Ale-ficionado.png', 'For all reviews under the Drink Category Ale (Beer).', 'Category', 'Ale', 1),
('Straight Outta The Abbey / One Hoppy Monk', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/11+One+Hoppy+Monk.png', 'For all reviews under the Drink Category Belgian Style (Beer).', 'Category', 'Belgian Style', 1),
('Lager Legend', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/12+Lager+Legend.png', 'For all reviews under the Drink Category Lager (Beer).', 'Category', 'Lager', 1),
('Orchard Oracle', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/13+Orchard+Oracle.png', 'For all reviews under the Drink Category Cider (Beer).', 'Category', 'Cider', 1),
('Brauhaus Regular', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/14+Bauhaus+Regular.png', 'For all reviews under the Drink Category German Style (Beer).', 'Category', 'German Style', 1),
('Hop Whisperer', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/15+Hop+Whisperer.png', 'For all reviews under the Drink Category IPA (Beer).', 'Category', 'IPA', 1),
('Mead Medici', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/16+Mead+Medici.png', 'For all reviews under the Drink Category Mead (Beer).', 'Category', 'Mead', 1),
('Into The Haze', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/17+Into+the+Haze.png', 'For all reviews under the Drink Category Hazy Ale (Beer).', 'Category', 'Hazy Ale', 1),
('Into The Abyss', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/18+Into+the+Abyss.png', 'For all reviews under the Drink Category Stout (Beer).', 'Category', 'Stout', 1),
('Pucker Me Up', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/19+Pucker+Me+Up.png', 'For all reviews under the Drink Category Sour (Beer).', 'Category', 'Sour', 1),
('Wheat Wizard', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/20+Wheat+Wizard.png', 'For all reviews under the Drink Category Wheat Beer (Beer).', 'Category', 'Wheat Beer', 1),

-- Sake Categories
('#NoFilter', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/23+NoFilter.png', 'For all reviews under the Drink Category Junmai (Sake).', 'Category', 'Junmai', 1),
('Rice Me Up!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/24+Rice+Me+Up!.png', 'For all reviews under the Drink Category Doburoku (Sake).', 'Category', 'Doburoku', 1),
('Renaissance Of Rice', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/25+Renaisance+of+Rice.png', 'For all reviews under the Drink Category Craft Sake (Sake).', 'Category', 'Craft Sake', 1),

-- Wine Categories
('Red-dy, Set, Grape!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/27+-+Red-dy%2C+Set%2C+Grape!.png', 'For all reviews under the Drink Category Red Wine (Wine).', 'Category', 'Red Wine', 1),
('All White Party', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/28+All+White+Party.png', 'For all reviews under the Drink Category White Wine (Wine).', 'Category', 'White Wine', 1),
('Give Me That Skin Contact', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/29+Give+Me+That+Skin+Contact.png', 'For all reviews under the Drink Category Orange Wine (Wine).', 'Category', 'Orange Wine', 1),
('You Had Me At Rose', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/30+You+Had+Me+At+Rose.png', 'For all reviews under the Drink Category Rose (Wine).', 'Category', 'Rose', 1),
('Fizz Me Up', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/31+Fizz+Me+Up.png', 'For all reviews under the Drink Category Sparkling (Wine).', 'Category', 'Sparkling', 1),
('Keep Calm And Fortify', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/32+Keep+Calm+and+Fortify.png', 'For all reviews under the Drink Category Fortified (Wine).', 'Category', 'Fortified', 1),
('Au Natural All Day', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/33+Au+Natural+All+Day.png', 'For all reviews under the Drink Category Natural (Wine).', 'Category', 'Natural', 1),

-- Brandy Categories
('Cognac Like Its 1900', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/35+Cognac+Is+Cool+Again.png', 'For all reviews under the Drink Category Cognac (Brandy).', 'Category', 'Cognac', 1),
('Armagnac For It!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/36+Armagnac+For+It!.png', 'For all reviews under the Drink Category Armagnac (Brandy).', 'Category', 'Armagnac', 1),
('How Do You Like Them Apples', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/37+How+Do+You+Like+Them+Apples.png', 'For all reviews under the Drink Category Calvados (Brandy).', 'Category', 'Calvados', 1),
('Grappa Hold Of This', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/38+Grappa+Hold+Of+This.png', 'For all reviews under the Drink Category Grappa (Brandy).', 'Category', 'Grappa', 1),

-- Cocktails Categories
('You''re Da Pome!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/48+You_re+Da+Pome.png', 'For all reviews under the Drink Category Beer- And Cider-Based Mixed Drinks (Cocktails).', 'Category', 'Beer- And Cider-Based Mixed Drinks', 1),
('You Can''t Play Spin The Bottle Here', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/49+You+Can_t+Play+Spin+the+Bottle+Here.png', 'For all reviews under the Drink Category Bottled Cocktails (Cocktails).', 'Category', 'Bottled Cocktails', 1),
('Champagne Supernova On Repeat', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/50+Champagne+Supernova+on+Repeat.png', 'For all reviews under the Drink Category Champagne Cocktails (Cocktails).', 'Category', 'Champagne Cocktails', 1),
('Fruits Of Your Labour', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/51+Fruits+of+Your+Labour.png', 'For all reviews under the Drink Category Cobblers (Cocktails).', 'Category', 'Cobblers', 1),
('Two''s A Crowd, Three''s A Party', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/52+Two_s+A+Crowd%2C+Three_s+A+Party.png', 'For all reviews under the Drink Category Duos and Trios (Cocktails).', 'Category', 'Duos and Trios', 1),
('From Paris To Milan', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/53+From+Paris+to+Lake+Como.png', 'For all reviews under the Drink Category French-Italian Drinks (Cocktails).', 'Category', 'French-Italian Drinks', 1),
('Let It Go, Let It Go, Can''t Hold It Back Anymore', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/54+Drink+Category_Let+It+Go%2C+Let+It+Go%2C+Can_t+Hold+It+Back+Anymore.png', 'For all reviews under the Drink Category Frozen Drinks (Cocktails).', 'Category', 'Frozen Drinks', 1),
('So-da-licious!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/55+-+Sodalicious.png', 'For all reviews under the Drink Category Highballs (Cocktails).', 'Category', 'Highballs', 1),
('Turning Up The Heat', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/56+Turning+Up+The+Heat.png', 'For all reviews under the Drink Category Hot Drinks (Cocktails).', 'Category', 'Hot Drinks', 1),
('Running For The Roses', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/57+Running+for+the+Roses.png', 'For all reviews under the Drink Category Juleps (Cocktails).', 'Category', 'Juleps', 1),
('The Italian Job', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/58+The+Italian+Job.png', 'For all reviews under the Drink Category Milanese Drinks (Cocktails).', 'Category', 'Milanese Drinks', 1),
('Could You Be Any Clearer', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/59+Could+You+Be+Any+Clearer.png', 'For all reviews under the Drink Category Muddle Drinks (Cocktails).', 'Category', 'Muddle Drinks', 1),
('It''s The Pousse In Boots!', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/60+It_s+The+Pousse+In+Boots!.png', 'For all reviews under the Drink Category Pousse-Cafes (Cocktails).', 'Category', 'Pousse-Cafes', 1),
('Throwin Hands', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/61+Throwin+Hands.png', 'For all reviews under the Drink Category Punches (Cocktails).', 'Category', 'Punches', 1),
('Ain''t No Whipper Snapper', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/62+Ain_t+No+Whipper+Snapper.png', 'For all reviews under the Drink Category Snappers (Cocktails).', 'Category', 'Snappers', 1),
('Dropping Acid / Captain pHantastic', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/63+Captain+pHantastic.png', 'For all reviews under the Drink Category Sours (Cocktails).', 'Category', 'Sours', 1),
('Tropic Thunder', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/64++-Tropic+Thunder.png', 'For all reviews under the Drink Category Tropical Drinks (Cocktails).', 'Category', 'Tropical Drinks', 1),
('They Say You Miss 100% Of The Shots You Don’t Take', 'https://drinkx-badges.s3.ap-southeast-1.amazonaws.com/Images+of+Drink+Type+-+Category+Badges/65+They+Say+You+Miss+100_+Of+the+Shots+You+Don_t+Take.png', 'For all reviews under the Drink Category Shots (Cocktails).', 'Category', 'Shots', 1);

INSERT INTO "clubs"(
    "clubName", "clubDesc", "isInviteOnly", "clubLink", "clubBanner", "dateCreated", "totalMembers", "createdByID", "createdByType")
VALUES
    ('Beer Enthusiasts', 'A club for fans of craft beers and brewing techniques', false, 'www.beerclub.com', '', '2024-10-29 19:00:31.403', 12, 1, 'user'),
    ('Wine Connoisseurs', 'Explore the world of fine wines, tastings, and pairings', true, 'www.wineclub.com', '', '2024-10-30 20:10:31.403', 2, 1, 'user'),
    ('Scotch Aficionados', 'Scotch lovers unite! Share and learn about premium scotches', false, 'www.scotchclub.com', '', '2024-11-01 15:25:31.403', 1, 1, 'producer'),
    ('Rum Admirers', 'A community for those who enjoy classic and modern rums', false, 'www.rumclub.com', '', '2024-11-03 17:35:31.403', 1, 1, 'venue'),
    ('Whisky Women', 'Empowering women to explore and enjoy whisky', true, 'www.whiskywomen.com', '', '2024-11-05 14:40:31.403', 1, 1, 'user'),
    ('Tequila Tribe', 'Dive into the rich flavors and traditions of tequila', false, 'www.tequilatribe.com', '', '2024-11-07 16:20:31.403', 1, 1, 'user'),
    ('Cocktail Creators', 'For mixologists and cocktail enthusiasts of all levels', true, 'www.cocktailclub.com', '', '2024-11-10 13:15:31.403', 1, 1, 'user'),
    ('Brandy Lovers', 'Discover and celebrate the elegance of brandy', false, 'www.brandyclub.com', '', '2024-11-12 12:30:31.403', 1, 1, 'user'),
    ('Gin Explorers', 'A group for gin enthusiasts and curious tasters', false, 'www.ginclub.com', '', '2024-11-15 14:50:31.403', 1, 1, 'user'),
    ('Spirit Collectors', 'A community for collectors of unique and rare spirits', true, 'www.spiritcollectors.com', '', '2024-12-13 18:10:31.403', 1, 5, 'user'),
    ('Highball Society', 'The perfect club for highball cocktail lovers', false, 'www.highballsociety.com', '', '2024-12-15 15:25:31.403', 1, 6, 'user'),
    ('Port & Sherry Lovers', 'Explore the depths of port and sherry flavors', true, 'www.portsherryclub.com', '', '2024-12-17 12:35:31.403', 1, 7, 'user'),
    ('Absinthe Advocates', 'A mysterious journey into absinthe culture and history', false, 'www.absintheclub.com', '', '2024-12-20 11:45:31.403', 1, 8, 'user'),
    ('Malt Masters', 'Dive deep into the intricacies of malt beverages', false, 'www.maltmasters.com', '', '2024-12-22 10:20:31.403', 1, 9, 'user'),
    ('Mocktail Makers', 'For those who enjoy crafting and drinking mocktails', false, 'www.mocktailclub.com', '', '2024-12-23 16:50:31.403', 1, 10, 'user'),
    ('Prosecco Pals', 'A bubbly club for prosecco lovers', false, 'www.proseccopals.com', '', '2024-12-24 15:15:31.403', 1, 11, 'user'),
    ('Sparkling Spirits', 'A vibrant community for lovers of sparkling beverages', true, 'www.sparklingspirits.com', '', '2024-12-25 14:10:31.403', 1, 12, 'user'),
    ('Whisky 101', 'Begin your whisky journey with us!', false, 'www.whisky101club.com', '', '2024-12-26 14:30:31.403', 1, 13, 'user'),
    ('Rum Rebels', 'Discover the rebellious side of rum culture', false, 'www.rumrebels.com', '', '2024-12-27 18:45:31.403', 1, 14, 'user'),
    ('Barrel Aged Fans', 'Uncover the flavors of barrel-aged drinks', true, 'www.barrelagedfans.com', '', '2024-12-28 19:20:31.403', 1, 15, 'user');


INSERT INTO "clubMembers"(
    "clubID", "userID", "userType", "joinDate", "isAdmin")
VALUES
    (1, 1, 'user', '2024-10-28 18:47:31.403', true),
    (1, 2, 'user', '2024-10-30 18:45:31.403', false),
    (1, 3, 'user', '2024-10-30 18:45:31.403', false),
    (1, 1, 'venue', '2024-10-30 18:53:31.403', false),
    (1, 1, 'producer', '2024-10-30 18:53:31.403', false),
    (1, 6, 'user', '2024-10-31 18:45:00.403', false),
    (1, 7, 'user', '2024-11-01 18:45:00.403', false),
    (1, 8, 'user', '2024-11-02 18:45:00.403', false),
    (1, 9, 'user', '2024-11-03 18:45:00.403', false),
    (1, 10, 'user', '2024-11-04 18:45:00.403', false),
    (1, 11, 'user', '2024-11-05 18:45:00.403', false),
    (1, 12, 'user', '2024-11-06 18:45:00.403', false),
    (1, 13, 'user', '2024-11-07 18:45:00.403', false),
    (1, 14, 'user', '2024-11-08 18:45:00.403', false),
    (1, 15, 'user', '2024-11-09 18:45:00.403', false),
    (2, 1, 'producer', '2024-10-28 18:55:31.403', true),
    (2, 5, 'user', '2024-10-28 18:55:31.403', true),
    (3, 1, 'user', '2024-10-30 18:45:31.403', true),
    (4, 1, 'venue', '2024-10-30 18:45:31.403', true),
    (5, 1, 'user', '2024-10-30 18:45:31.403', true),
    (6, 1, 'user', '2024-10-30 18:45:31.403', true),
    (7, 1, 'user', '2024-10-30 18:45:31.403', true),
    (8, 1, 'user', '2024-10-30 18:45:31.403', true),
    (9, 1, 'user', '2024-10-30 18:45:31.403', true),
    (10, 5, 'user', '2024-10-30 18:45:31.403', true),
    (11, 6, 'user', '2024-10-30 18:45:31.403', true),
    (12, 7, 'user', '2024-10-30 18:45:31.403', true),
    (13, 8, 'user', '2024-10-30 18:45:31.403', true),
    (14, 9, 'user', '2024-10-30 18:45:31.403', true),
    (15, 10, 'user', '2024-10-30 18:45:31.403', true),
    (16, 11, 'user', '2024-10-30 18:45:31.403', true),
    (17, 12, 'user', '2024-10-30 18:45:31.403', true),
    (18, 13, 'user', '2024-11-01 18:45:31.403', true),
    (19, 14, 'user', '2024-11-01 18:45:31.403', true),
    (20, 15, 'user', '2024-11-01 18:45:31.403', true);

INSERT INTO "clubInvites"(
    "clubID", "inviteeID", "inviteeUserType", "inviterID", "inviterUserType", "inviteDate")
VALUES
    (3, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403'),
    (4, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403'),
    (5, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403'),
    (6, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403'),
    (7, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403'),
    (8, 5, 'user', 1, 'user', '2024-10-30 18:45:31.403');

INSERT INTO "clubRequests"(
    "clubID", "userID", "userType", "requestDate")
VALUES
    (2, 3, 'user', '2024-10-31 18:45:31.403'),
    (2, 4, 'user', '2024-10-31 18:45:31.403');

INSERT INTO "clubPosts"(
    "clubID", "postDate", "postContent", "postPhotos", "posterID")
VALUES 
    (1, '2024-10-31 18:45:31.403', 'First taste of Yamazaki 12-Year\n\nSmooth with notes of honesy, dried fruits, vanilla, and a touch of spice. Enjoyed it neat - how do you prefer yours?\n\nAny recommendations for what I should try next?', '{}', 1),
    (1, '2024-10-31 19:00:31.403', 'Tried Glenfiddich 15-Year tonight. The sherry cask influence is incredible! Any other whiskies with a strong sherry profile I should try?', '{}', 2),
    (1, '2024-11-01 20:15:31.403', 'Enjoyed a dram of Ardbeg 10-Year. That smoky, peaty kick is unreal! Who else loves Islay whiskies?', '{}', 3),
    (1, '2024-11-02 18:30:31.403', 'Finally tried Maker’s Mark. Sweet, easy to drink, but I’m curious—how does it compare to Buffalo Trace?', '{}', 4),
    (1, '2024-11-03 19:45:31.403', 'Visited a local distillery today and tried their new single malt. A bit young but promising. Anyone else into independent distilleries?', '{}', 1),
    (1, '2024-11-04 21:00:31.403', 'Thinking of hosting a whisky tasting night. What’s the best way to organize the tasting order?', '{}', 2),
    (1, '2024-11-05 17:20:31.403', 'Macallan Double Cask 12-Year was on my list today. Smooth, sweet, and a perfect after-dinner drink. What’s your go-to dessert whisky?', '{}', 3),
    (1, '2024-11-06 19:10:31.403', 'Tried Laphroaig Quarter Cask. It’s bold, smoky, and unforgettable. What’s the best food pairing for such a peaty whisky?', '{}', 4),
    (1, '2024-11-07 20:50:31.403', 'Experimented with a whisky sour using Woodford Reserve. Turned out great! Do you prefer your whisky straight or in cocktails?', '{}', 1),
    (1, '2024-11-08 18:25:31.403', 'Had my first taste of Highland Park 18-Year. Truly balanced with honey, peat, and spice. Is the 21-Year worth the splurge?', '{}', 2),
    (1, '2024-11-09 19:30:31.403', 'For beginners: Glenlivet 12-Year is a great start. What would you recommend as a next step up?', '{}', 3),
    (1, '2024-11-10 20:45:31.403', 'Attended a whisky festival today! Tried so many new brands. Who else loves whisky events?', '{}', 4),
    (1, '2024-11-11 18:15:31.403', 'Balvenie Caribbean Cask 14-Year is so unique. The rum cask finish adds a sweet twist. What are your favorite cask finishes?', '{}', 1),
    (1, '2024-11-12 19:40:31.403', 'Just opened a bottle of Bunnahabhain 12-Year. It’s unpeated but still full of character. A great alternative to Islay smoke.', '{}', 2),
    (1, '2024-11-13 20:10:31.403', 'Who’s tried Japanese whiskies like Hibiki or Nikka? I’m amazed at how refined they are!', '{}', 3),
    (1, '2024-11-14 17:45:31.403', 'Eagle Rare 10-Year is my pick for the night. Great balance of caramel, vanilla, and oak. What’s your favorite bourbon?', '{}', 4),
    (1, '2024-11-15 19:50:31.403', 'Tried a whisky-infused chocolate today. It was divine! Anyone else into whisky pairings?', '{}', 1),
    (1, '2024-11-16 21:15:31.403', 'Lagavulin 16-Year is perfection in a bottle. Smoky, rich, and complex. Can’t wait to try the 12-Year soon.', '{}', 2),
    (1, '2024-11-17 18:30:31.403', 'Sampled Glenkinchie 12-Year. A very light and floral Lowland whisky. Perfect for a sunny day.', '{}', 3),
    (1, '2024-11-18 19:25:31.403', 'Anyone else a fan of blended whiskies? I just had Johnnie Walker Green Label, and it’s fantastic.', '{}', 4),
    (1, '2024-11-19 20:45:31.403', 'Exploring rye whiskies lately. Had Knob Creek Rye tonight, and it’s spicy and bold! Any other ryes to recommend?', '{}', 1),
    (1, '2024-11-20 21:30:31.403', 'Whisky fact: Did you know Scotch legally needs to be aged in oak barrels for at least 3 years? Learned this at a tour!', '{}', 2),
    (1, '2024-11-21 18:20:31.403', 'Opened a Glen Grant 10-Year. Light, fruity, and perfect for casual sipping. What’s your everyday whisky?', '{}', 3),
    (1, '2024-11-22 19:15:31.403', 'Received a bottle of Dalmore 12-Year as a gift. It’s elegant and rich. Anyone tried the King Alexander III?', '{}', 4),
    (1, '2024-11-23 20:40:31.403', 'Experimented with whisky and coffee tonight. A splash of Jameson made it amazing. What’s your favorite whisky-based drink?', '{}', 3),
    (1, '2024-11-24 21:50:31.403', 'Visited Scotland last year and toured Glenmorangie. Their 18-Year is unforgettable. Who else has done a distillery tour?', '{}', 1),
    (1, '2024-11-25 18:35:31.403', 'Decided to try something new—peated Irish whisky! Connemara was a pleasant surprise.', '{}', 2),
    (1, '2024-11-26 19:20:31.403', 'Found a local store selling rare whiskies. Picked up a Springbank 15-Year. Can’t wait to try it!', '{}', 3),
    (1, '2024-11-27 20:55:31.403', 'Looking for recommendations: What’s a good budget-friendly whisky for everyday sipping?', '{}', 1),
    (1, '2024-11-28 21:45:31.403', 'Whisky trivia: Did you know that bourbon must be made in the U.S. and use at least 51% corn? Cheers to learning!', '{}', 2),
    (1, '2024-11-29 18:25:31.403', 'GlenDronach 12-Year is a hidden gem. Rich, sherry-forward, and affordable. Highly recommend it!', '{"https://m.media-amazon.com/images/I/710obA9RM7L._AC_UF1000,1000_QL80_.jpg", "https://maltwineasia.com/wp-content/uploads/2024/08/The-Glendronach-Original-12-Years-New.jpg", "https://maltwineasia.com/wp-content/uploads/2024/08/The-Glendronach-Original-12-Years-New-Banner-1300x650.jpg"}', 3);

INSERT INTO "clubPostsLikes"(
    "clubID", "postID", "memberID")
VALUES
    (1, 1, 2),
    (1, 1, 3);

INSERT INTO "clubPostComments"(
    "postID", "commentDate", "commentContent", "commenterID")
VALUES
    (1, '2024-11-01 18:45:31.403', 'I usually enjoy it neat as well. Sometimes I add a drop or 2 of water to open up the flavors even more.\n\nFor your next try, I''d recommend Hakushu 12 if you want something lighter and herbal.', 2),
    (1, '2024-11-01 19:00:31.403', 'I always go neat with Yamazaki! If you''re into Japanese whisky, try Nikka From The Barrel—it''s incredible.', 3),
    (1, '2024-11-01 19:10:31.403', 'Adding a splash of water can really open up those fruity notes. Hakushu 12 is a great next step!', 1),
    (1, '2024-11-01 19:20:31.403', 'I like Yamazaki with a single large ice cube—keeps it cool without diluting too fast. For your next try, maybe go for Hibiki Harmony.', 2),
    (1, '2024-11-01 19:30:31.403', 'Yamazaki 12 is a classic! Try Glenlivet 18 for something equally smooth but a bit more robust.', 3),
    (1, '2024-11-01 19:40:31.403', 'Neat is the way to go! If you enjoy this, you might like Balvenie DoubleWood 12.', 1),
    (1, '2024-11-01 19:50:31.403', 'I prefer mine with just a couple of drops of water to release the aromas. You should try Kavalan Solist Sherry Cask next.', 2),
    (1, '2024-11-01 20:00:31.403', 'I usually go for it neat as well, but pairing it with dark chocolate really enhances the flavors.', 3),
    (1, '2024-11-01 20:10:31.403', 'Try Glenmorangie Signet if you''re looking for something bold and rich. It’s one of my favorites!', 1),
    (1, '2024-11-01 20:20:31.403', 'I''ve heard adding a bit of chilled green tea to Yamazaki is popular in Japan. Ever tried that?', 2),
    (1, '2024-11-01 20:30:31.403', 'I love Yamazaki! I think the Nikka Yoichi 10-Year would be a great follow-up for something smokier.', 3),
    (1, '2024-11-01 20:40:31.403', 'Neat or on the rocks, Yamazaki never disappoints. Next on your list should be Dalmore 15.', 1),
    (1, '2024-11-01 20:50:31.403', 'I''d recommend trying Glenfiddich 18 for a similar smoothness with a bit more spice.', 2),
    (1, '2024-11-01 21:00:31.403', 'Adding a few drops of water always works for me. As for recommendations, try Suntory''s Toki—it''s lighter but still fantastic.', 3),
    (1, '2024-11-01 21:10:31.403', 'Yamazaki is best enjoyed neat! For your next try, GlenDronach 12 is an excellent sherried option.', 4),
    (1, '2024-11-01 21:20:31.403', 'I''ve found that Yamazaki pairs surprisingly well with a mild cigar. Ever tried pairing whisky with cigars?', 2),
    (1, '2024-11-01 21:30:31.403', 'I suggest experimenting with small sips after warming the glass in your hands. Also, try Macallan 12 next!', 3),
    (1, '2024-11-01 21:40:31.403', 'Neat is my go-to as well! If you’re looking for something a bit peaty, try Laphroaig Quarter Cask.', 1),
    (1, '2024-11-01 21:50:31.403', 'I love how Yamazaki evolves over time in the glass. For your next bottle, I''d recommend Oban 14.', 2),
    (1, '2024-11-01 22:00:31.403', 'Yamazaki is a solid choice! Next, consider trying Compass Box Hedonism for a unique experience.', 4),
    (1, '2024-11-01 22:10:31.403', 'I find that Yamazaki is perfect for slow evenings. Try Glenkinchie 12 next for something light and floral.', 1),
    (1, '2024-11-01 22:20:31.403', 'Adding a touch of honey really enhances the sweet notes for me. Next, give Aberlour A’bunadh a shot.', 2),
    (1, '2024-11-01 22:30:31.403', 'Yamazaki is a favorite of mine! If you like it, you might enjoy Auchentoshan Three Wood.', 3),
    (1, '2024-11-01 22:40:31.403', 'Drinking it neat really lets the complexity shine. I think Glenfarclas 15-Year could be your next favorite.', 1),
    (1, '2024-11-01 22:50:31.403', 'I’d suggest pairing it with a cheese platter—it''s amazing! Next, try Balblair 15-Year.', 2),
    (1, '2024-11-01 23:00:31.403', 'I love Yamazaki 12! If you’re feeling adventurous, go for Ardbeg An Oa—it''s very different but delightful.', 3),
    (1, '2024-11-01 23:10:31.403', 'Try a few sips while eating roasted almonds or dried fruits—it really complements the flavors.', 1),
    (1, '2024-11-01 23:20:31.403', 'Neat is the only way for Yamazaki. I''d suggest Highland Park 18-Year for your next exploration.', 1),
    (1, '2024-11-01 23:30:31.403', 'I always drink it neat, but on a hot day, a splash of soda water works well. Try Hibiki 17-Year next!', 2),
    (1, '2024-11-01 23:40:31.403', 'Yamazaki is best savored slowly. I think Redbreast 12-Year is a great one to explore next.', 3);

INSERT INTO "clubPostCommentsLikes"(
    "postID", "commentID", "memberID")
VALUES
    (1, 1, 3);

INSERT INTO "events"(
    "eventName", "eventDesc", "eventType", "eventStartDate", "eventEndDate", "eventStartTime", "eventEndTime", "eventLimit", "eventBanners", "ticketed", "paidEvent", "eventLocation", "paymentLink", "eventOwnerID", "eventOwnerType", "numAttendees", "createdDate") 
VALUES 
    ('Trivia Night', 'Test your knowledge in our weekly trivia night! Prizes for the top teams.', 'Online', '2025-06-05', '2025-06-05', '19:00:00', '22:00:00', 100, NULL, FALSE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', '', 1, 'venue', 0, '2025-05-01 18:45:31.403'),  
    ('Whiskey Appreciation Night', 'Explore the world of whiskey with guided tastings of premium selections.', 'Online', '2025-03-05', '2025-03-05', '19:00:00', '22:00:00', 100, '{"https://img.pikbest.com/templates/20210426/bg/602bf6957a0b2.png!w700wp", "https://png.pngtree.com/png-clipart/20210502/original/pngtree-classic-bar-whiskey-leading-poster-png-image_6264354.png", "https://www.chivas.com/wp-content/uploads/2022/06/citrus-old-fashioned-whisky-cocktail-promo-1.jpg"}', TRUE, TRUE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 1, 'venue', 10, '2025-02-01 18:45:31.403'),   
    ('Beer Pong Tournament', 'Compete with friends and other teams in our ultimate beer pong showdown.', 'Online', '2025-03-03', '2025-03-03', '18:00:00', '22:00:00', 100, NULL, FALSE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', '', 2, 'user', 7, '2025-02-05 18:45:31.403'),
    ('Wine Tasting Night', 'Savor an evening of fine wines paired with small bites and expert insights.', 'Location', '2025-03-10', '2025-03-10', '18:30:00', '21:00:00', 100, NULL, TRUE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 3, 'user', 4, '2025-02-12 18:45:31.403'),
    ('Rum Cocktail Masterclass', 'Learn to craft the perfect rum-based cocktails with our expert mixologists.', 'Location', '2025-03-18', '2025-03-18', '17:00:00', '19:00:00', 100, NULL, TRUE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 1, 'producer', 0, '2025-02-13 18:45:31.403'),
    ('Ladies Night - Margaritas Galore', 'Enjoy $5 margaritas and a free welcome drink for all ladies.', 'Location', '2025-06-10', '2025-06-10', '18:00:00', '23:00:00', 100, NULL, FALSE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', '', 1, 'venue', 0, '2025-05-02 18:45:31.403'),
    ('Bourbon & Blues Night', 'Pair smooth bourbons with soulful blues music in a cozy atmosphere.', 'Location', '2025-03-15', '2025-03-15', '20:00:00', '23:00:00', 100, NULL, TRUE, TRUE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 1, 'producer', 0, '2025-02-15 18:45:31.403'),  
    ('IPA Showcase', 'Discover unique IPAs from local breweries in this beer lover’s event.', 'Location', '2025-06-15', '2025-06-15', '17:00:00', '20:00:00', 100, NULL, FALSE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', '', 1, 'venue', 0, '2025-05-03 18:45:31.403'),
    ('Cocktail Night: Around the World', 'Travel the globe one sip at a time with cocktails inspired by international flavors.', 'Location', '2025-03-25', '2025-03-25', '19:00:00', '23:00:00', 100, NULL, TRUE, FALSE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 1, 'user', 0, '2025-02-17 18:45:31.403'),
    ('Cider Festival', 'Celebrate the best ciders with unlimited tastings and live music all day long.', 'Location', '2025-06-20', '2025-06-20', '14:00:00', '22:00:00', 100, NULL, TRUE, TRUE, '10 Jln Serene, #01-03 Serene Centre, Singapore 258748', 'https://www.google.com', 1, 'venue', 0, '2025-05-04 18:45:31.403');


INSERT INTO "eventAttendees"(
    "eventID", "eventDate", "eventStartTime", "userID", "attendeeType", "attendeeStatus")
VALUES
    (1, '2025-01-20', '19:00:00', 5, 'user', true),
    (2, '2025-03-05', '19:00:00', 1, 'user', true),
    (2, '2025-03-05', '19:00:00', 1, 'producer', true),
    (2, '2025-03-05', '19:00:00', 2, 'user', true),
    (2, '2025-03-05', '19:00:00', 3, 'user', true),
    (2, '2025-03-05', '19:00:00', 6, 'user', true),
    (2, '2025-03-05', '19:00:00', 7, 'user', true),
    (2, '2025-03-05', '19:00:00', 8, 'user', true),
    (2, '2025-03-05', '19:00:00', 9, 'user', true),
    (2, '2025-03-05', '19:00:00', 10, 'user', true),
    (2, '2025-03-05', '19:00:00', 11, 'user', true),
    (3, '2025-03-03', '18:00:00', 1, 'user', true),
    (3, '2025-03-03', '18:00:00', 2, 'user', true),
    (3, '2025-03-03', '18:00:00', 3, 'user', true),
    (3, '2025-03-03', '18:00:00', 4, 'user', true),
    (3, '2025-03-03', '18:00:00', 5, 'user', true),
    (3, '2025-03-03', '18:00:00', 6, 'user', true),
    (3, '2025-03-03', '18:00:00', 7, 'user', true),
    (4, '2025-03-10', '18:30:00', 1, 'user', true),
    (4, '2025-03-10', '18:30:00', 2, 'user', true),
    (4, '2025-03-10', '18:30:00', 3, 'user', true),
    (4, '2025-03-10', '18:30:00', 4, 'user', true);

-- ========= [NEW!] "associations" - ADDED BY SMU GROUP 3 =========
INSERT INTO "associations"( "subTag1", "subTag2")
VALUES
    ('Fruit Flowers', 'Tinned Fruit'),
    ('Fruit Flowers', 'Orchard Fruits'),
    ('Fruit Flowers', 'Stone Fruits'),
    ('Fruit Flowers', 'Green Fruits'),
    ('Fruit Flowers', 'Yellow Fruits'),
    ('Dried Fruits', 'Fruit Flowers'),
    ('Orchard Fruits', 'Tinned Fruit'),
    ('Tinned Fruit', 'Tropical Fruits'),
    ('Green Fruits', 'Tinned Fruit'),
    ('Tinned Fruit', 'Yellow Fruits'),
    ('Dried Fruits', 'Tinned Fruit'),
    ('Orchard Fruits', 'Stone Fruits'),
    ('Orchard Fruits', 'Tropical Fruits'),
    ('Green Fruits', 'Orchard Fruits'),
    ('Orchard Fruits', 'Yellow Fruits'),
    ('Orchard Fruits', 'Unripe Fruits'),
    ('Dried Fruits', 'Orchard Fruits'),
    ('Orchard Fruits', 'Vines'),
    ('Green Fruits', 'Stone Fruits'),
    ('Stone Fruits', 'Yellow Fruits'),
    ('Stone Fruits', 'Unripe Fruits'),
    ('Green Fruits', 'Tropical Fruits'),
    ('Tropical Fruits', 'Yellow Fruits'),
    ('Dried Fruits', 'Tropical Fruits'),
    ('Citrus', 'Green Fruits'),
    ('Green Fruits', 'Yellow Fruits'),
    ('Green Fruits', 'Unripe Fruits'),
    ('Dried Fruits', 'Green Fruits'),
    ('Green Fruits', 'Melons'),
    ('Green Fruits', 'Vines'),
    ('Citrus', 'Yellow Fruits'),
    ('Unripe Fruits', 'Yellow Fruits'),
    ('Dried Fruits', 'Yellow Fruits'),
    ('Melons', 'Yellow Fruits'),
    ('Vines', 'Yellow Fruits'),
    ('Dried Fruits', 'Vines'),
    ('Sweet Wine', 'Vines');

INSERT INTO "pointSystemRules" ("ruleName", "ruleDesc", "ruleCategory", "proofPoints")
 VALUES
     ('Max Points', 'Max Points', 'Others', 200),
     ('Simple Review (Text Only)', 'The bare minimum review. This is the base upon which more points can be earned for the same primary action', 'Primary', 5),
     ('Extensive Review', 'Fills up extended review component +Points on top of Simple Review (Text Only)', 'Secondary', 3),
     ('Image Attached To Review', 'Adds image to post +Points on top of Simple Review (Text Only)', 'Secondary', 2),
     ('Tags Location', 'Tags location to post +Points on top of Simple Review (Text Only)', 'Secondary', 2),
     ('Tags Friends', 'Tags friends to Review +Points on top of Simple Review (Text Only); Same points awarded regardless of how many friends tagged', 'Secondary', 2),
     ('Posts In Clubs', 'Creates a post in Clubs. Points awarded independent of any other event', 'Primary', 1),
     ('Upvote', 'When a review/comment/club post gets an upvote; awarded for each Upvote given', 'Secondary', 1),
     ('Downvote', 'When a review/comment/club post gets a downvote; deducted for each Downvote given', 'Secondary', -1),
     ('Comment', 'Makes a comment on a Review of Club Post; independent of any other event', 'Primary', 1),
     ('Invites Friends', 'Invites Friends to join Drink-x; awarded for each invite sent', 'Primary', 3),
     ('Adds New Drink Listing', 'Adds New Drink Listing, that has been successfully approved; awarded for each new drink listing approved', 'Primary', 3),
     ('Suggest Edit Drink Listing', 'For each Edit successfully approved', 'Primary', 2),
     ('Create Public Lists', 'For each public list created', 'Primary', 2),
     ('Submits Qns For Producers/Venues', 'For each question posted to a Producer/Venue', 'Primary', 1);
 
 
 INSERT INTO "pointsRecorder"("userID", "userType", "currentPoints")
 VALUES
     (1, 'user', 802),
     (2, 'user', 404),
     (3, 'user', 200),
     (4, 'user', 800),
     (5, 'user', 100),
     (6, 'user', 88),
     (7, 'user', 0),
     (8, 'user', 0),
     (9, 'user', 0),
     (10, 'user', 0),
     (11, 'user', 0),
     (12, 'user', 0),
     (13, 'user', 0),
     (14, 'user', 0),
     (15, 'user', 0),
     (16, 'user', 0),
     (17, 'user', 0),
     (18, 'user', 0),
     (19, 'user', 0),
     (20, 'user', 0);