from pasing_to_DB import parsing_to_database
from querys_DB import query
import os

def start():
    print("""
        1 - Fill database
        2 - Do querrys
        """)

    inp = input("Type what you want to do: ")
    
    try:
        inp = int(inp)
    except:
        print("Please only give a number")
        exit()
        
    if inp == 1:
        if os.path.exists("weather_data.db"):
            inp = input("Data is already stored, du you want to overwrite? [y/n]: ")
            if inp.lower == "y":
                os.remove("weather_data.db")
                parsing_to_database()
            else:
                print("Skip download of data.")
                print("")
    elif inp == 2:
        query()
    else:
        print("Pleaseo only give a number between(and including) 1 and 2.")
    
def restart():
    start()
    
start()