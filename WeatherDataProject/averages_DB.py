import sqlite3
from datetime import datetime

db_name = "weather_data.db"

def get_station_id(station_name):
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT Stations_id FROM Metadaten_Geographie WHERE Stationsname=?", (station_name,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None

def format_date(init_date):
    date_object = datetime.strptime(str(init_date), '%Y%m%d').date()
    return date_object

def get_average(field_name):
    pass
    # TODO: function to get input wich field shod be read (Outpit of options with meaning)
    # also read time and format and print


station_input = input("Enter station name or ID: ")
try: 
    station_id = int(station_input)
except:
    station_id = get_station_id(station_input)

print(station_id)