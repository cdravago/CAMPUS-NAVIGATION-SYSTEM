# NAVIGATION HISTORY - Stack (LIFO: Last In, First Out)
# The stack is a plain list. The END of the list is the TOP of the stack,
# so the newest search is always on top.

history_stack = []


def push(term):
    # Put a new search on top of the stack
    history_stack.append(term)


def pop():
    # Take the top (newest) search off the stack
    # Returns None if the stack is empty
    if is_empty():
        return None
    return history_stack.pop()


def is_empty():
    return len(history_stack) == 0


def view_history():
    # Show the stack from top (newest) to bottom (oldest) without removing anything
    print("\n[-------------------------------------------]")
    print("        [-NAVIGATION HISTORY-]")
    if is_empty():
        print("       [-NO SEARCH HISTORY FOUND-]")
    else:
        number = 1
        for i in range(len(history_stack) - 1, -1, -1):
            print(f"{number}. {history_stack[i]}")
            number += 1
    print("[-------------------------------------------]\n")


def remove_latest():
    removed = pop()
    print("\n[-------------------------------------------]")
    if removed is None:
        print("       [-NOTHING TO REMOVE-]")
    else:
        print(f"  [-REMOVED MOST RECENT SEARCH: {removed}-]")
    print("[-------------------------------------------]\n")


def history_menu():
    while True:
        print("[-------------------------------------------]")
        print("        [-NAVIGATION HISTORY-]")
        print("[1] View history (newest first)")
        print("[2] Remove most recent search")
        print("[3] Back")
        print("[-------------------------------------------]")

        choice = input("Select an option [1 - 3]: ").strip()

        if choice == "1":
            view_history()
        elif choice == "2":
            remove_latest()
        elif choice == "3":
            return
        else:
            print("\n  [-INVALID CHOICE. PLEASE ENTER [1 - 3]-]\n")
