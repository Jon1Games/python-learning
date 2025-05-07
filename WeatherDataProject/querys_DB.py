import sqlite3

db_name = "weather_data.db"

def get_time_data(stations_id, field_name, limit, start_date):
    """
    Retrieves data with times and an optional limit for an specific sation id
    Args:
        stations_id (str): The ID of the weather station.
        field_name (str): The name of the field to average (e.g., 'TT_TU').
        limit (int): The maximum number of records to retrieve. -1 is all
    Returns:
        list: A list of tuples, where each tuple contains the MESS_DATUM and the value of the specified field.
              Returns an empty list if no data is found.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if stations_id == -1:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE MESS_DATUM >= {start_date} limit {limit};")
    else:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}' WHERE MESS_DATUM >= {start_date} limit {limit};")
    data = cursor.fetchall()

    conn.close()
    return data

def get_time_data_between(stations_id, field_name, start_date, end_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if stations_id == -1:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE MESS_DATUM BETWEEN {start_date} and {end_date};")
    else:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM BETWEEN {start_date} and {end_date};")
    data = cursor.fetchall()

    conn.close()
    return data

def get_averages(stations_id, field_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if stations_id == -1:
        cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag;")
    else:
        cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}';")
    data = cursor.fetchone()

    conn.close()
    return data[0]

def get_averages_between(stations_id, field_name, start_date, end_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    if stations_id == -1:
        cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag WHERE MESS_DATUM between {start_date} and {end_date};")
    else:
        cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM between {start_date} and {end_date};")
    data = cursor.fetchone()

    conn.close()
    return data[0]

def format_time(oTime):
    """
    Format time form YYYYMMDD to DD.MM.YYYY (German readable time format) and back
    """
    time = str(oTime)
    if "." in time:
        day, month, year = time.split(".")
        return f"{year}{month}{day}"
    year = time[:4]
    month = time[4:6]
    day = time[6:8]
    return f"{day}.{month}.{year}"

def query():
    station = input("Station id or name: ")
    if station.lower() == "all":
        station = -1
    else:
        try:
            station = int(station)
        except:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()

            cursor.execute(f"SELECT Stations_ID FROM Metadaten_Geographie WHERE Stationsname = '{station}';")
            data = cursor.fetchone()
            if data:
                station = data[0]
                conn.close()
            else:
                print(f"No station found with name {station}")
                cursor.execute(f"SELECT Stations_ID, Stationsname FROM Metadaten_Geographie WHERE Stationsname LIKE '%{station}%';")
                data = cursor.fetchall()
                print(f"Do you meean one of these?")

                names = []
                for entry in data:
                    names.append(entry[1])
                names = list(set(names))
                for name in names:
                    print(name)
                
                conn.close()
                exit()
            
    print("""
        Data stored:
        QN_3 - Quality index of 3 hours of sunshine duration
        FX - Maximum wind speed
        FM - Average wind speed
        QN_4 - Quality index of 24-hour precipitation amount
        RSK - Daily precipitation amount
        RSKF - Precipitation form (rain or snow)
        SDK - Sunshine duration
        SHK_Tag - Daily snow depth
        NM - Cloud cover
        VPM - Vapour pressure
        PM - Air pressure
        TMK - Medium temperature at 2m height
        UPM - Relative humidity
        TXK - Maximum temperature at 2m height
        TNK - Minimum temperature at 2m height
        TGK - Daily average temperature at 2m height
        """)
    collumn = input("Wich data?: ").capitalize()
            
    print("""
        Querys:
        1 - data with date with limit
        2 - data with date between dates
        3 - all averages
        4 - all averages between
        """)

    query_id = int(input("Query: "))

    if query_id == 1:
        start_date = format_time(input("Start date: "))
        limit = int(input("Limit: "))
        print(f"Get {collumn} from station {station} with limit {limit} stating at {start_date}")
        data = get_time_data(station, collumn, limit, start_date)
        print("Station | Date: value")
        for set in data:
            print(f"{set[0]} | {format_time(set[1])}: {set[2]}") 
    elif query_id == 2:
        print("Dates as DD.MM.YYYY")
        start_date = format_time(input("Start date: "))
        end_date = format_time(input("End date: "))
        print(f"Get {collumn} between {start_date} and {end_date} fromstation {station}")
        data = get_time_data_between(station, collumn, start_date, end_date)
        print("Station | Date: value")
        for set in data:
            print(f"{set[0]} | {format_time(set[1])}: {set[2]}")
    elif query_id == 3:
        print(f"Get all averages from station {station} for {collumn}")
        print(get_averages(station, collumn))
    elif query_id == 4:
        print("Dates as DD.MM.YYYY")
        start_date = format_time(input("Start date: "))
        end_date = format_time(input("End date: "))
        print(f"Averages between {start_date} and {end_date} from station {station}")
        print(get_averages_between(station, collumn, start_date, end_date))