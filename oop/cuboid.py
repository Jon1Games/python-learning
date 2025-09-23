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