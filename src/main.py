# CAMPUS NAVIGATION SYSTEM - main menu
# Each option calls a function from its own file:
#   search.py    - Building Search       (Linear Search, Binary Search)
#   history.py   - Navigation History    (Stack)
#   stats.py     - Building Stats/Filter (Arrays)
#   sort_rank.py - Directory Sort/Rank   (Bubble, Insertion, Selection Sort)
#   route.py     - Route Planning        (Queue, Stack)

from search import search_menu
from history import history_menu
from stats import building_stats
from sort_rank import directory_sort
from route import plan_route


def main_menu():
    while True:
        print("[-------------------------------------------]")
        print("      [-CAMPUS NAVIGATION SYSTEM-]")
        print("[1] Search for a Building")
        print("[2] View Navigation History")
        print("[3] Building Stats / Filter")
        print("[4] Directory Sort / Rank")
        print("[5] Plan a Route")
        print("[6] Exit")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 6]: ").strip()

        if choice == "1":
            search_menu()
        elif choice == "2":
            history_menu()
        elif choice == "3":
            building_stats()
        elif choice == "4":
            directory_sort()
        elif choice == "5":
            plan_route()
        elif choice == "6":
            print("EXITING SYSTEM...")
            break
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 6]-]\n")


if __name__ == "__main__":
    main_menu()
