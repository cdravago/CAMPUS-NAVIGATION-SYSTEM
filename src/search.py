# BUILDING SEARCH
#   Search by name -> Linear Search (checks every building one by one)
#   Search by ID   -> Binary Search (needs the list to be in order by ID)

from database import campus_locations
from history import push


def search_by_name():
    # Linear Search Algorithm
    term = input("\nEnter the name of the building to search: ").strip().lower()
    if term == "":
        print("\n  [-SEARCH CANNOT BE EMPTY-]\n")
        return

    push(term)  # save the search in the history stack
    found = False

    print("\n[-------------------------------------------]")
    print("           [-SEARCH RESULTS-]")
    for loc in campus_locations:
        if term in loc.name.lower():
            print(loc.display_info())
            found = True

    if not found:
        print("   [-BUILDING NOT FOUND, TRY ANOTHER NAME-]")
    print("[-------------------------------------------]\n")


def search_by_id():
    # Binary Search Algorithm
    # campus_locations is already in order by building ID, so we can keep
    # cutting the search area in half.
    text = input("\nEnter the building ID to search: ").strip()
    if not text.isdigit():
        print("\n  [-PLEASE ENTER A WHOLE NUMBER-]\n")
        return

    target = int(text)
    push("ID " + text)  # save the search in the history stack

    low = 0
    high = len(campus_locations) - 1
    found = None

    while low <= high:
        mid = (low + high) // 2
        mid_id = campus_locations[mid].building_id
        if mid_id == target:
            found = campus_locations[mid]
            break
        elif mid_id < target:
            low = mid + 1
        else:
            high = mid - 1

    print("\n[-------------------------------------------]")
    print("           [-SEARCH RESULTS-]")
    if found is not None:
        print(found.display_info())
    else:
        print("   [-BUILDING ID NOT FOUND-]")
    print("[-------------------------------------------]\n")


def search_menu():
    while True:
        print("[-------------------------------------------]")
        print("        [-SEARCH FOR A BUILDING-]")
        print("[1] Search by name")
        print("[2] Search by ID")
        print("[3] Back")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 3]: ").strip()

        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_by_id()
        elif choice == "3":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
