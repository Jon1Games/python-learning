import sqlite3
from datetime import datetime

db_name = "weather_data.db"

def get_time_data(stations_id, field_name, limit):
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

    cursor.execute(f"SELECT MESS_DATUM, {field_name} FROM produkt_klima_tag  WHERE STATIONS_ID = '{stations_id}' limit {limit};")
    data = cursor.fetchall()

    conn.close()
    return data

def get_time_data_between(stations_id, field_name, start_date, end_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT MESS_DATUM, {field_name} FROM produkt_klima_tag  WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM BETWEEN {start_date} and {end_date};")
    data = cursor.fetchall()

    conn.close()
    return data

def get_averages(stations_id, field_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag  WHERE STATIONS_ID = '{stations_id}';")
    data = cursor.fetchall()

    conn.close()
    return data[0][0]

def get_averages_between(stations_id, field_name, start_date, end_date):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(f"SELECT AVG({field_name}) FROM produkt_klima_tag  WHERE STATIONS_ID = '{stations_id}' AND MESS_DATUM between {start_date} and {end_date};")
    data = cursor.fetchall()

    conn.close()
    return data[0][0]

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

print("all from station 1 with limit 5")
data = get_time_data(1, "NM", 5)
for set in data:
    print(f"{format_time(set[0])}: {set[1]}")
    
print("All between 01.01.1937 and 12.01.1937 fromstation 1")
data_between = get_time_data_between(1, "NM", format_time("01.01.1937"), format_time("12.01.1937"))
for set in data:
    print(f"{format_time(set[0])}: {set[1]}")

print("Averages all form station 1")
print(get_averages(1, "NM"))

print("Averages between 01.01.1937 and 12.01.1937 from station 1")
print(get_averages_between(1, "NM", format_time("01.01.1937"), format_time("12.01.1937")))