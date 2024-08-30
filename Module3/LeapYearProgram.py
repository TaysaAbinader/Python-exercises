year = float(input("Enter a year: "))
leap_year = year % 4 == 0
print(year)


if leap_year and (year % 100 != 0 or year % 400 == 0):
    print("Leap Year!")
else:
    print("Not Leap Year")
