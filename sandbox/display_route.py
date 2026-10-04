import heapq

# ---------------------------------------------------------------------------
# 1. ALL NODES: 18 real buildings (sele  ctable) + synthetic road junctions
#    (not selectable, only used to shape the route realistically)
# ---------------------------------------------------------------------------
NODES = {
    # --- Buildings (selectable in the menu) ---
    "MAIN_GATE":       {"name": "Main Gate",                                              "x": 434, "y": 1287, "building": True},
    "AUDIO_VISUAL":    {"name": "Audio Visual Room",                                      "x": 389, "y": 916,  "building": True},
    "SALCEDA":         {"name": "Salceda Building",                                       "x": 491, "y": 867,  "building": True},
    "ADMIN":           {"name": "Administration Building",                                "x": 254, "y": 809,  "building": True},
    "CES":             {"name": "Center for Computing and Engineering",                   "x": 255, "y": 692,  "building": True},
    "CSC":             {"name": "Center for Student Services (CSC)",                      "x": 424, "y": 685,  "building": True},
    "REGISTRAR":       {"name": "Registrar Office",                                       "x": 109, "y": 900,  "building": True},
    "AUTOMOTIVE":      {"name": "Automotive Building",                                    "x": 114, "y": 777,  "building": True},
    "RDEPO":           {"name": "Research and Development Extension Production Office",   "x": 117, "y": 676,  "building": True},
    "PDMO":            {"name": "Physical Development Management Office",                 "x": 117, "y": 627,  "building": True},
    "SABIDO":          {"name": "Sabido (Electronics and Electrical Building)",           "x": 117, "y": 513,  "building": True},
    "MACHINE_WELDING": {"name": "Machine and Welding Shop Building",                      "x": 128, "y": 382,  "building": True},
    "GYM":             {"name": "Gym",                                                    "x": 267, "y": 480,  "building": True},
    "TECH_ENTREP":     {"name": "Technology and Entrepreneurship Building",               "x": 301, "y": 317,  "building": True},
    "CANTEEN":         {"name": "Canteen",                                                "x": 435, "y": 582,  "building": True},
    "NURSING":         {"name": "Nursing and Health Department",                          "x": 538, "y": 583,  "building": True},
    "DORMITORY":       {"name": "Dormitory",                                              "x": 505, "y": 298,  "building": True},
    "FOOD_LAB":        {"name": "Food Lab",                                               "x": 444, "y": 466,  "building": True},

    # --- Synthetic road junctions (menu-hidden, only used to shape routes) ---
    "J_TOP_W":        {"x": 120, "y": 345, "building": False},
    "J_TOP_MID":      {"x": 365, "y": 345, "building": False},
    "J_TOP_E":        {"x": 600, "y": 320, "building": False},
    "J_ROW1_MID":     {"x": 365, "y": 480, "building": False},
    "J_MIDHORIZ_MID": {"x": 365, "y": 585, "building": False},
    "J_MIDHORIZ_E":   {"x": 600, "y": 600, "building": False},
    "J_ROW2_MID":     {"x": 365, "y": 650, "building": False},
    "J_LOW_E":        {"x": 600, "y": 860, "building": False},
    "J_SOUTH_W":      {"x": 120, "y": 950, "building": False},
    "J_ROUNDABOUT":   {"x": 455, "y": 955, "building": False},
}

# Buildings only -- what the menu shows
LOCATIONS = {code: n for code, n in NODES.items() if n.get("building")}

# Two-letter acronym for each building, used as its marker on the ASCII map
MAP_ACRONYMS = {
    "MAIN_GATE":       "MG",
    "AUDIO_VISUAL":    "AV",
    "SALCEDA":         "SA",
    "ADMIN":           "AD",
    "CES":             "CE",
    "CSC":             "CS",
    "REGISTRAR":       "RG",
    "AUTOMOTIVE":      "AT",
    "RDEPO":           "RD",
    "PDMO":            "PD",
    "SABIDO":          "SB",
    "MACHINE_WELDING": "MW",
    "GYM":             "GY",
    "TECH_ENTREP":     "TE",
    "CANTEEN":         "CT",
    "NURSING":         "NH",
    "DORMITORY":       "DM",
    "FOOD_LAB":        "FL",
}

# ---------------------------------------------------------------------------
# 2. ROAD TOPOLOGY - traced from the visible walkways in the map image
# ---------------------------------------------------------------------------
EDGE_TOPOLOGY = [
    # West corridor (top to bottom)
    ("J_TOP_W", "MACHINE_WELDING"), ("MACHINE_WELDING", "SABIDO"), ("SABIDO", "PDMO"),
    ("PDMO", "RDEPO"), ("RDEPO", "AUTOMOTIVE"), ("AUTOMOTIVE", "REGISTRAR"), ("REGISTRAR", "J_SOUTH_W"),
    # Top horizontal road
    ("J_TOP_W", "J_TOP_MID"), ("J_TOP_MID", "J_TOP_E"),
    ("J_TOP_MID", "TECH_ENTREP"),
    # Middle corridor (top to bottom)
    ("J_TOP_MID", "J_ROW1_MID"), ("J_ROW1_MID", "J_MIDHORIZ_MID"),
    ("J_MIDHORIZ_MID", "J_ROW2_MID"), ("J_ROW2_MID", "J_ROUNDABOUT"),
    # Row 1 spurs (gym / food lab)
    ("J_ROW1_MID", "GYM"), ("J_ROW1_MID", "FOOD_LAB"),
    # Mid-horizontal road links
    ("J_MIDHORIZ_MID", "RDEPO"), ("J_MIDHORIZ_MID", "CANTEEN"), ("J_MIDHORIZ_MID", "J_MIDHORIZ_E"),
    # Row 2 spurs (CES / CSC)
    ("J_ROW2_MID", "CES"), ("J_ROW2_MID", "CSC"),
    # East perimeter road (top to bottom)
    ("J_TOP_E", "DORMITORY"), ("J_TOP_E", "J_MIDHORIZ_E"),
    ("J_MIDHORIZ_E", "NURSING"), ("J_MIDHORIZ_E", "J_LOW_E"),
    ("J_LOW_E", "SALCEDA"), ("J_LOW_E", "J_ROUNDABOUT"),
    # South road / main gate path
    ("J_SOUTH_W", "J_ROUNDABOUT"), ("J_ROUNDABOUT", "AUDIO_VISUAL"), ("J_ROUNDABOUT", "MAIN_GATE"),
    # Administration building block
    ("ADMIN", "AUTOMOTIVE"), ("ADMIN", "J_ROW2_MID"),
]


def _pixel_dist(a, b):
    ax, ay = NODES[a]["x"], NODES[a]["y"]
    bx, by = NODES[b]["x"], NODES[b]["y"]
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


# Adjacency list; weight is raw pixel distance, used only internally by
# Dijkstra to compare candidate paths (not shown to the user).
GRAPH = {n: [] for n in NODES}
for a, b in EDGE_TOPOLOGY:
    w = _pixel_dist(a, b)
    GRAPH[a].append((b, w))
    GRAPH[b].append((a, w))


# ---------------------------------------------------------------------------
# 3. DIJKSTRA'S SHORTEST PATH
# ---------------------------------------------------------------------------
def find_shortest_path(start, end):
    distances = {n: float("inf") for n in NODES}
    previous = {n: None for n in NODES}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_dist, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            break
        for neighbor, weight in GRAPH[current]:
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))

    if distances[end] == float("inf"):
        return None

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path


# ---------------------------------------------------------------------------
# 4. ASCII MAP RENDERING
#    Every building keeps its real x,y pixel coordinate from the campus
#    map image. Those coordinates are scaled down so the whole campus fits
#    a terminal-sized grid, where one character cell = one scaled
#    coordinate unit (i.e. "1 space in the terminal = 1 coordinate" on
#    this scaled grid).
# ---------------------------------------------------------------------------
GRID_WIDTH = 70
GRID_HEIGHT = 34

_all_x = [n["x"] for n in NODES.values()]
_all_y = [n["y"] for n in NODES.values()]
_MIN_X, _MAX_X = min(_all_x), max(_all_x)
_MIN_Y, _MAX_Y = min(_all_y), max(_all_y)


def _to_grid(x, y):
    """Map a real pixel coordinate to a (col, row) cell on the ASCII grid.
    Column range leaves room for a 2-character marker (acronyms are 2
    letters wide), so a marker never gets clipped by the right border."""
    col = round((x - _MIN_X) / (_MAX_X - _MIN_X) * (GRID_WIDTH - 2))
    row = round((y - _MIN_Y) / (_MAX_Y - _MIN_Y) * (GRID_HEIGHT - 1))
    return col, row


def _bresenham_line(c0, r0, c1, r1):
    """Return every grid cell on the straight line between two cells."""
    points = []
    dc = abs(c1 - c0)
    dr = -abs(r1 - r0)
    sc = 1 if c0 < c1 else -1
    sr = 1 if r0 < r1 else -1
    err = dc + dr
    c, r = c0, r0
    while True:
        points.append((c, r))
        if c == c1 and r == r1:
            break
        e2 = 2 * err
        if e2 >= dr:
            err += dr
            c += sc
        if e2 <= dc:
            err += dc
            r += sr
    return points


def _path_char(dc, dr):
    """Pick a road-like character for a segment based on its direction:
    '|' for mostly vertical, '_' for mostly horizontal, '/' or '\\' for
    a diagonal (depending on which way it slants)."""
    adc, adr = abs(dc), abs(dr)
    if adc == 0:
        return "|"
    if adr == 0:
        return "_"
    if adr >= adc * 2:
        return "|"
    if adc >= adr * 2:
        return "_"
    # Diagonal: screen row increases downward, so matching signs of
    # dc/dr slant like a backslash, opposite signs slant like a slash.
    return "\\" if (dc > 0) == (dr > 0) else "/"


def render_ascii_map(path):
    """Build the ASCII grid: the FULL road network drawn with directional
    characters (always shown, not just the found route), the specific
    route from current location to destination traced with dots on top
    (so it stands out from the rest of the network), all buildings as
    2-letter acronyms (uppercase = a stop on this route), and 'o'/'x'
    marking the current location and destination."""
    grid = [[" " for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    # 1. Draw every road in the network (the full graph), not just the
    #    edges used by this particular route -- this is the campus's
    #    road layout, always visible.
    for a, b in EDGE_TOPOLOGY:
        c0, r0 = _to_grid(NODES[a]["x"], NODES[a]["y"])
        c1, r1 = _to_grid(NODES[b]["x"], NODES[b]["y"])
        ch = _path_char(c1 - c0, r1 - r0)
        for c, r in _bresenham_line(c0, r0, c1, r1):
            if grid[r][c] == " ":
                grid[r][c] = ch

    # 2. Trace the specific route (current location -> destination) with
    #    dots on top of the network, so it's highlighted against the
    #    roads that aren't part of this trip.
    if path:
        for a, b in zip(path, path[1:]):
            c0, r0 = _to_grid(NODES[a]["x"], NODES[a]["y"])
            c1, r1 = _to_grid(NODES[b]["x"], NODES[b]["y"])
            for c, r in _bresenham_line(c0, r0, c1, r1):
                grid[r][c] = "."

    route_codes = set(path) if path else set()

    def place_marker(col, row, text):
        for i, ch in enumerate(text):
            if 0 <= col + i < GRID_WIDTH:
                grid[row][col + i] = ch

    # 3. All buildings for context; route buildings use their acronym in
    #    uppercase, others use the acronym in lowercase (still legible,
    #    but visually recedes compared to the highlighted route).
    for code, loc in LOCATIONS.items():
        c, r = _to_grid(loc["x"], loc["y"])
        acronym = MAP_ACRONYMS[code]
        if code in route_codes:
            place_marker(c, r, acronym)
        else:
            place_marker(c, r, acronym.lower())

    # 4. Mark current location and destination (overrides the acronym at
    #    that exact cell -- the step list above already names the
    #    building, this just pinpoints it on the map).
    if path:
        start_code, end_code = path[0], path[-1]
        sc, sr = _to_grid(NODES[start_code]["x"], NODES[start_code]["y"])
        ec, er = _to_grid(NODES[end_code]["x"], NODES[end_code]["y"])
        place_marker(sc, sr, "o ")
        place_marker(ec, er, "x ")

    lines = ["+" + "-" * GRID_WIDTH + "+"]
    for row in grid:
        lines.append("|" + "".join(row) + "|")
    lines.append("+" + "-" * GRID_WIDTH + "+")
    return "\n".join(lines)


def print_legend():
    print("\nMAP LEGEND")
    print("-" * 60)
    items = list(LOCATIONS.items())
    for i in range(0, len(items), 2):
        left_code, left_loc = items[i]
        left = f"{MAP_ACRONYMS[left_code]} = {left_loc['name']}"
        if i + 1 < len(items):
            right_code, right_loc = items[i + 1]
            right = f"{MAP_ACRONYMS[right_code]} = {right_loc['name']}"
            print(f"  {left:<42} {right}")
        else:
            print(f"  {left}")
    print("-" * 60)
    print("  o = your current location     x = destination")
    print("  .   = your route (highlighted against the full network)")
    print("  |   = other road running roughly north-south")
    print("  _   = other road running roughly east-west")
    print("  / \\ = other road running diagonally")
    print("  UPPERCASE acronym = a stop on your route")
    print("  lowercase acronym = other campus buildings (for reference)")


# ---------------------------------------------------------------------------
# 5. TERMINAL INTERFACE
# ---------------------------------------------------------------------------
def print_header():
    print("=" * 50)
    print("     BUPC CAMPUS NAVIGATION SYSTEM")
    print("=" * 50)


def print_location_menu(prompt_label):
    codes = list(LOCATIONS.keys())
    print(f"\n{prompt_label}")
    print("-" * 50)
    for i, code in enumerate(codes, start=1):
        print(f"  {i:>2}. {LOCATIONS[code]['name']}")
    print("-" * 50)
    return codes


def ask_location_choice(prompt_label):
    codes = print_location_menu(prompt_label)
    while True:
        choice = input(f"Enter number (1-{len(codes)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(codes):
            return codes[int(choice) - 1]
        print("Invalid choice. Please enter a valid number.")


def run():
    print_header()

    while True:
        start = ask_location_choice("CURRENT LOCATION")
        destination = ask_location_choice("DESTINATION")

        if start == destination:
            print("\nCurrent location and destination must be different. Try again.\n")
            continue

        path = find_shortest_path(start, destination)

        print("\n" + "=" * 50)
        if path is None:
            print("No route found between these locations.")
            print("=" * 50)
        else:
            steps = [NODES[n]["name"] for n in path if NODES[n].get("building")]
            print(f"ROUTE: {LOCATIONS[start]['name']} -> {LOCATIONS[destination]['name']}")
            print("-" * 50)
            for i, step_name in enumerate(steps, start=1):
                print(f"  {i}. {step_name}")
            print("=" * 50)
            print(render_ascii_map(path))
            print_legend()
            print("=" * 50)

        again = input("\nFind another route? (y/n): ").strip().lower()
        if again != "y":
            print("\nThank you for using BUPC Campus Navigation System.")
            break
        print()


if __name__ == "__main__":
    run()
