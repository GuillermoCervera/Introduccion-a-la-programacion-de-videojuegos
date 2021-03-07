import pygame
from pygame.locals import *
import os

SCREEN_SIZE = (640, 480)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)

circle = pygame.Surface((50,50))
pygame.draw.circle(circle, (60,139,210), (25, 25), 25)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == VIDEORESIZE:
            SCREEN_SIZE = event.size
            screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
            print(f'Window Resized to {event.size}')

    screen.fill((0, 0, 0))

    screen.blit(circle, (screen.get_width()/2 - circle.get_width()/2, screen.get_height()/2 - circle.get_width()/2))
        
    pygame.display.update()

pygame.quit()
