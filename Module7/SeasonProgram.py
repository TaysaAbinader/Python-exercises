seasons = ("Winter","Spring","Summer","Autumn")
(season1, season2, season3, season4) = seasons
user_input = int(input("Type the number of the month: "))

if user_input == 12 or user_input == 1 or user_input == 2:
    print(f"It's {season1}.")
elif user_input == 3 or user_input == 4 or user_input == 5:
    print(f"It's {season2}.")
elif user_input == 6 or user_input == 7 or user_input == 8:
    print(f"It's {season3}.")
elif user_input == 9 or user_input == 10 or user_input == 11:
    print(f"It's {season4}.")
else:
    quit()








