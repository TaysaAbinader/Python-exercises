from DatabaseConnection import connection

def get_airport_by_area_code (code):
    sql = f"select name, type from airport where airport.iso_country = '{code}'order by airport.type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in results:
            print(f"- Airport: {row[0]}, type: {row[1]}")
    return

code = input("Inform the area code of the airports: ")

get_airport_by_area_code(code)