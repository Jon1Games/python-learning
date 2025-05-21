import os
import sqlite3
import shutil
import time
import zipfile
import requests
import csv
from bs4 import BeautifulSoup

class WetherData():
    def __init__(self, url):
        self.url = url
        
    # download with os.path.exist
    # informative output
    
    # queries -> inp what tp query
    
    # 
    
def example():
    weather = WetherData("https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/kl/historical/")
    # input for what to start
    
print(example())