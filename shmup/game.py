#!/usr/bin/env python3

import pygame
import os

from shmup.fpsstats import FPSStats
from shmup.config import Config
from shmup.assets.sound_manager import Soundmanager
from shmup.assets.assetmanager import AssetType, AssetManager
from shmup.states.statemanager import StateManager

class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.init()

        self.__screen = pygame.display.set_mode(Config.screen_size,0,32)
        pygame.display.set_caption(Config.game_title)

        self.__load_assets()
        self.__fps_stats = FPSStats()

        self.__state_manager = StateManager()

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
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                if event.key == pygame.K_F5:
                    Config.debug = not Config.debug
            self.__state_manager.handle_event(event)

    def __update(self, delta):
        self.__state_manager.update(delta)
        Soundmanager.instance().update(delta)

    def __render(self):
        self.__screen.fill(Config.background_color)
        self.__state_manager.render(self.__screen)
        if Config.debug:
            self.__fps_stats.render_stats(self.__screen)
        pygame.display.update()

    def __quit(self):
        pygame.quit()

    def __calc_delta(self, last):
        current = pygame.time.get_ticks()
        delta = current - last
        return delta, current

    def __load_assets(self):
        AssetManager.instance().load(AssetType.SpriteSheet, Config.entities_name, Config.entities_filename, data_filename = Config.entities_data_filename)
        AssetManager.instance().load(AssetType.Font, Config.font_name, Config.font_filename, size = Config.font_fps_size)

        AssetManager.instance().load(AssetType.Sound, Config.gunfire_name, Config.gunfire_filename)
        AssetManager.instance().load(AssetType.Music, Config.theme_name, Config.theme_filename)