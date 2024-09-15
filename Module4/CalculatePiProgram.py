import random

# Let N be the total number of random points.
N = int(input("How many points should I generate? "))
counter = 0
n = 0

while counter < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1, 1)
    if x*x + y*y < 1:
        # point is inside the circle
        n += 1
    counter += 1

pi = 4*n/N
print(f"The approximation of pi is {pi}")



