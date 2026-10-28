# BUILDING STATS / FILTER - Array counting and linear filtering

from database import campus_locations


def get_categories():
    # Build a list of each category once (no repeats)
    categories = []
    for loc in campus_locations:
        if loc.category not in categories:
            categories.append(loc.category)
    return categories


def count_per_category():
    categories = get_categories()
    print("\n[-------------------------------------------]")
    print("       [-BUILDING COUNT PER CATEGORY-]")
    for cat in categories:
        count = 0
        for loc in campus_locations:
            if loc.category == cat:
                count += 1
        print(f"{cat}: {count}")
    print("[-------------------------------------------]\n")


def filter_by_category():
    categories = get_categories()
    print("\nAVAILABLE CATEGORIES:", ", ".join(categories))
    cat_input = input("Enter category to filter: ").strip()

    matches = []
    for loc in campus_locations:
        if loc.category.lower() == cat_input.lower():
            matches.append(loc)

    print("\n[-------------------------------------------]")
    if len(matches) > 0:
        print(f"     [-BUILDINGS UNDER {cat_input.upper()}-]")
        for loc in matches:
            print(loc.display_info())
    else:
        print(f"   [-NO BUILDINGS FOUND UNDER CATEGORY '{cat_input}'-]")
    print("[-------------------------------------------]\n")


def building_stats():
    print("\n[-------------------------------------------]")
    print("   [-BUILDING STATS / FILTER BY CATEGORY-]")
    print("[1] View building count per category")
    print("[2] Filter buildings by category")
    print("[-------------------------------------------]\n")

    # The choice is read as text (not int) so typing letters cannot crash the program
    choice = input("Select an option [1 - 2]: ").strip()

    if choice == "1":
        count_per_category()
    elif choice == "2":
        filter_by_category()
    else:
        print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 2]-]\n")
