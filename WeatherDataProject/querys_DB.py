import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

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
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM >= '{start_date}' limit {limit};")
    data = cursor.fetchall()

    conn.close()
    return data

def get_time_data_between(stations_id, field_name, start_date, end_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    print(start_date, end_date)

    if stations_id == -1:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE MESS_DATUM BETWEEN {start_date} and {end_date};")
    else:
        cursor.execute(f"SELECT STATIONS_ID, MESS_DATUM, {field_name} FROM produkt_klima_tag WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM BETWEEN '{start_date}' and '{end_date}';")
    data = cursor.fetchall()

    conn.close()
    return data

def get_averages(stations_id, field_name, start_date, limit):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    data = []

    for x in range(0, limit):
        print("Process: " + str(start_date))
        cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag WHERE MESS_DATUM BETWEEN '{start_date}0101' and '{start_date}1231' AND STATIONS_ID = '{stations_id}';")
        data.append(cursor.fetchone())
        start_date += 1

    conn.close()
    return data

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

def plot_time_data(stations_id, field_name, limit: str, start_date):
    """
    Retrieves time series data and plots it using matplotlib.
    
    """
    if start_date.__contains__("."):
        start_date = format_time(start_date)
    
    if limit.__contains__("."):
        limit = format_time(limit)
        data = get_time_data_between(stations_id, field_name, limit, start_date)
    else:
        data = get_time_data(stations_id, field_name, limit, start_date)
    if not data:
        print("No data found for plotting.")
        return
    
    print("finished query of data.")

    dates = []
    values = []
    
    for item in data:
        d = format_time(item[1])
        v = float(item[2])
        #print(d, v)
        dates.append(d)
        values.append(v)

    station_id = data[0][0] if data else "All"

    plt.figure(figsize=(12, 6))
    plt.plot(dates, values, marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel(field_name)
    plt.title(f"{field_name} over Time for Station {station_id}")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_average_over_time(stations_id, field_name, start_date, end_date):
    """
    Retrieves time series data and plots it using matplotlib.
    
    """
    start_date = int(start_date)
    
    data = get_averages(stations_id, field_name, start_date, int(end_date)-int(start_date)+1)
    if not data:
        print("No data found for plotting.")
        return

    dates = []
    values = []
    
    for item in data:
        if item[0] is None:
            continue
        dates.append(start_date)
        values.append(float(item[0]))
        start_date += 1

    plt.figure(figsize=(12, 6))
    plt.plot(dates, values, marker='o', linestyle='-')
    plt.xlabel("Date")
    plt.ylabel(field_name)
    plt.title(f"{field_name} over Time for Station {stations_id}")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

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
    collumn = input("Wich data?: ").upper()
    if collumn not in ["QN_3", "FM", "FX", "QN_4", "RSK", "RSKF", "SDK", "SHK_TAG", "NM", "VPM", "PM", "TMK", "UPM", "TXK", "TNK", "TGK"]:
        print("not valid data field name.")
    else:   
        print("""
            Querys:
            1 - data with date with limit
            2 - data with date between dates
            3 - Yearly averages
            """)

        query_id = int(input("Query: "))

        if query_id == 1:
            print("Dates as DD.MM.YYYY")
            start_date = input("Start date: ")
            limit = input("Limit: ")
            print(f"Get {collumn} from station {station} with limit {limit} stating at {start_date}")
            plot_time_data(station, collumn, limit, start_date)
        elif query_id == 2:
            print("Dates as DD.MM.YYYY")
            start_date = input("Start date: ")
            end_date = input("End date: ")
            print(f"Get {collumn} between {start_date} and {end_date} fromstation {station}")
            plot_time_data(station, collumn, start_date, end_date)
        elif query_id == 3:
            print(f"Get yearly averages from station {station} for {collumn}")
            try:
                start = int(input("Start Year: "))
                end = int(input("End Year: "))
                plot_average_over_time(station, collumn, start, end)
            except:
                print("only give yearly numbers, eg.: 2001")