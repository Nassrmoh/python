users = [
    {"name": "omar", "password": "123"},
    {"name": "Omar", "password": "143"},
    {"name": "ahmed", "password": "456"}
]
def checker(name, password):
    for user in users: #for loop to loop on each user
        if user["name"].lower() == name.lower() and user["password"] == password:
            return True
    return False
def login():
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    if checker(user_name, password):
        print("Valid Login")
    else:
        print("Invalid username or password")
login()