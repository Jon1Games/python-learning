from mcpi.minecraft import Minecraft
from wall import Wall
from mcpi import block

class WallWithDoor(Wall):
    def __init__(self, pos: tuple, mc: Minecraft, height: int = 5, width: int = 6, rotated: bool = False, material_id: int = block.STONE.id, door_material_id: int = block.AIR.id):
        super().__init__(pos, mc, height, width, rotated, material_id)
        self.door_material_id = door_material_id
        
    def build(self):
        x, y, z = self.pos
        if self.rotated:
            # Build the wall with doors
            for i in range(self.width):
                for j in range(self.height):
                    if ((i % 2 == 0 and (i == self.width // 2 or i == self.width // 2 - 1)) or (i % 2 == 1 and i == self.width // 2)) and (j == 1 or j == 2 or j == 3):
                        self.bw.setBlock(x + i, y + j, z, self.door_material_id)
                    else:
                        self.bw.setBlock(x + i, y + j, z, self.material_id)
        else:
            # Build the wall with doors
            for i in range(self.width):
                for j in range(self.height):
                    if ((i % 2 == 0 and (i == self.width // 2 or i == self.width // 2 - 1)) or (i % 2 == 1 and i == self.width // 2)) and (j == 1 or j == 2 or j == 3):
                        self.bw.setBlock(x, y + j, z + i, self.door_material_id)
                    else:
                        self.bw.setBlock(x, y + j, z + i, self.material_id)