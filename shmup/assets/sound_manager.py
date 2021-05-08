import pygame
from os import path

from shmup.assets.assetmanager import AssetType, AssetManager

class Soundmanager:

    _instance = None

    @staticmethod
    def instance():
        if Soundmanager._instance is None:
            Soundmanager()
        return Soundmanager._instance

    def __init__(self):
        if Soundmanager._instance is None:
            Soundmanager._instance = self

            self.__sound_volume = 1.0
            self.__music_volume = 1.0

            self.__current_music = None
            self.__next_music = None

        else:
            raise exception("Soundmanager is a singleton")


    def play_sound(self, name):
        sound = AssetManager.instance().get(AssetType.Sound, name)

        sound.set_volume(self.__sound_volume)
        sound.play()

    def play_music(self, name):
        if name is self.__current_music:
            return 

        music = AssetManager.instance().get(AssetType.Music, name)

        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(self.__music_volume)
        self.__current_music = name
        pygame.mixer.music.play(-1)

    def play_music_fade(self, name):
        if name is self.__current_music:
            return 
        
        self.__next_music = name
        pygame.mixer.music.fadeout(500)

    def update(self, delta):
        if self.__next_music is not None and not pygame.mixer.music.get_busy():
            self.play_music(self.__next_music)
            self.__current_music = self.__next_music
            self.__next_music = None
