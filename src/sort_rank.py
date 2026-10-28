# DIRECTORY SORT / RANK - Bubble Sort, Insertion Sort, Selection Sort
# Every sort works on a COPY of campus_locations, so the original list stays
# in order by ID (Binary Search by ID needs that).

from database import campus_locations


def get_key(loc, by_name):
    # The value we compare: the building name (A-Z) or the building ID
    if by_name:
        return loc.name.lower()
    return loc.building_id


def bubble_sort(items, by_name):
    # Compare neighbors and swap them if they are in the wrong order
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if get_key(items[j], by_name) > get_key(items[j + 1], by_name):
                temp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = temp


def insertion_sort(items, by_name):
    # Take one item at a time and insert it into its place in the sorted part
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >= 0 and get_key(items[j], by_name) > get_key(current, by_name):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = current


def selection_sort(items, by_name):
    # Find the smallest item in the unsorted part and move it to the front
    n = len(items)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if get_key(items[j], by_name) < get_key(items[smallest], by_name):
                smallest = j
        temp = items[i]
        items[i] = items[smallest]
        items[smallest] = temp


def directory_sort():
    print("\n[-------------------------------------------]")
    print("        [-DIRECTORY SORT / RANK-]")
    print("Sort by:")
    print("[1] Name (A - Z)")
    print("[2] Building ID")
    print("[-------------------------------------------]\n")
    key_choice = input("Select an option [1 - 2]: ").strip()
    if key_choice != "1" and key_choice != "2":
        print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 2]-]\n")
        return
    by_name = (key_choice == "1")

    print("\nSorting method:")
    print("[1] Bubble Sort")
    print("[2] Insertion Sort")
    print("[3] Selection Sort")
    method = input("Select an option [1 - 3]: ").strip()

    items = campus_locations.copy()  # sort a copy, keep the original in order

    if method == "1":
        bubble_sort(items, by_name)
        method_name = "BUBBLE SORT"
    elif method == "2":
        insertion_sort(items, by_name)
        method_name = "INSERTION SORT"
    elif method == "3":
        selection_sort(items, by_name)
        method_name = "SELECTION SORT"
    else:
        print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
        return

    if by_name:
        label = "NAME (A - Z)"
    else:
        label = "BUILDING ID"

    print("\n[-------------------------------------------]")
    print(f"  [-SORTED BY {label} USING {method_name}-]")
    for loc in items:
        print(loc.display_info())
    print("[-------------------------------------------]\n")
