import random

number = int(input("Guess a number from 1 to 10: "))
random = random.randint(1, 10)

while number != random:
    if number > random:
        print("Too high!")

    if number < random:
        print("Too low!")
    number = int(input("Guess a number from 1 to 10: "))

print("Correct!")
