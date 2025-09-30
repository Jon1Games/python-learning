from mcpi.minecraft import Minecraft
from mcpi import block

class Wall:
    def __init__(self, pos: tuple, mc: Minecraft, height: int = 5, width: int = 6, rotated: bool = False, material_id: int = block.STONE.id):
        self.height = height
        self.width = width
        self.pos = pos
        self.rotated = rotated
        self.material_id = material_id
        self.mc = mc

    def build(self):
        x, y, z = self.pos
        if self.rotated:
            self.mc.setBlocks(x, y, z, x + self.width - 1, y + self.height - 1, z, self.material_id)
        else:
            self.mc.setBlocks(x, y, z, x, y + self.height - 1, z + self.width - 1, self.material_id)