# ROUTE PLANNING - uses a Queue and a Stack (plus arrays)
#   Queue: explores the roads outward from the start, one step at a time
#          (FIFO - the first point added is the first one explored)
#   Stack: flips the path around so it prints from start to destination
#          (LIFO - the last point added is the first one taken out)
# The result is the route with the FEWEST ROAD STEPS, not the fewest meters.

from database import campus_locations, connections, TOTAL_POINTS

BUILDING_COUNT = len(campus_locations)


def get_neighbors(point):
    # Linear search through the connections for every point next to this one
    neighbors = []
    for a, b in connections:
        if a == point:
            neighbors.append(b)
        elif b == point:
            neighbors.append(a)
    return neighbors


def find_route(start, destination):
    # Arrays indexed by point number (index 0 is not used)
    visited = [False] * (TOTAL_POINTS + 1)
    came_from = [0] * (TOTAL_POINTS + 1)

    # --- Queue: explore the roads ---
    queue = []
    queue.append(start)          # enqueue
    visited[start] = True

    while len(queue) > 0:
        current = queue.pop(0)   # dequeue (take from the front)
        if current == destination:
            break
        for neighbor in get_neighbors(current):
            if not visited[neighbor]:
                visited[neighbor] = True
                came_from[neighbor] = current   # remember where we came from
                queue.append(neighbor)

    if not visited[destination]:
        return []   # no route found

    # --- Stack: walk back from the destination, then pop to read forward ---
    stack = []
    point = destination
    while point != start:
        stack.append(point)      # push
        point = came_from[point]
    stack.append(start)

    path = []
    while len(stack) > 0:
        path.append(stack.pop()) # pop gives start first, destination last
    return path


def ask_building(label):
    while True:
        text = input(label).strip()
        if text.isdigit() and 1 <= int(text) <= BUILDING_COUNT:
            return int(text)
        print(f"  [-INVALID CHOICE. ENTER A NUMBER FROM 1 TO {BUILDING_COUNT}-]")


def plan_route():
    print("\n[-------------------------------------------]")
    print("            [-PLAN A ROUTE-]")
    for loc in campus_locations:
        print(loc.display_info())
    print("[-------------------------------------------]\n")

    start = ask_building("Enter the ID of your current location: ")
    destination = ask_building("Enter the ID of your destination: ")

    print("\n[-------------------------------------------]")
    if start == destination:
        print("   [-START AND DESTINATION ARE THE SAME-]")
    else:
        path = find_route(start, destination)
        if len(path) == 0:
            print("        [-NO ROUTE FOUND-]")
        else:
            print("              [-ROUTE-]")
            # Only buildings are printed. Points above BUILDING_COUNT are
            # road junctions, so they are skipped.
            for point in path:
                if point <= BUILDING_COUNT:
                    print(f"  {campus_locations[point - 1].name}")
            print(f"Road steps: {len(path) - 1}")
    print("[-------------------------------------------]\n")
