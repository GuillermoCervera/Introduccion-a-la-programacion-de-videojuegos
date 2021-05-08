import pygame
from enum import Enum

from shmup.entities.gameobject import GameObject
from shmup.assets.assetmanager import AssetManager, AssetType
from shmup.config import Config

class ProjectileType(Enum):
    AlliedBullet = 0,
    EnemyBullet = 1,
    Missile = 2

class Projectile(GameObject):

    def __init__(self, projectile_type, position, velocity):
        super().__init__()

        self.__type = projectile_type
        self.position = pygame.math.Vector2(position)
        self.__velocity = velocity

        if self.__type == ProjectileType.AlliedBullet:
            _, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.allied_bullet_name, sheet_name = Config.entities_name)

        self.rect = clip.copy()
        self.render_rect = clip.copy()
        self._center()

    def update(self, delta):
        if self.__type == ProjectileType.AlliedBullet or self.__type == ProjectileType.EnemyBullet:
            self.position += self.__velocity * delta

        self._center()

        if self.position.y < (0 - self.render_rect.height):
            self.kill()

    def render(self, surface):
        if self.__type == ProjectileType.AlliedBullet:
            image, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.allied_bullet_name, sheet_name = Config.entities_name)
        
        surface.blit(image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)