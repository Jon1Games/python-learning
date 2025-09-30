from mcpi.minecraft import Minecraft
from mcpi import block
import time
from wall import Wall
from wallWithWindows import WallWithWindows

def pos(offset=(0,0,0)):
    player_pos = mc.player.getPos()
    return (int(player_pos.x) + offset[0], int(player_pos.y) + offset[1], int(player_pos.z) + offset[2])

# Verbinde mit Minecraft
mc = Minecraft.create(address="192.168.172.44", port=4711)

# Warte auf Tastendruck zum Fortfahren
while True:
    hits = mc.events.pollChatPosts()
    for hit in hits:
        if hit.message == "stop":
            mc.postToChat("Programm beendet!")
            exit()
        elif hit.message == "1":
            # Hole die aktuelle Position des Spielers
            x, y, z = pos((5,0,0))

            # Baue eine 3x4x5 Struktur aus verschiedenen Blöcken
            mc.setBlocks(x, y, z, x, y, z+3, block.DIRT.id)
            mc.setBlocks(x, y+1, z, x, y+3, z, block.COBBLESTONE.id)
            mc.setBlocks(x+1, y, z, x+3, y, z, block.STONE.id)

            # Sende eine Nachricht an den Spieler
            mc.postToChat("3x4x5 Blöcke platziert!")
        elif hit.message == "2":
            test = WallWithWindows(windows_material_id="minecraft:glass")
            pass
    time.sleep(0.1)