gallon_input = float(input("Amount in gallons: "))

def litres(x):
    return (x * 3.785)

while gallon_input >=0:
    amount = litres(gallon_input)
    print(f"{gallon_input} gallons are {amount}")
    gallon_input = float(input("Amount in gallons: "))


