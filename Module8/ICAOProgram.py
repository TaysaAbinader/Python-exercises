from DatabaseConnection import connection

def get_airport_location_by_icao (icao):
    sql = f"select name, municipality from airport where airport.ident = '{icao}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in results:
            print(f"- Airport: {row[0]}, location: {row[1]}")
    if cursor.rowcount == 0:
        return
    return

icao = input("Inform the ICAO of the airport: ")

get_airport_location_by_icao(icao)

