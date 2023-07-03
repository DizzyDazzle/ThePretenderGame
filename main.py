import pygame
import jarod
import missparker
import block
import map
from constants import *

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()           #tells pygame to start/starts game engine
jarod = jarod.Jarod()   #create an object called Jarod
missparker = missparker.Missparker()
block = block.Block(500, 500)
map = map.Map()
map.load_map()

def main():
    running = True

    while running:
        clock.tick(TICK_RATE)  # sets FPS (frames per second)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    board.reset()
                if event.key == pygame.K_q:
                    running = False
        draw()
        update()

    pygame.quit()


def draw():
    surface.fill(LYELLOW)  # erase the screen
    jarod.draw(surface)
    missparker.draw(surface)
    #block.draw(surface)            #Used to test
    map.draw(surface)
    #draw_court(surface)
    #draw_score(surface)

    pygame.display.flip()  # tells us to move onto the next frame


def update():
    jarod.update(map.blocks)
    #missparker.update(jarod)
    #cpu.update(ball)


if __name__ == "__main__":              #tells it to run the main function
    main()
