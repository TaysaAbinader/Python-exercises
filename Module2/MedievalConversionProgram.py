talents_str = input("Enter Talents: ")
talents = float(talents_str)
talents_to_grams = float(talents * 20 * 32 * 13.3)

pounds_str = input("Enter Pounds: ")
pounds = float(pounds_str)
pounds_to_grams = float(pounds * 32 * 13.3)

lot_str = input("Enter Lots: ")
lot = float(lot_str)
lot_to_grams = float(lot * 13.3)

grams_total = lot_to_grams + pounds_to_grams + talents_to_grams
grams_to_kg_int = int(grams_total / 1000)

print (f"Weight in kg: {grams_to_kg_int} kilograms", f"Weight in grams: {grams_total % 1000:.2f} grams")



