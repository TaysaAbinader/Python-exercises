import random

def dice():
    return random.randint(1,6)


value = 0
while value != 6:
    value = dice()
    print(value)



