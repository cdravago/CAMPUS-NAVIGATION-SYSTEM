from database import campus_locations

def search_building():
    # Linear Search Algorithm
    search_term = input("\nEnter the name of the building to search: ").lower()
    found = False

    print("\nSearch Results")
    for loc in campus_locations:
        if search_term in loc.name.lower():
            print(loc.display_info())
            found = True

    if not found:
        print("Building not found. Please try another name")

def main_menu():
    while True:
        print("\nCAMPUS NAVIGATION SYSTEM")
        print("[1] Search for a Building")
        print("[2] View Navigation History") # Stack
        print("[3] Plan a Route")            # Graph
        print("[4] Exit")

        choice = input("Select an option [1 - 4]: ")

        match choice:
            case '1':
                search_building()
            case '2':
                pass 
            case '3':
                pass
            case '4':
                print("\nExiting system...")
                break
            case _:
                print("Invalid choice. Please enter [1 - 4]")

if __name__ == "__main__":
    main_menu()
