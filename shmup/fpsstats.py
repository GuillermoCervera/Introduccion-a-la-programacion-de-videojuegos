#!/usr/bin/env python3

import pygame

from shmup.config import Config
from shmup.assets.assetmanager import AssetManager, AssetType

class FPSStats:

    def __init__(self):
        self.__render_fps = 0
        self.__logic_fps = 0
        self.__update_time = 0
        self.__update_fps()

    def update_render(self):
        self.__render_fps += 1

    def update_logic(self, delta):
        self.__logic_fps +=1
        self.__update_time += delta

        if self.__update_time >= Config.refresh_time:
            self.__update_fps()

            self.__update_time -= Config.refresh_time
            self.__render_fps = 0
            self.__logic_fps = 0

    def __update_fps(self):
        font  = AssetManager.instance().get(AssetType.Font, Config.font_name)
        self.__fps = font.render(f"Logic {self.__logic_fps} fps  Render {self.__render_fps} fps", True, Config.fps_foreground_color, Config.fps_background_color)

    def render_stats(self, screen):
        screen.blit(self.__fps, (0,0))