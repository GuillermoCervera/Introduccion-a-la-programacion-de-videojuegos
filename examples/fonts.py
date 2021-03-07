import pygame
from pygame.locals import *
import os

SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

my_font = pygame.font.SysFont("arial", 16)
text = my_font.render("Hello World!!!", True, (0,0,0), (255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))

    screen.blit(text, (screen.get_width()/2 - text.get_width()/2, screen.get_height()/2 - text.get_width()/2))
        
    pygame.display.update()

pygame.quit()