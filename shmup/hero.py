import pygame

import os

from shmup.config import Config

class Hero:
    def __init__(self, window_size):
        self.__image = pygame.image.load(os.path.join(*Config.hero_filename)).convert_alpha()        

        self.__is_moving_up = False
        self.__is_moving_right = False
        self.__is_moving_down = False
        self.__is_moving_left = False

        self.__position = pygame.math.Vector2(window_size[0]/2 - self.__image.get_width()/2, window_size[1] - self.__image.get_height())        

    def handle_input(self, pressed, key):
        if key == pygame.K_UP:
            self.__is_moving_up = pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = pressed

    def update(self, delta):
        move = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            move.y -= Config.hero_speed
        if self.__is_moving_right:
            move.x += Config.hero_speed
        if self.__is_moving_down:
            move.y += Config.hero_speed
        if self.__is_moving_left:
            move.x -= Config.hero_speed

        self.__position += move * delta

    def render(self, dest):
        dest.blit(self.__image, self.__position.xy)

    def release(self):
        pass