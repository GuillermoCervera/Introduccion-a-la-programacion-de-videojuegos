from enum import Enum
import pygame
from os import path

from shmup.assets.spritesheet import SpriteSheet

class AssetType(Enum):
    Image = 0,
    SpriteSheet = 1, 
    Font = 2,
    Sound = 3,
    Music = 4

class AssetManager:

    _instance = None

    @staticmethod
    def instance():
        if AssetManager._instance is None:
            AssetManager()
        return AssetManager._instance

    def __init__(self):
        if AssetManager._instance is None:
            AssetManager._instance = self

            self.__assets = {}
        else:
            raise exception("AssetManager is a singleton")

    def load(self, asset_type, asset_name, asset_filename, data_filename = None, size = 0):
        asset_filename_path = path.join(*asset_filename)

        if asset_name not in self.__assets and path.isfile(asset_filename_path):
            if asset_type == AssetType.Image:
                self.__assets[asset_name] = pygame.image.load(asset_filename_path).convert_alpha()
            elif asset_type == AssetType.SpriteSheet:
                self.__assets[asset_name] = SpriteSheet(asset_filename, data_filename)
            elif asset_type == AssetType.Font:
                self.__assets[asset_name] = pygame.font.Font(asset_filename_path, size)
            elif asset_type == AssetType.Sound:
                self.__assets[asset_name] = pygame.mixer.Sound(asset_filename_path)
            elif asset_type == AssetType.Music:
                self.__assets[asset_name] = asset_filename_path
        return

    def get(self, asset_type, asset_name, sheet_name = None):
        if asset_type == AssetType.SpriteSheet:
            if sheet_name in self.__assets:
                return self.__assets[sheet_name].get_image(asset_name)
            return None, pygame.Rect(0,0,0,0)
        elif asset_type == AssetType.Image:
            if asset_name in self.__assets:
                return self.__assets[asset_name], self.__assets[asset_name].get_rect()
            return None, pygame.Rect(0,0,0,0)
        else:
            if asset_name in self.__assets:
                return self.__assets[asset_name]
            return None