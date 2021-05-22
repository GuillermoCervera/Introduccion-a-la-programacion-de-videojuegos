#!/usr/bin/env python3

import pygame

from shmup.config import Config
from shmup.fps_stats import FPSStats
from shmup.assets.sound_manager import SoundManager
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.states.state_manager import StateManager

class Game:

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 4096)
        pygame.init()

        self.__window = pygame.display.set_mode(Config.screen_size, 0, 32)
        pygame.display.set_caption(Config.game_title)

        self.__load_assets()

        self.__running = False
        self.__fps_stats = FPSStats()

        self.__state_manager = StateManager()

    def run(self):
        self.__running = True

        last_time = pygame.time.get_ticks()
        time_since_last_update = 0
        while self.__running:
            delta_time, last_time = self.__calc_delta_time(last_time)
            time_since_last_update += delta_time
            while time_since_last_update > Config.time_per_frame:
                time_since_last_update -= Config.time_per_frame

                self.__process_events()
                self.__update(Config.time_per_frame)

                self.__fps_stats.update_logic(Config.time_per_frame)

            self.__fps_stats.update_render()
            self.__render()

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

    def __update(self, delta_time):
        self.__state_manager.update(delta_time)
        SoundManager.instance().update(delta_time)

    def __render(self):
        self.__window.fill(Config.background_color)
        self.__state_manager.render(self.__window)

        if Config.debug:
            self.__fps_stats.render_stats(self.__window)

        pygame.display.update()

    def __quit(self):
        self.__state_manager.quit()
        pygame.quit()

    def __calc_delta_time(self, last):
        current = pygame.time.get_ticks()
        delta = current - last
        return delta, current

    def __load_assets(self):  # TODO - Asset manager by states and one global
        AssetManager.instance().load(AssetType.SpriteSheet, Config.entities_name, Config.entities_image_filename, data_filename = Config.entities_data_filename)
        AssetManager.instance().load(AssetType.FlipBook, Config.explosion_name, Config.explosion_image_filename, rows = Config.explosion_size[0], cols = Config.explosion_size[1])
        AssetManager.instance().load(AssetType.Image, Config.jungle_name, Config.jungle_image_filename)
        AssetManager.instance().load(AssetType.Image, Config.clouds_name, Config.clouds_image_filename)
        AssetManager.instance().load(AssetType.Font, Config.font_name, Config.font_filename, font_size = 12)
        AssetManager.instance().load(AssetType.Sound, Config.allied_gunfire_name, Config.allied_gunfire_filename)
        AssetManager.instance().load(AssetType.Sound, Config.enemy_gunfire_name, Config.enemy_gunfire_filename)
        AssetManager.instance().load(AssetType.Sound, Config.explosion1_name, Config.explosion1_filename)
        AssetManager.instance().load(AssetType.Sound, Config.explosion2_name, Config.explosion2_filename)
        AssetManager.instance().load(AssetType.Music, Config.mission_theme_name, Config.mission_theme_filename)
        self.__load_asset_from_spritesheet(Config.enemy_raptor_name)
        self.__load_asset_from_spritesheet(Config.enemy_avenger_name)

    def __load_asset_from_spritesheet(self, name):
        sheet, clip = AssetManager.instance().get(AssetType.SpriteSheet, name, sheet_name = Config.entities_name)
        image = pygame.Surface(clip.size, depth = 32, flags = pygame.SRCALPHA)
        image.blit(sheet, pygame.Rect((0,0), clip.size), clip)
        AssetManager.instance().set(name, image)