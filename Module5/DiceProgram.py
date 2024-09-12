import random

dice_quantity = int(input("How many dices?"))
dice_value = sum_rolls = 0

for i in range(dice_quantity):
    dice_value = random.randint(1, 6)
    print(dice_value)
    sum_rolls = sum_rolls + dice_value

print(sum_rolls)












