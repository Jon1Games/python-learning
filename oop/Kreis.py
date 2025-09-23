import math

class Kreis:
    def __init__(self, radius: float, farbe: str = "blau"):
        self.radius = radius
        self.farbe = farbe
        
    def get_radius(self):
        return self.radius
    
    def berechne_flaeche(self):
        return math.pi * self.radius ** 2
    
    def berechne_umfang(self):
        return 2 * math.pi * self.radius
    
# Beispielobjekt
radius1 = float(input("Radius des Kreises: "))
radius2 = float(input("Radius des zweiten Kreises: "))
radius3 = float(input("Radius des dritten Kreises: "))
kreis1 = Kreis(radius1)
kreis2 = Kreis(radius2, "rot")
kreis3 = Kreis(radius3)

print(f"Kreis 1 - Radius: {kreis1.get_radius()}, Fläche: {kreis1.berechne_flaeche():.2f}, Umfang: {kreis1.berechne_umfang():.2f}, Farbe: {kreis1.farbe}")
print(f"Kreis 2 - Radius: {kreis2.get_radius()}, Fläche: {kreis2.berechne_flaeche():.2f}, Umfang: {kreis2.berechne_umfang():.2f}, Farbe: {kreis2.farbe}")
print(f"Kreis 3 - Radius: {kreis3.get_radius()}, Fläche: {kreis3.berechne_flaeche():.2f}, Umfang: {kreis3.berechne_umfang():.2f}, Farbe: {kreis3.farbe}")