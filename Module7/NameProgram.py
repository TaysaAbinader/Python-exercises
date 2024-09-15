user_input = input("Give me a name: ")
names = set()

while user_input != "":
    name = user_input
    names.add(name)
    print("New name.")
    user_input = input("Give me a name: ")
    if user_input in names:
        name != user_input
        print("Existing")
        user_input = input("Give me a name: ")
for name in names:
    print(f" - {(name)}")
















