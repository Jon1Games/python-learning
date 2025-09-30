from mcpi import World
from wall import Wall

class WallWithWindows(Wall):
    def __init__(self, pos: tuple, bw: World, height: int = 5, width: int = 6, rotated: bool = False, material_id: str = "minecraft:stone", windows_material_id: str = "minecraft:air"):
        super().__init__(pos, bw, height, width, rotated, material_id)
        self.windows_material_id = windows_material_id
        
    def build(self):
        x, y, z = self.pos
        if self.rotated:
            # Build the wall with windows
            for i in range(self.width):
                for j in range(self.height):
                    if (i % 3 == 1) and (j % 3 == 1):
                        self.bw.setBlock(x + i, y + j, z, self.windows_material_id)
                    else:
                        self.bw.setBlock(x + i, y + j, z, self.material_id)
        else:
            # Build the wall with windows
            for i in range(self.width):
                for j in range(self.height):
                    if (i % 3 == 1) and (j % 3 == 1):
                        self.bw.setBlock(x, y + j, z + i, self.windows_material_id)
                    else:
                        self.bw.setBlock(x, y + j, z + i, self.material_id)