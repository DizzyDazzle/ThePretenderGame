import pygame as pgk
import pygame
from constants import *
import missparker


class Jarod():
    def __init__(self):
        self.img = pygame.image.load("Blank head.png")
        self.img = pygame.transform.scale(self.img, (BLOCKSIZE, BLOCKSIZE))
        self.rect = pygame.Rect(250, 250, BLOCKSIZE, BLOCKSIZE)
        #print(self.rect)       #
        self.radius = 32
        self.xspeed = 5
        self.yspeed = 5
        self.speed = 10
        #self.player_score = 0
        #self.cpu_score = 0
        #self.reset()

    def update(self, object):
        self.movement()
        self.check_collision(object)

    def movement(self):          #tells Jarod to update and do math of movements checks for collisons
        keys = pgk.key.get_pressed()

        if keys[pgk.K_UP]:
            if self.rect.y > 0:  # top is self.rect.y, tells player it cannot go past 0 (top of screen)
                self.rect.y -= self.speed  # if it hits the paddle move in opposite direction

        if keys[pgk.K_DOWN]:
            if self.rect.y + self.rect.height < GAME_HEIGHT:  # paddle can't go past bottom
                self.rect.y += self.speed

        if keys[pgk.K_RIGHT]:
            if self.rect.right < GAME_WIDTH:
                self.rect.right += self.speed

        if keys[pgk.K_LEFT]:
            if self.rect.left > 0:  # jarod can't go past left
                self.rect.left -= self.speed

    def check_collision(self, objects):
        for object in objects:

             if self.rect.colliderect(object.rect):
                #self.rect.right = object.rect.left
                if self.rect.x > object.rect.x :
                    self.rect.left = object.rect.right
                if self.rect.x < object.rect.x:
                    self.rect.right = object.rect.left
                if self.rect.y < object.rect.y :
                    self.rect.bottom = object.rect.top
                if self.rect.y > object.rect.y :
                    self.rect.top = object.rect.bottom


        #self.check_collision(missparker)


    #def check_collision(self, missparker):
        #if self.rect.colliderect(missparker.rect):

            #ball.reverse()

    def draw(self, surface):
        surface.blit(self.img, (self.rect.x, self. rect.y))
        #pygame.draw.circle(surface, WHITE,(self.rect.x + BLOCKSIZE // 2, self.rect.y + BLOCKSIZE // 2), self.radius)
        #pygame.draw.rect(surface, (0, 0, 255), self.rect)