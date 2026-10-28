from models import Location

# 18 campus buildings, kept in order by building ID (1 to 18).
# Search by ID (Binary Search) needs this list to stay in order.
campus_locations = [
    Location(1, "Main Gate", "Entrance"),
    Location(2, "Audio Visual Room", "Academic"),
    Location(3, "Salceda Building", "Academic"),
    Location(4, "Administration Building", "Academic"),
    Location(5, "Computing and Engineering Building", "Academic"),
    Location(6, "Center for Student Services (CSC) Building", "Administrative"),
    Location(7, "Registrar Office", "Administrative"),
    Location(8, "Automotive Building", "Technical"),
    Location(9, "Research and Development Management Office", "Administrative"),
    Location(10, "Physical Development Management Office", "Administrative"),
    Location(11, "Electronics and Electrical Building", "Technical"),
    Location(12, "Machine and Welding Shop", "Technical"),
    Location(13, "Gym", "Facility"),
    Location(14, "Technology and Entrepreneurship Building", "Academic"),
    Location(15, "Canteen", "Facility"),
    Location(16, "Dormitory", "Residential"),
    Location(17, "Food Lab", "Academic"),
    Location(18, "Nursing Department", "Academic"),
]

# Road points used by Route Planning.
# Points 1 to 18 are the buildings above. Points 19 to 28 are road
# junctions (places where roads meet). They are not buildings, so they
# are not in campus_locations, but routes pass through them.
# Taken from the road map in Mateo's original display_route.py.
TOTAL_POINTS = 28

# Each pair means: these two points are directly connected by a road.
connections = [
    (19, 12), # Junction (top west) - Machine and Welding Shop
    (12, 11), # Machine and Welding Shop - Electronics and Electrical Building
    (11, 10), # Electronics and Electrical Building - Physical Development Mgt. Office
    (10, 9),  # Physical Development Mgt. Office - R&D Management Office
    (9, 8),   # R&D Management Office - Automotive Building
    (8, 7),   # Automotive Building - Registrar Office
    (7, 27),  # Registrar Office - Junction (south west)
    (19, 20), # Junction (top west) - Junction (top middle)
    (20, 21), # Junction (top middle) - Junction (top east)
    (20, 14), # Junction (top middle) - Technology and Entrepreneurship Building
    (20, 22), # Junction (top middle) - Junction (upper middle)
    (22, 23), # Junction (upper middle) - Junction (center)
    (23, 25), # Junction (center) - Junction (lower middle)
    (25, 28), # Junction (lower middle) - Roundabout
    (22, 13), # Junction (upper middle) - Gym
    (22, 17), # Junction (upper middle) - Food Lab
    (23, 9),  # Junction (center) - R&D Management Office
    (23, 15), # Junction (center) - Canteen
    (23, 24), # Junction (center) - Junction (center east)
    (25, 5),  # Junction (lower middle) - Computing and Engineering Building
    (25, 6),  # Junction (lower middle) - CSC Building
    (21, 16), # Junction (top east) - Dormitory
    (21, 24), # Junction (top east) - Junction (center east)
    (24, 18), # Junction (center east) - Nursing Department
    (24, 26), # Junction (center east) - Junction (lower east)
    (26, 3),  # Junction (lower east) - Salceda Building
    (26, 28), # Junction (lower east) - Roundabout
    (27, 28), # Junction (south west) - Roundabout
    (28, 2),  # Roundabout - Audio Visual Room
    (28, 1),  # Roundabout - Main Gate
    (4, 8),   # Administration Building - Automotive Building
    (4, 25),  # Administration Building - Junction (lower middle)
]
