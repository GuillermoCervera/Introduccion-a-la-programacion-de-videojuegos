from shmup.assets.sound_manager import Soundmanager
from shmup.entities.rendergroup import RenderGroup
from shmup.entities.projectile import Projectile
from shmup.config import Config
from shmup.entities.hero import Hero

class World:

    def __init__(self):
        self.__players = RenderGroup(Hero(Config.screen_size, self))
        self.__allied_bullets = RenderGroup()

    def handle_input(self, key, pressed):
        for gameobject in self.__players:
            gameobject.handle_input(key, pressed) 

    def update(self, delta_time):
        self.__players.update(delta_time)
        self.__allied_bullets.update(delta_time)

    def render(self, surface):
        self.__players.draw(surface)
        self.__allied_bullets.draw(surface)

    def spawn_allied_bullet(self, projectile_type, position, velocity):
        self.__allied_bullets.add(Projectile(projectile_type, position, velocity))
        Soundmanager.instance().play_sound(Config.gunfire_name)