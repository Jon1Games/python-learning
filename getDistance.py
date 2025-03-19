import math

def haversine(lat1, lon1, lat2, lon2):
    # Radius der Erde in Kilometern
    R = 6371.0
    
    # Konvertiere Grad in Radianten
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    # Haversine-Formel
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Entfernung in Kilometern
    distance = R * c
    return distance

# Standardwerte (Wohnort und Geburtsort)
wohnort_lat = 
wohnort_lon = 
geburtsort_lat = 
geburtsort_lon = 

# Überschreiben?
if input("use deault? [y/n]: ") == "y":
    wohnort_lat = input(wohnort_lat)
    wohnort_lon = input(wohnort_lon)
    geburtsort_lat = input(geburtsort_lat)
    geburtsort_lon = input(geburtsort_lon)


# Berechne den Abstand
distance = haversine(wohnort_lat, wohnort_lon, geburtsort_lat, geburtsort_lon)
print(f"Der Abstand zwischen Wohnort und Geburtsort beträgt {distance:.2f} Kilometer.")