class Cuboid:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    
    def is_cube(self):
        return self.length == self.width == self.height
    
# Beispielobjekt
length = float(input("Länge des Quaders: "))
width = float(input("Breite des Quaders: "))
height = float(input("Höhe des Quaders: "))
cuboid1 = Cuboid(length, width, height)
print(f"Volumen: {cuboid1.volume()}")
print(f"Oberfläche: {cuboid1.surface_area()}")
print(f"Ist Würfel: {cuboid1.is_cube()}")