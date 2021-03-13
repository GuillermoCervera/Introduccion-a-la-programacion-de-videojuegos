#!/usr/bin/env python3

import pygame
import os

from shmup.fpsstats import FPSStats
from shmup.config import Config

class Game:

    def __init__(self):
        pygame.init()

        self.__screen = pygame.display.set_mode(Config.screen_size,0,32)
        pygame.display.set_caption(Config.game_title)

        self.__hero = pygame.image.load(os.path.join(*Config.hero_filename)).convert_alpha()
        self.__running = False

        self.__is_moving_up = False
        self.__is_moving_right = False
        self.__is_moving_down = False
        self.__is_moving_left = False

        self.__hero_position = pygame.math.Vector2(self.__screen.get_width()/2 - self.__hero.get_width()/2, self.__screen.get_height() - self.__hero.get_height())        
        self.__font = pygame.font.Font(os.path.join(*Config.font_filename), Config.font_fps_size)

        self.__fps_stats = FPSStats(self.__font)

    def run(self):       
        self.__running = True

        last = pygame.time.get_ticks()
        time_since_last_update = 0
        while self.__running:
            delta, last = self.__calc_delta(last)

            time_since_last_update += delta
            while time_since_last_update > Config.time_per_frame:
                time_since_last_update -= Config.time_per_frame

                self.__process_events()
                self.__update(Config.time_per_frame)
                self.__fps_stats.update_logic(Config.time_per_frame)

            self.__render()   
            self.__fps_stats.update_render()         
        
        self.__quit()        

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                self.__player_controller(True, event.key)
            if event.type == pygame.KEYUP:
                self.__player_controller(False, event.key)


    def __update(self, delta):
        move = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            move.y -= Config.hero_speed
        if self.__is_moving_right:
            move.x += Config.hero_speed
        if self.__is_moving_down:
            move.y += Config.hero_speed
        if self.__is_moving_left:
            move.x -= Config.hero_speed

        self.__hero_position += move * delta

    def __render(self):
        self.__screen.fill(Config.background_color)

        self.__screen.blit(self.__hero, self.__hero_position.xy)

        self.__fps_stats.render_stats(self.__screen)

        pygame.display.update()

    def __quit(self):
        pygame.quit()

    def __player_controller(self, pressed, key):
        if key == pygame.K_UP:
            self.__is_moving_up = pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = pressed

    def __calc_delta(self, last):
        current = pygame.time.get_ticks()
        delta = current - last
        return delta, current