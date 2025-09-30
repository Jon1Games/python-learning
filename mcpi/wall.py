from mcpi import World

class Wall:
    def __init__(self, pos: tuple, bw: World, height: int = 5, width: int = 6, rotated: bool = False, material_id: str = "minecraft:stone"):
        self.height = height
        self.width = width
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.bw = bw
        
    def build(self):
        x, y, z = self.pos
        if self.rotated:
            self.bw.setBlocks(x, y, z, x + self.width - 1, y + self.height - 1, z, self.material_id)
        else:
            self.bw.setBlocks(x, y, z, x, y + self.height - 1, z + self.width - 1, self.material_id)