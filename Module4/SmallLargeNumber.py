user_input = input("Enter a number: ")

if user_input == "":
    exit()

number = largest = smallest = int(user_input)

while user_input != "":
    number = int(user_input)
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    number = user_input = input("Enter a number: ")

print(f"Largest number: {largest} and Smallest number: {smallest}")






