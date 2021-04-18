import pygame
from os import path

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

            self.__sounds = {}
            self.__music = {}

            self.__sound_volume = 1.0
            self.__music_volume = 1.0

            self.__current_music = None
            self.__next_music = None

        else:
            raise exception("Soundmanager is a singleton")


    def add_sound(self, filename, name):
        self.__sounds[name] = pygame.mixer.Sound(path.join(*filename))

    def add_music(self, filename, name):
        self.__music[name] = filename

    def play_sound(self, name):
        if name not in self.__sounds:
            return 

        self.__sounds[name].set_volume(self.__sound_volume)
        self.__sounds[name].play()

    def play_music(self, name):
        if name not in self.__music and name is self.__current_music:
            return 

        pygame.mixer.music.load(self.__music[name])
        pygame.mixer.music.set_volume(self.__music_volume)
        self.__current_music = name
        pygame.mixer.music.play(-1)

    def play_music_fade(self, name):
        if name not in self.__music and name is self.__current_music:
            return 
        
        self.__next_music = name
        pygame.mixer.music.fadeout(500)

    def update(self, delta):
        if self.__next_music is not None and not pygame.mixer.music.get_busy():
            self.play_music(self.__next_music)
            self.__current_music = self.__next_music
            self.__next_music = None
