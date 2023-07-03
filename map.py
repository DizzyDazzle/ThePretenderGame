import block
from constants import *


class Map():
    def __init__(self):
        self.blocks = []

    def load_map(self) :
        x, y = 0, 0
        with open("maps.txt") as file:
            for line in file :
                #print(line)
                for l in line:
                    print(f"x:{x}, y{y}")
                    if l == "1":
                        self.blocks.append(block.Block(x * BLOCKSIZE // 2, y * BLOCKSIZE // 2))
                    x += 1

                y += 1
                x = 0

    def draw(self, surface):
        for block in self.blocks:
            block.draw(surface)



