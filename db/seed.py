
USERS = [
    {
        "id": 1,
        "full_name": "Jesse Faden",
        "role_id": 1
    },{
        "id": 2,
        "full_name": "Zachariah Trench",
        "role_id": 5
    },{
        "id": 3,
        "full_name": "Emily Pope, Dr",
        "role_id": 3
    },{
        "id": 4,
        "full_name": "Jeremy Clarkson",
        "role_id": 2
    },{
        "id": 5,
        "full_name": "Helen Marshall",
        "role_id": 5
    },{
        "id": 6,
        "full_name": "Dale Cooper",
        "role_id": 4
    }
]

BADGES = [
    {
        "id": 1,
        "user_id": 1
    },{
        "id": 2,
        "user_id": 2
    },{
        "id": 3,
        "user_id": 3
    },{
        "id": 4,
        "user_id": None
    },{
        "id": 5,
        "user_id": 4
    },{
        "id": 6,
        "user_id": 5
    },{
        "id": 7,
        "user_id": 6
    },{
        "id": 8,
        "user_id": None
    }
]

ROLES = [
    {
        "id": 1,
        "label": "Director",
        "night_availability": False
    },{
        "id": 2,
        "label": "Janitor",
        "night_availability": False
    },{
        "id": 3,
        "label": "Head of Research",
        "night_availability": True
    },{
        "id": 4,
        "label": "Security Chief",
        "night_availability": True
    },{
        "id": 5,
        "label": "Visitor",
        "night_availability": False
    },
]

SECTORS = [
    {
        "id": 1,
        "label": "Executive sector",
        "role_id": 1
    },{
        "id": 2,
        "label": "Maintenance sector",
        "role_id": 2
    },{
        "id": 3,
        "label": "Research sector",
        "role_id": 3
    },{
        "id": 4,
        "label": "Containment sector",
        "role_id": 4
    },
]

BADGE_READERS = [
    {
        "id": 1,
        "label": "Nostalgic Cafe",
        "sector_id": 1
    },{
        "id": 2,
        "label": "Board room",
        "sector_id": 1
    },{
        "id": 3,
        "label": "Director office",
        "sector_id": 1
    },{
        "id": 4,
        "label": "Ventilation",
        "sector_id": 2
    },{
        "id": 5,
        "label": "Quarry",
        "sector_id": 2
    },{
        "id": 6,
        "label": "Field training",
        "sector_id": 2
    },{
        "id": 7,
        "label": "Parapsychology",
        "sector_id": 3
    },{
        "id": 8,
        "label": "HRA Lab",
        "sector_id": 3
    },{
        "id": 9,
        "label": "Ashtray Lab",
        "sector_id": 3
    },{
        "id": 10,
        "label": "Control room",
        "sector_id": 4
    },{
        "id": 11,
        "label": "Shelter",
        "sector_id": 4
    },{
        "id": 12,
        "label": "Security",
        "sector_id": 4
    },
]

BADGE_READERS_ROLES = [
    {
       "role_id": 1, #Director #Director
       "badge_reader_id": 1 #Nostalgic Cafe
    },
    {
       "role_id": 2, #Janitor
       "badge_reader_id": 1 #Nostalgic Cafe
    },{
       "role_id": 3, #Head of Research
       "badge_reader_id": 1 #Nostalgic Cafe
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 1 #Nostalgic Cafe
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 1 #Nostalgic Cafe
    },{
       "role_id": 1, #Director
       "badge_reader_id": 2 #Board Room
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 2 #Board Room
    },{
       "role_id": 1, #Director
       "badge_reader_id": 3 #Director office
    },{
       "role_id": 1, #Director
       "badge_reader_id": 4 #Ventilation
    },{
       "role_id": 2, #Janitor
       "badge_reader_id": 4 #Ventilation
    },{
       "role_id": 3, #Head of Research
       "badge_reader_id": 5 #Quarry
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 5 #Quarry
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 6 #Field training
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 6 #Field training
    },{
       "role_id": 1, #Director
       "badge_reader_id": 7 #Parapsychology
    },{
       "role_id": 3, #Head of Research
       "badge_reader_id": 7 #Parapsychology
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 7 #Parapsychology
    },{
       "role_id": 3, #Head of Research
       "badge_reader_id": 8 #HRA Lab
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 8 #HRA Lab
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 9 #Ashtray Lab
    },{
       "role_id": 1, #Director
       "badge_reader_id": 10 #Control room
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 10 #Control room
    },{
       "role_id": 2, #Janitor
       "badge_reader_id": 10 #Control room
    },{
       "role_id": 1, #Director
       "badge_reader_id": 11 #Shelter
    },{
       "role_id": 2, #Janitor
       "badge_reader_id": 11 #Shelter
    },{
       "role_id": 3, #Head of Research
       "badge_reader_id": 11 #Shelter
    },{
       "role_id": 4, #Security Chief
       "badge_reader_id": 11 #Shelter
    },{
       "role_id": 5, #Visitor
       "badge_reader_id": 12 #Security
    },{
       "role_id": 2, #Janitor
       "badge_reader_id": 12 #Security
    }
]

ACCESSES = [
    {
    "id": 1,
    "timestamp_in": "2023-11-12 04:27:52.058918",
    "timestamp_out": None,
    "badge_id": 6, #badge_id: 6 -> Helen Marshall - Visitor
    "badge_reader_id": 9 #id: 9 -> Ashtray Lab
    },{
    "id": 2,
    "timestamp_in": "2023-11-22 12:27:52.058918",
    "timestamp_out": "2023-11-22 14:47:52.058918",
    "badge_id": 1, # Jesse Faden
    "badge_reader_id": 1 # Nostalgic Cafe
    },{
    "id": 3,
    "timestamp_in": "2023-11-22 14:57:52.058918",
    "timestamp_out": "2023-11-23 03:47:52.058918",
    "badge_id": 1, # Jesse Faden
    "badge_reader_id": 3 # Director office
    },{
    "id": 4,
    "timestamp_in": "2023-11-23 08:27:52.058918",
    "timestamp_out": "2023-11-23 17:27:52.058918",
    "badge_id": 3, # Emily Pope, Dr
    "badge_reader_id": 7 # Parapsychology
    },{
    "id": 5,
    "timestamp_in": None, # user not authorized 
    "timestamp_out": None,
    "badge_id": 2, #badge_id: 2 -> Zachariah Trench - Visitor
    "badge_reader_id": 12 #id: 12 -> Security
    },{
    "id": 6,
    "timestamp_in": "2023-11-25 22:27:52.058918",
    "timestamp_out": "2023-11-26 12:33:52.058918",
    "badge_id": 7, #badge_id: 7 -> Dale Cooper - Security Chief
    "badge_reader_id": 10 #id: 10 -> Control room
    },{
    "id": 7,
    "timestamp_in": "2023-11-27 09:27:52.058918",
    "timestamp_out": None,
    "badge_id": 3, #badge_id: 3 -> Emily Pope, Dr - Head of Research
    "badge_reader_id": 5 #id: 5 -> Quarry
    },{
    "id": 8,
    "timestamp_in": "2023-11-27 07:01:52.058918",
    "timestamp_out": "2023-11-27 07:56:52.058918",
    "badge_id": 5, #badge_id: 5 -> Jeremy Clarkson - Janitor
    "badge_reader_id": 1 #id: 1 -> Nostalgic Cafe
    },{
    "id": 8,
    "timestamp_in": "2023-11-27 07:57:52.058918",
    "timestamp_out": None,
    "badge_id": 5, #badge_id: 5 -> Jeremy Clarkson - Janitor
    "badge_reader_id": 4 #id: 4 -> Ventilation
    }
]

WARNINGS = [
    {
       "id": 1,
       "code_name": "Polaris",
       "description": "High Concentration Resonance-base"
    },{
       "id": 2,
       "code_name": "Hedron",
       "description": "Mold Spores - deprecated in 03/23/87"
    },{
       "id": 3,
       "code_name": "The Hiss",
       "description": "Uncontrolled Loss"
    }
]

BADGE_READERS_WARNINGS = [
    {
       "warning_id": 1, # Polaris: High Concentration Resonance-base
       "badge_reader_id": 5 # Quarry
    },{
       "warning_id": 1, # Polaris: High Concentration Resonance-base
       "badge_reader_id": 9  # Ashtray Lab
    },{
       "warning_id": 2, # Hedron: Mold Spores - deprecated in 03/23/87
       "badge_reader_id": 1 # Nostalgic Cafe
    },{
       "warning_id": 2, # Hedron: Mold Spores - deprecated in 03/23/87
       "badge_reader_id": 11 # Shelter
    },{
       "warning_id": 3, # The Hiss: Uncontrolled Loss
       "badge_reader_id": 6 # Field training
    },{
       "warning_id": 3, # The Hiss: Uncontrolled Loss
       "badge_reader_id": 4 # Ventilation
    },{
       "warning_id": 3, # The Hiss: Uncontrolled Loss
       "badge_reader_id": 9  # Ashtray Lab
    },
]
