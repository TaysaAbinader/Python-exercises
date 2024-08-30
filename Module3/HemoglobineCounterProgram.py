biological_gender = input("Enter your biological gender: ").upper()
hemoglobine_levels = float(input("Enter your hemoglobine levels (g/l): "))
print(biological_gender)
print(hemoglobine_levels)

if biological_gender == "MALE" and hemoglobine_levels < 134:
    print ("LOW")
elif biological_gender == "MALE" and hemoglobine_levels > 167:
    print ("HIGH")
elif biological_gender == "FEMALE" and hemoglobine_levels < 117:
    print ("LOW")
elif biological_gender == "FEMALE" and hemoglobine_levels > 155:
    print ("HIGH")
else:
    print ("NORMAL")