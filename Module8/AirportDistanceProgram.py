from DatabaseConnection import connection
from geopy import distance

def get_distance_betwen_airports(icao1, icao2):
    sql = f"select latitude_deg, longitude_deg from airport where airport.ident = '{icao1}' or airport.ident = '{icao2}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount == 2:
        distance_in_kilometers = distance.distance(results[0], results[1]).kilometers
        print(f"The distance between {icao1} and {icao2} is {distance_in_kilometers} kilometers")
    else:
        print(f"Invalid result: {results}")
    return

icao1 = input("Inform the ICAO of the first airport: ")
icao2 = input("Inform the ICAO of the second airport: ")

get_distance_betwen_airports(icao1, icao2)