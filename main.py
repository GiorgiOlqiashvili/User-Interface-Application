from auth import authenticate
from entries import add_entry, load_entries
from utils import sort_entries

current_user = authenticate()
if not current_user:
    print("Authentication failed.")
else:
    print(f"Welcome, {current_user}!")
    while True:
        action = input("Add entry (a), Sort entries (s) or Quit (q)? ").lower()
        if action == 'a':
            add_entry(current_user)
        elif action == 's':
            entries = load_entries(current_user)
            sort_by = input("Sort by ID (id) or Memo (memo)? ").lower()
            sorted_entries = sort_entries(entries, sort_by)
            print("Sorted entries:", sorted_entries)
        elif action == 'q':
            break
        else:
            print("Invalid option.")
