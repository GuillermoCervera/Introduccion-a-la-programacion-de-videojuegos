import pygame

import os

from shmup.config import Config
from shmup.assets.assetmanager import AssetManager, AssetType
from shmup.entities.gameobject import GameObject
from shmup.entities.projectile import ProjectileType

class Hero(GameObject):
    def __init__(self, window_size, world):
        super().__init__()
        self.__is_moving_up = False
        self.__is_moving_right = False
        self.__is_moving_down = False
        self.__is_moving_left = False

        _, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.hero_name, sheet_name = Config.entities_name)
        self.position = pygame.math.Vector2(window_size[0]/2, window_size[1] - window_size[1]/5)
        self.rect = clip.copy()
        self.rect.inflate_ip(-self.rect.width * 0.60, -self.rect.height * 0.2)

        self.render_rect = clip.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = pressed
        elif key == pygame.K_SPACE:
            self.__fire_bullet()

    def update(self, delta):
        move = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            move.y -= Config.hero_speed
        if self.__is_moving_right:
            move.x += Config.hero_speed
        if self.__is_moving_down:
            move.y += Config.hero_speed
        if self.__is_moving_left:
            move.x -= Config.hero_speed

        self.position += move * delta
        self._center()

        #TODO Watch for screen limits

    def render(self, surface):
        hero_name = Config.hero_name
        if self.__is_moving_left:
            hero_name = Config.hero_left_name
        if self.__is_moving_right:
            hero_name = Config.hero_right_name
        if self.__is_moving_left and self.__is_moving_right:
            hero_name = Config.hero_name

        image, clip = AssetManager.instance().get(AssetType.SpriteSheet, hero_name, sheet_name = Config.entities_name)
        surface.blit(image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)

    def release(self):
        pass

    def __fire_bullet(self):
        self.__world.spawn_allied_bullet(ProjectileType.AlliedBullet, self.render_rect.midtop, pygame.math.Vector2(Config.allied_bullet_velocity))
