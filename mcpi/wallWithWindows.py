from mcpi.minecraft import Minecraft
from wall import Wall
from mcpi import block

class WallWithWindows(Wall):
    def __init__(self, pos: tuple, mc: Minecraft, height: int = 5, width: int = 6, rotated: bool = False, material_id: int = block.STONE.id, windows_material_id: int = block.GLASS.id):
        super().__init__(pos, mc, height, width, rotated, material_id)
        self.windows_material_id = windows_material_id
        
    def build(self):
        x, y, z = self.pos
        if self.rotated:
            # Build the wall with windows
            for i in range(self.width):
                for j in range(self.height):
                    if (i != 1 and i != self.width-1) and (j == 2 or j == 3):
                        self.bw.setBlock(x + i, y + j, z, self.windows_material_id)
                    else:
                        self.bw.setBlock(x + i, y + j, z, self.material_id)
        else:
            # Build the wall with windows
            for i in range(self.width):
                for j in range(self.height):
                    if (i != 1 and i != self.width-1) and (j == 2 or j == 3):
                        self.bw.setBlock(x, y + j, z + i, self.windows_material_id)
                    else:
                        self.bw.setBlock(x, y + j, z + i, self.material_id)