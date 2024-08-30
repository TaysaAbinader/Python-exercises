cabin_type = input("Cabin Class: ").upper()
print(cabin_type)

if cabin_type == "LUX":
    print ("Upper-deck cabin with a balcony.")
elif cabin_type == "CABIN A":
    print ("Above the car deck, equipped with a window.")
elif cabin_type == "CABIN B":
    print ("Windowless cabin above the car deck.")
elif cabin_type == "CABIN C":
    print ("Windowless cabin below the car deck.")
else:
    print ("Invalid Cabin Class")