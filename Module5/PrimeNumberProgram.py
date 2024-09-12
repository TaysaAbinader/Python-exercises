number_input = int(input("Give me an integer number, I'll tell you if it's a prime: "))

for item in range(2, number_input):
    if number_input % item == 0:
        print (f"{number_input} is not a prime.")
        quit()

print(f"{number_input} is a prime.")