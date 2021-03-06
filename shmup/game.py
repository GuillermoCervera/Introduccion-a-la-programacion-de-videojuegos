import pygame
import os

class Game:

    hero_filename = ["shmup", "assets", "images", "hero.png"]

    def __init__(self):
        pass

    def run(self):
        pygame.init()

        screen = pygame.display.set_mode((640,480),0,32)
        pygame.display.set_caption("Hello World")

        hero = pygame.image.load(os.path.join(*Game.hero_filename)).convert_alpha()

        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0,0,0,0))

            x,y = pygame.mouse.get_pos()
            screen.blit(hero, (x - hero.get_width()/2,y - hero.get_height()/2))

            pygame.display.update()

        pygame.quit()