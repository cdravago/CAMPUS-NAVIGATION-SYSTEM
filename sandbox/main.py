from database import campus_locations
#push test
#push test success
MAX_HISTORY = 5
navigation_history = []

def log_search(term):
    term = term.strip()
    if not term:
        return
    if len(navigation_history) >= MAX_HISTORY:
        navigation_history.pop(0)
    navigation_history.append(term)

def search_building():
    # Linear Search Algorithm
    search_term = input("\nEnter the name of the building to search: ").lower()
    log_search(search_term)
    found = False

    print("\nSearch Results")
    for loc in campus_locations:
        if search_term in loc.name.lower():
            print(loc.display_info())
            found = True

    if not found:
        print("Building not found. Please try another name")

def view_history():
    print(f"\nNavigation History (last {MAX_HISTORY} searches)")
    if not navigation_history:
        print("No search history yet.")
        return

    for i, term in enumerate(navigation_history, start=1):
        print(f"{i}. {term}")

def building_stats():
    categories = []
    for loc in campus_locations:
        if loc.category not in categories:
            categories.append(loc.category)

    print("\nBuilding Stats / Filter by Category")
    print("[1] View building count  per category")
    print("[2] Filter Buildings by category")
    choice = int(input("Select an option [1 - 2]: "))

    match choice:
        case 1:
            print("\nBuilding Counter per Category")
            for cat in categories:
                count = 0
                for loc in campus_locations:
                    if loc.category == cat:
                        count += 1
                print(f"{cat}: {count}")
        case 2:
            print("\nAvailable Categories:", ", ".join(categories))
            cat_input = input("Enter category to filter: ").strip()

            matches = []
            for loc in campus_locations:
                if loc.category.lower() == cat_input.lower():
                    matches.append(loc)

            if matches:
                print(f"\nBuildings under {cat_input}")
                for loc in matches:
                    print(loc.display_info())
            else:
                print(f"No buildings found under category '{cat_input}'")
        case _:
            print("Invalid choice. Please enter [1 - 2]")


def main_menu():
    while True:
        print("\nCAMPUS NAVIGATION SYSTEM")
        print("[1] Search for a Building")
        print("[2] View Navigation History")    # Stack - Array(log) for now
        print("[3] Building Stats / Filter")    # Array 
        print("[4] Plan a Route")               # Graph - future implementation
        print("[5] Exit")

        choice = input("Select an option [1 - 5]: ")

        match choice:
            case '1':
                search_building()
            case '2':
                view_history()
            case '3':
                building_stats()
            case '4':
                pass
            case '5':
                print("Exiting System...")
                break
            case _:
                print("Invalid choice. Please enter [1 - 5]")

if __name__ == "__main__":
    main_menu()
