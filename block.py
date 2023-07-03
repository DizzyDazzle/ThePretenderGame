import pygame
from constants import *


class Block():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCKSIZE // 2, BLOCKSIZE // 2)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

