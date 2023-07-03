import pygame
import random
from constants import *

class Missparker():
    def __init__(self):
        self.rect = pygame.Rect(600, 600, BLOCKSIZE, BLOCKSIZE)
        self.speed = 3
        self.radius = 32
        #self.player_score = 0
        #self.cpu_score = 0
        #self.reset()

    def chase(self, jarod):
        jr = jarod.rect         #jr means Jarod's rectangle; where is Jarod? Gives coordinates

        #     else:
        #         if self.rect.bottom < GAME_HEIGHT:
        #             self.rect.y += self.speed
        if jr.right > self.rect.right :
            self.rect.x += self.speed  #goes right
        #Get to Jarod as quickly as possible, if Jarods coordinates are bigger add speed to Miss parker's coordinates

        if jr.left < self.rect.left:
            self.rect.left -= self.speed        #goes left

        if jr.top < self.rect.top:              #goes up
            if self.rect.top > 0:
                self.rect.top -= self.speed

        else:                                   #goes down
            if jr.bottom > self.rect.bottom :
                if self.rect.bottom < GAME_HEIGHT:
                    self.rect.bottom += self.speed


    def update(self, jarod):           #tells missparker to update and do math of movements checks for collisons
        #print("missparker update")     #used to tell me if it works
        self.chase(jarod)
        #self.check_collision(jarod)

    def draw(self, surface):
        pygame.draw.circle(surface, BLACK,(self.rect.x + BLOCKSIZE // 2, self.rect.y + BLOCKSIZE // 2), self.radius)
