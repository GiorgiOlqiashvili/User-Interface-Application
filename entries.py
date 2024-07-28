import json
import os


def load_entries(username):
    filename = f'{username}_entries.json'
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def save_entries(username, entries):
    filename = f'{username}_entries.json'
    with open(filename, 'w') as file:
        json.dump(entries, file)


def add_entry(username):
    entries = load_entries(username)
    memo = input("Enter memo: ")
    entry_id = len(entries) + 1
    entries.append({'id': entry_id, 'memo': memo})
    save_entries(username, entries)
    print("Entry added successfully.")

