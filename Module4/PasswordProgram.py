username = input("Enter your username: ").lower()
password = input("Enter your password: ").lower()
attempts = 1

while username != "python" and password != "rules":
    username = input("Enter your username: ").lower()
    password = input("Enter your password: ").lower()
    attempts += 1
    if attempts == 5:
        print("Access Denied")
        exit()
    print("Welcome")
    exit()