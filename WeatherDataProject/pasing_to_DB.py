import requests
import zipfile
import csv
import os
import sqlite3
import shutil
from bs4 import BeautifulSoup
import time

url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

files = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href.endswith('.zip'):
        files.append(url + href)

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('weather_data.db')
c = conn.cursor()

for file in files:
    # Download the file
    response = requests.get(file)
    with open("temp.zip", "wb") as f:
        f.write(response.content)

    # Extract the file
    with zipfile.ZipFile("temp.zip", "r") as zip_ref:
        zip_ref.extractall(".extracted_files")

    # Remove every thinh exept station infos and prod clima data
    for filename in os.listdir(".extracted_files"):
        if not filename.startswith("produkt") and not filename.startswith("Metadaten_Geographie"):
            os.remove(os.path.join(".extracted_files", filename))
            
            
    # Process each txt file in the .extracted_files directory
    for txt_file in [f for f in os.listdir(".extracted_files") if f.endswith(".txt")]:
        print("Processing file: " + txt_file)
        # Read the CSV file to get the headers
        with open(os.path.join(".extracted_files", txt_file), newline='', encoding='latin1') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            headers = next(reader)
            data = list(reader)
        
        # Create table with the name of the file (without extension and numbers) and columns from CSV headers
        table_name = ''.join([i for i in os.path.splitext(txt_file)[0] if not i.isdigit()]).rstrip('_')
        columns = ", ".join([f'"{header}" TEXT' for header in headers])
        c.execute(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns})')
        
        # Insert data into the table
        placeholders = ', '.join(['?'] * len(headers))
        insert_query = f'INSERT INTO "{table_name}" VALUES ({placeholders})'
        
        # Execute the query for each row of data
        for row in data:
            try:
                c.execute(insert_query, row)
            except sqlite3.ProgrammingError as e:
                # ignore as it will be invalid lines like legend or credits
                continue

    # Remove the temporary zip file and folder
    os.remove("temp.zip")
    shutil.rmtree(".extracted_files")

    # Commit changes
    conn.commit()

    time.sleep(1.5)    

# Close the connection
conn.close()
