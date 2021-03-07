import pygame
from pygame.locals import *
import os

pygame.init()

screen = pygame.display.set_mode([640, 480], 0, 32)

circle = pygame.Surface((50,50))
pygame.draw.circle(circle, (60,139,210), (25, 25), 25)

full_screen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_f:
                full_screen = not full_screen
                if full_screen:
                    screen = pygame.display.set_mode([640, 480], FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode([640, 480], 0, 32) 

    screen.fill((0, 0, 0))

    screen.blit(circle, (screen.get_width()/2 - circle.get_width()/2, screen.get_height()/2 - circle.get_width()/2))
        
    pygame.display.update()

pygame.quit()