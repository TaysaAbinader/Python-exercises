def pizza_squaremeter (diameter, price):
    diameter = diameter/100
    unit_price = float(price/diameter)
    return unit_price

pizza1_diam_input = input("Diameter of pizza 1: ")
pizza1_price_input = input("Price od pizza 1: ")
pizza2_diam_input = input("Diameter of pizza 2: ")
pizza2_price_input = input("Price of pizza 2: ")
pizza1 = pizza_squaremeter(float(pizza1_diam_input),float(pizza1_price_input))
pizza2 = pizza_squaremeter(float(pizza2_diam_input), float(pizza2_price_input))


if pizza1 < pizza2:
    pizza1 = "First Pizza"
    print(pizza1 + " has the best value for money.")
else:
    pizza2 = "Second Pizza"
    print(pizza2 + " has the best value for money.")





