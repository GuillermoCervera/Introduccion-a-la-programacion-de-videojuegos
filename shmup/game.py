#!/usr/bin/env python3

import pygame
import os

from shmup.fpsstats import FPSStats
from shmup.config import Config
from shmup.hero import Hero
from shmup.sound_manager import Soundmanager

class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.init()

        self.__screen = pygame.display.set_mode(Config.screen_size,0,32)
        pygame.display.set_caption(Config.game_title)

        self.__hero = Hero(self.__screen.get_size())

        self.__font = pygame.font.Font(os.path.join(*Config.font_filename), Config.font_fps_size)
        self.__fps_stats = FPSStats(self.__font)

        self.__load_sounds()

        self.__running = False

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
                self.__hero.handle_input(True, event.key)
            if event.type == pygame.KEYUP:
                self.__hero.handle_input(False, event.key)

    def __update(self, delta):
        self.__hero.update(delta)
        Soundmanager.instance().update(delta)

    def __render(self):
        self.__screen.fill(Config.background_color)
        self.__hero.render(self.__screen)
        self.__fps_stats.render_stats(self.__screen)
        pygame.display.update()

    def __quit(self):
        self.__hero.release()
        pygame.quit()

    def __calc_delta(self, last):
        current = pygame.time.get_ticks()
        delta = current - last
        return delta, current

    def __load_sounds(self):
        Soundmanager.instance().add_sound(Config.gunfire_filename, "gunfire")
        Soundmanager.instance().add_music(Config.theme_filename, "mission_theme")