airports = {"YSSY":"Australia",
            "EBBR":"Belgium",
            "SAEZ":"Argentina",
            "SLVR":"Bolivia",
            "SBGR":"Brazil",
            "ZBAA":"China",
            "EDDF":"Germany",
            "EFHK":"Finland",
            "EGLL":"United Kingdom"}

user_input = input("To enter a new airport type - new, to consult existing airport type - existing, or to quit type - quit:")
while user_input != "quit":
    if user_input == "new":
        icao = input("ICAO: ")
        airport_location = input("Country: ")
        airports[icao] = airport_location
        user_input = input("To enter a new airport type - new, to consult existing airport type - existing, or to quit type - quit:")

    elif user_input == "existing":
        icao = input("ICAO: ")
        if icao in airports:
            print({airports[icao]})
        user_input = input("To enter a new airport type - new, to consult existing airport type - existing, or to quit type - quit:")

if user_input == "quit":
    print("Program ended.")
    quit()

