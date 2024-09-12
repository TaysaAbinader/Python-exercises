numbers = []
number_input = input("Enter number: ")

while number_input != "":
    numbers.append(int(number_input))
    number_input = input("Enter a number: ")
numbers.sort(reverse=True)

print(numbers[:5])






