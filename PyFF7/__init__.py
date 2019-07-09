#!/usr/bin/env python3
'''
Global functions and classes
Niema Moshiri 2019
'''
BITS_PER_BYTE = 8
BYTES_TO_FORMAT = {1:'B', 2:'H', 4:'I'}
MAX_SIGNED_SHORT = 32767
MAX_UNSIGNED_SHORT = 65535
MAX_UNSIGNED_INT = 4294967295
NULL_BYTE = b'\x00'
NULL_STR = NULL_BYTE.decode()

# item database
ITEM_DB = {
    (0x00, 0): "Potion",
    (0x00, 1): "Bronze Bangle",
    (0x01, 0): "Hi-Potion",
    (0x01, 1): "Iron Bangle",
    (0x02, 0): "X-Potion",
    (0x02, 1): "Titan Bangle",
    (0x03, 0): "Ether",
    (0x03, 1): "Mythril Armlet",
    (0x04, 0): "Turbo Ether",
    (0x04, 1): "Carbon Bangle",
    (0x05, 0): "Elixir",
    (0x05, 1): "Silver Armlet",
    (0x06, 0): "Megalixir",
    (0x06, 1): "Gold Armlet",
    (0x07, 0): "Phoenix Down",
    (0x07, 1): "Diamond Bangle",
    (0x08, 0): "Antidote",
    (0x08, 1): "Crystal Bangle",
    (0x09, 0): "Soft",
    (0x09, 1): "Platinum Bangle",
    (0x0A, 0): "Maiden's Kiss",
    (0x0A, 1): "Rune Armlet",
    (0x0B, 0): "Cornucopia",
    (0x0B, 1): "Edincoat",
    (0x0C, 0): "Echo Screen",
    (0x0C, 1): "Wizard Bracelet",
    (0x0D, 0): "Hyper",
    (0x0D, 1): "Adaman Bangle",
    (0x0E, 0): "Tranquilizer",
    (0x0E, 1): "Gigas Armlet",
    (0x0F, 0): "Remedy",
    (0x0F, 1): "Imperial Guard",
    (0x10, 0): "Smoke Bomb",
    (0x10, 1): "Aegis Armlet",
    (0x11, 0): "Speed Drink",
    (0x11, 1): "Fourth Bracelet",
    (0x12, 0): "Hero Drink",
    (0x12, 1): "Warrior Bangle",
    (0x13, 0): "Vaccine",
    (0x13, 1): "Shinra Beta",
    (0x14, 0): "Grenade",
    (0x14, 1): "Shinra Alpha",
    (0x15, 0): "Shrapnel",
    (0x15, 1): "Four Slots",
    (0x16, 0): "Right arm",
    (0x16, 1): "Fire Armlet",
    (0x17, 0): "Hourglass",
    (0x17, 1): "Aurora Armlet",
    (0x18, 0): "Kiss of Death",
    (0x18, 1): "Bolt Armlet",
    (0x19, 0): "Spider Web",
    (0x19, 1): "Dragon Armlet",
    (0x1A, 0): "Dream Powder",
    (0x1A, 1): "Minerva Band",
    (0x1B, 0): "Mute Mask",
    (0x1B, 1): "Escort Guard",
    (0x1C, 0): "War Gong",
    (0x1C, 1): "Mystile",
    (0x1D, 0): "Loco weed",
    (0x1D, 1): "Ziedrich",
    (0x1E, 0): "Fire Fang",
    (0x1E, 1): "Precious Watch",
    (0x1F, 0): "Fire Veil",
    (0x1F, 1): "Chocobracelet",
    (0x20, 0): "Antarctic Wind",
    (0x20, 1): "Power Wrist",
    (0x21, 0): "Ice Crystal",
    (0x21, 1): "Protect Vest",
    (0x22, 0): "Bolt Plume",
    (0x22, 1): "Earring",
    (0x23, 0): "Swift Bolt",
    (0x23, 1): "Talisman",
    (0x24, 0): "Earth Drum",
    (0x24, 1): "Choco Feather",
    (0x25, 0): "Earth Mallet",
    (0x25, 1): "Amulet",
    (0x26, 0): "Deadly Waste",
    (0x26, 1): "Champion Belt",
    (0x27, 0): "M-Tentacles",
    (0x27, 1): "Poison Ring",
    (0x28, 0): "Stardust",
    (0x28, 1): "Touph Ring",
    (0x29, 0): "Vampire Fang",
    (0x29, 1): "Circlet",
    (0x2A, 0): "Ghost Hand",
    (0x2A, 1): "Star Pendant",
    (0x2B, 0): "Vagyrisk Claw",
    (0x2B, 1): "Silver Glasses",
    (0x2C, 0): "Light Curtain",
    (0x2C, 1): "Headband",
    (0x2D, 0): "Lunar Curtain",
    (0x2D, 1): "Fairy Ring",
    (0x2E, 0): "Mirror",
    (0x2E, 1): "Jem Ring",
    (0x2F, 0): "Holy Torch",
    (0x2F, 1): "White Cape",
    (0x30, 0): "Bird Wing",
    (0x30, 1): "Sprint Shoes",
    (0x31, 0): "Dragon Scales",
    (0x31, 1): "Peace Ring",
    (0x32, 0): "Impaler",
    (0x32, 1): "Ribbon",
    (0x33, 0): "Shrivel",
    (0x33, 1): "Fire Ring",
    (0x34, 0): "Eye drop",
    (0x34, 1): "Ice Ring",
    (0x35, 0): "Molotov",
    (0x35, 1): "Bolt Ring",
    (0x36, 0): "S-mine",
    (0x36, 1): "Tetra Elemental",
    (0x37, 0): "8inch Cannon",
    (0x37, 1): "Safety Bit",
    (0x38, 0): "Graviball",
    (0x38, 1): "Fury Ring",
    (0x39, 0): "T/S Bomb",
    (0x39, 1): "Curse Ring",
    (0x3A, 0): "Ink",
    (0x3A, 1): "Protect Ring",
    (0x3B, 0): "Dazers",
    (0x3B, 1): "Cat's Bell",
    (0x3C, 0): "Dragon Fang",
    (0x3C, 1): "Reflect Ring",
    (0x3D, 0): "Cauldron",
    (0x3D, 1): "Water Ring",
    (0x3E, 0): "Sylkis Greens",
    (0x3E, 1): "Sneak Glove",
    (0x3F, 0): "Reagan Greens",
    (0x3F, 1): "HypnoCrown",
    (0x40, 0): "Mimett Greens",
    (0x41, 0): "Curiel Greens",
    (0x42, 0): "Pahsana Greens",
    (0x43, 0): "Tantal Greens",
    (0x44, 0): "Krakka Greens",
    (0x45, 0): "Gysahl Greens",
    (0x46, 0): "Tent",
    (0x47, 0): "Power Source",
    (0x48, 0): "Guard Source",
    (0x49, 0): "Magic Source",
    (0x4A, 0): "Mind Source",
    (0x4B, 0): "Speed Source",
    (0x4C, 0): "Luck Source",
    (0x4D, 0): "Zeio Nut",
    (0x4E, 0): "Carob Nut",
    (0x4F, 0): "Porov Nut",
    (0x50, 0): "Pram Nut",
    (0x51, 0): "Lasan Nut",
    (0x52, 0): "Saraha Nut",
    (0x53, 0): "Luchile Nut",
    (0x54, 0): "Pepio Nut",
    (0x55, 0): "Battery",
    (0x56, 0): "Tissue",
    (0x57, 0): "Omnislash",
    (0x58, 0): "Catastrophe",
    (0x59, 0): "Final Heaven",
    (0x5A, 0): "Great Gospel",
    (0x5B, 0): "Cosmo Memory",
    (0x5C, 0): "All Creation",
    (0x5D, 0): "Chaos",
    (0x5E, 0): "Highwind",
    (0x5F, 0): "1/35 Soldier",
    (0x60, 0): "Super Sweeper",
    (0x61, 0): "Masamune Blade",
    (0x62, 0): "Save Crystal",
    (0x63, 0): "Combat Diary",
    (0x64, 0): "Autograph",
    (0x65, 0): "Gambler",
    (0x66, 0): "Desert Rose ",
    (0x67, 0): "Earth Harp",
    (0x68, 0): "Guide Book",
    (0x80, 0): "Buster Sword",
    (0x81, 0): "Mythril Saber",
    (0x82, 0): "Hardedge",
    (0x83, 0): "Butterfly Edge",
    (0x84, 0): "Enhance Sword",
    (0x85, 0): "Organics",
    (0x86, 0): "Crystal Sword",
    (0x87, 0): "Force Stealer",
    (0x88, 0): "Rune Blade",
    (0x89, 0): "Murasame",
    (0x8A, 0): "Nail Bat",
    (0x8B, 0): "Yoshiyuki",
    (0x8C, 0): "Apocalypse",
    (0x8D, 0): "Heaven's Cloud",
    (0x8E, 0): "Ragnarok",
    (0x8F, 0): "Ultima Weapon",
    (0x90, 0): "Leather Glove",
    (0x91, 0): "Metal Knuckle",
    (0x92, 0): "Mythril Claw",
    (0x93, 0): "Grand Glove",
    (0x94, 0): "Tiger Fang",
    (0x95, 0): "Diamond Knuckle",
    (0x96, 0): "Dragon Claw",
    (0x97, 0): "Crystal Glove",
    (0x98, 0): "Motor Drive",
    (0x99, 0): "Platinum Fist",
    (0x9A, 0): "Kaiser Knuckle",
    (0x9B, 0): "Work Glove",
    (0x9C, 0): "Powersoul",
    (0x9D, 0): "Master Fist",
    (0x9E, 0): "God's Hand",
    (0x9F, 0): "Premium Heart",
    (0xA0, 0): "Gatling Gun",
    (0xA1, 0): "Assault Gun",
    (0xA2, 0): "Cannon Ball",
    (0xA3, 0): "Atomic Scissorss",
    (0xA4, 0): "Heavy Vulcan",
    (0xA5, 0): "Chainsaw",
    (0xA6, 0): "Microlaser",
    (0xA7, 0): "A-M Cannon",
    (0xA8, 0): "W Machine Gun",
    (0xA9, 0): "Drill Arm",
    (0xAA, 0): "Solid Bazooka",
    (0xAB, 0): "Rocket Punch",
    (0xAC, 0): "Enemy Launcher",
    (0xAD, 0): "Pile Banger",
    (0xAE, 0): "Max Ray",
    (0xAF, 0): "Missing Score",
    (0xB0, 0): "Mythril Clip",
    (0xB1, 0): "Diamond Pin",
    (0xB2, 0): "Silver Barrette",
    (0xB3, 0): "Gold Barrette",
    (0xB4, 0): "Adaman Clip",
    (0xB5, 0): "Crystal Comb",
    (0xB6, 0): "Magic Comb",
    (0xB7, 0): "Plus Barrette",
    (0xB8, 0): "Centclip",
    (0xB9, 0): "Hairpin",
    (0xBA, 0): "Seraph Comb",
    (0xBB, 0): "Behimoth Horn",
    (0xBC, 0): "Spring Gun Clip",
    (0xBD, 0): "Limited Moon",
    (0xBE, 0): "Guard Stick",
    (0xBF, 0): "Mythril Rod",
    (0xC0, 0): "Full Metal Staff",
    (0xC1, 0): "Striking Staff",
    (0xC2, 0): "Prism Staff",
    (0xC3, 0): "Aurora Rod",
    (0xC4, 0): "Wizard Staff",
    (0xC5, 0): "Wizer Staff",
    (0xC6, 0): "Fairy Tale",
    (0xC7, 0): "Umbrella",
    (0xC8, 0): "Princess Guard",
    (0xC9, 0): "Spear",
    (0xCA, 0): "Slash Lance",
    (0xCB, 0): "Trident",
    (0xCC, 0): "Mast Ax",
    (0xCD, 0): "Partisan",
    (0xCE, 0): "Viper Halberd",
    (0xCF, 0): "Javelin",
    (0xD0, 0): "Grow Lance",
    (0xD1, 0): "Mop",
    (0xD2, 0): "Dragoon Lance",
    (0xD3, 0): "Scimitar",
    (0xDB, 0): "Hawkeye",
    (0xD4, 0): "Flayer",
    (0xD5, 0): "Spirit Lance",
    (0xD6, 0): "Venus Gospel",
    (0xD7, 0): "4-point Shuriken",
    (0xD8, 0): "Boomerang",
    (0xD9, 0): "Pinwheel",
    (0xDA, 0): "Razor Ring",
    (0xDC, 0): "Crystal Cross",
    (0xDD, 0): "Wind Slash",
    (0xDE, 0): "Twin Viper",
    (0xDF, 0): "Spiral Shuriken",
    (0xE0, 0): "Superball",
    (0xE1, 0): "Magic Shuriken",
    (0xE2, 0): "Rising Sun",
    (0xE3, 0): "Oritsuru",
    (0xE4, 0): "Conformer",
    (0xE5, 0): "Yellow M-phone",
    (0xE6, 0): "Green M-phone",
    (0xE7, 0): "Blue M-phone",
    (0xE8, 0): "Red M-phone",
    (0xE9, 0): "Crystal M-phone",
    (0xEA, 0): "White M-phone",
    (0xEB, 0): "Black M-phone",
    (0xEC, 0): "Silver M-phone",
    (0xED, 0): "Trumpet Shell",
    (0xEE, 0): "Gold M-phone",
    (0xEF, 0): "Battle Trumpet",
    (0xF0, 0): "Starlight Phone",
    (0xF1, 0): "HP Shout",
    (0xF2, 0): "Quicksilver",
    (0xF3, 0): "Shotgun",
    (0xF4, 0): "Shortbarrel",
    (0xF5, 0): "Lariat",
    (0xF6, 0): "Winchester",
    (0xF7, 0): "Peacemaker",
    (0xF8, 0): "Buntline",
    (0xF9, 0): "Long Barrel R",
    (0xFA, 0): "Silver Rifle",
    (0xFB, 0): "Sniper CR",
    (0xFC, 0): "Supershot ST",
    (0xFD, 0): "Outsider",
    (0xFE, 0): "Death Penalty",
    (0xFF, 0): "Masamune",
}
