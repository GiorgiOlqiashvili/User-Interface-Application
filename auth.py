import json
import os

ACCOUNTS_FILE = 'accounts.json'


def ensure_accounts_file():
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'w') as file:
            json.dump({}, file)


def load_accounts():
    ensure_accounts_file()
    with open(ACCOUNTS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_accounts(accounts):
    with open(ACCOUNTS_FILE, 'w') as file:
        json.dump(accounts, file)


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    accounts = load_accounts()
    if username in accounts:
        print("Username already exists.")
        return None
    accounts[username] = password
    save_accounts(accounts)
    print("Registration successful.")
    return username


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    accounts = load_accounts()
    if accounts.get(username) == password:
        print("Login successful.")
        return username
    print("Invalid username or password.")
    return None


def authenticate():
    while True:
        choice = input("Register (r) or Login (l)? ").lower()
        if choice == 'r':
            return register()
        elif choice == 'l':
            return login()


