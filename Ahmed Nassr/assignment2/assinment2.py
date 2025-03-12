Name = input("write your name ")
try:
    if not Name.isalpha():
        raise ValueError("Invalid name")
    print(f"welcome {Name}")
except ValueError as e:
    print(e)
    
while True:
    email = input("enter your email: ")
    try:
        username, domain = email.split("@")
        x, y = domain.split(".")
        if not username or not domain or not x or not y:
            raise ValueError("Invalid email structure")
        break
    except ValueError as e:
        print("Invalid email, please enter a valid email")

print(f"\nyour name is {Name}")
print(f"your email is {email}")