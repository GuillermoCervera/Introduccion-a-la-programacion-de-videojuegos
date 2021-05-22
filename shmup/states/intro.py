import pygame
from enum import Enum

from shmup.states.state import State
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.ui.label import UILabel
from shmup.ui.label_clickable import UILabelClickable
from shmup.config import Config

class Actions(Enum):
    Next_Level = 0

class Intro(State):

    def __init__(self):
        super().__init__()
        self.next_state = "GamePlay"

        font = AssetManager.instance().get(AssetType.Font, Config.font_name)
        center_position = [x/2 for x in Config.screen_size]
        self.__button = UILabelClickable(center_position, font, "Click To Start The Game", (140, 140, 190), (200, 200, 250), action = Actions.Next_Level)
        self.__label = UILabel((center_position[0], 100), font, "ShMup Game A VIU Project", (200, 60, 60))

    def enter(self):
        self.done = False

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
