import pygame

from shmup.world import World
from shmup.states.state import State

class GamePlay(State):
    def __init__(self):
        super().__init__()
        self.next_state = ""
        self.__world = World()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.__world.handle_input(event.key, True)
        if event.type == pygame.KEYUP:
            self.__world.handle_input(event.key, False)

    def update(self, delta_time):
        self.__world.update(delta_time)

    def render(self, surface):
        self.__world.render(surface)

    def enter(self):
        pass

    def exit(self):
        pass
