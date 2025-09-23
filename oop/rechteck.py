# Class Diagram für Rechteck:
# 
# ┌─────────────────────────────────┐
# │            Rechteck             │
# ├─────────────────────────────────┤
# │ + length: float                 │
# │ + width: float                  │
# ├─────────────────────────────────┤
# │ + __init__(length, width)       │
# │ + flaeche(): float              │
# │ + umfang(): float               │
# └─────────────────────────────────┘

class Rechteck:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def flaeche(self):
        return self.length * self.width

    def umfang(self):
        return 2 * (self.length + self.width)
    
# Beispielobjekt
rechtecke = []
for i in range(3):
    length = float(input(f"Länge des Rechtecks {i+1}: "))
    width = float(input(f"Breite des Rechtecks {i+1}: "))
    rechteck = Rechteck(length, width)
    rechtecke.append(rechteck)

for i, rechteck in enumerate(rechtecke):
    print(f"Rechteck {i+1} - Fläche: {rechteck.flaeche()}, Umfang: {rechteck.umfang()}")