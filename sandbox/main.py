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

    print("\n[-------------------------------------------]")
    print("           [-SEARCH RESULTS-]")
    for loc in campus_locations:
        if search_term in loc.name.lower():
            print(loc.display_info())
            print("[-------------------------------------------]\n")
            found = True

    if not found:
        print("   [-BUILDING NOT FOUND, TRY ANOTHER NAME-]")
        print("[-------------------------------------------]\n")

def view_history():
    print("\n[-------------------------------------------]")
    print(f"  [-NAVIGATION HISTORY (LAST {MAX_HISTORY} SEARCHES)-]")
    if not navigation_history:
        print("\n[-------------------------------------------]")
        print("         [-NO SEARCH HISTORY FOUND]-")
        print("[-------------------------------------------]\n")
        return

    for i, term in enumerate(navigation_history, start=1):
        print(f"{i}. {term}")
    print("[-------------------------------------------]\n")

def building_stats():
    categories = []
    for loc in campus_locations:
        if loc.category not in categories:
            categories.append(loc.category)
    print("\n[-------------------------------------------]")
    print("   [-BUILDING STATS / FILTER BY CATEGORY-]")
    print("[1] View building count  per category")
    print("[2] Filter Buildings by category")
    print("[-------------------------------------------]\n")
    choice = int(input("Select an option [1 - 2]: "))

    match choice:
        case 1:
            print("\n[-------------------------------------------]")
            print("       [-BUILDING COUNT PER CATEGORY-]")
            for cat in categories:
                count = 0
                for loc in campus_locations:
                    if loc.category == cat:
                        count += 1
                print(f"{cat}: {count}")
            print("[-------------------------------------------]\n")
        case 2:
            print("AVAILABLE CATEGORIES:", ", ".join(categories))
            cat_input = input("Enter category to filter: ").strip()

            matches = []
            for loc in campus_locations:
                if loc.category.lower() == cat_input.lower():
                    matches.append(loc)

            if matches:
                print(f"\n     [-BUILDINGS UNDER {cat_input.upper()}-]")
                for loc in matches:
                    print(loc.display_info())
                print("[-------------------------------------------]\n")
            else:
                print(f"   [-NO BUILDINGS FOUND UNDER CATEGORY '{cat_input}'-]")
        case _:
            print("Invalid choice. Please enter [1 - 2]")
        


def main_menu():
    while True:

        print("[-------------------------------------------]")
        print("      [-CAMPUS NAVIGATION SYSTEM-] ＼(￣▽￣)／")
        print("[1] Search for a Building")
        print("[2] View Navigation History")    # Stack - Array(log) for now
        print("[3] Building Stats / Filter")    # Array 
        print("[4] Plan a Route")               # Graph - future implementation
        print("[5] Exit")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 5]: ")
        #sherwin was here
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
                print("EXITING SYSTEM...")
                break
            case _:
                print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 5]-]\n")

if __name__ == "__main__":
    main_menu()
