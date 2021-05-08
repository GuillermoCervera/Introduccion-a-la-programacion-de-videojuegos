import pygame
from enum import Enum

from shmup.states.state import State
from shmup.assets.assetmanager import AssetManager, AssetType
from shmup.ui.label import UILabel
from shmup.ui.label_clickable import UILabelClickable
from shmup.config import Config

class Actions(Enum):
    Next_Level = 0

class Intro(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GamePlay"

        center = [x/2 for x in Config.screen_size]
        font = AssetManager.instance().get(AssetType.Font, Config.font_name)

        self.__button = UILabelClickable(center, font, "Click Here To Start Game", (120, 120, 190), (200, 200, 250), action = Actions.Next_Level)
        self.__label =  UILabel((center[0], 100), font, "ShMUp Game, A Student's VIU Project", (200, 50, 50))

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_input(self, event):
        if self.__button.handle_input(event) == Actions.Next_Level:
            self.done = True

    def update(self, delta_time):
        pass

    def render(self, surface):
        self.__button.render(surface)
        self.__label.render(surface)