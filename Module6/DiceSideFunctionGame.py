import random
side_input = int(input("Give me the amount ou sides: "))

def dice(value):
    return random.randint(1, value)

amount = 0
while amount < side_input:
    amount = dice(side_input)
    print(amount)