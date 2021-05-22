import pygame

from shmup.config import Config
from shmup.assets.asset_manager import AssetManager, AssetType
from shmup.entities.gameobject import GameObject
from shmup.entities.projectile import ProjectileType

class Hero(GameObject):

    def __init__(self, world):
        super().__init__()
        self.__is_moving_up = False
        self.__is_moving_right = False
        self.__is_moving_down = False
        self.__is_moving_left = False
        self.__cool_down_time = 0.0

        _, clip = AssetManager.instance().get(AssetType.SpriteSheet, Config.hero_entity_name, sheet_name = Config.entities_name)

        self.position = pygame.math.Vector2(Config.screen_size[0]/2, Config.screen_size[1] - Config.screen_size[1]/3)
        self.rect = clip.copy()
        self.rect.inflate_ip(self.rect.width * -0.60, self.rect.height * -0.2)

        self.render_rect = clip.copy()

        self._center()

        self.__world = world

    def handle_input(self, key, is_pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        elif key == pygame.K_SPACE:
            if self.__cool_down_time <= 0.0:
                self.__fire_bullet()

    def update(self, delta):
        movement = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            movement.y -= Config.hero_speed
        if self.__is_moving_down:
            movement.y += Config.hero_speed
        if self.__is_moving_left:
            movement.x -= Config.hero_speed
        if self.__is_moving_right:
            movement.x += Config.hero_speed

        self.position += movement * delta
        self.check_bounds()
        self._center()

        if self.__cool_down_time > 0.0:
            self.__cool_down_time -= delta

    def render(self, surface):
        hero_name = Config.hero_entity_name
        if self.__is_moving_left:
            hero_name = Config.hero_left_entity_name
        if self.__is_moving_right:
            hero_name = Config.hero_right_entity_name
        if self.__is_moving_left and self.__is_moving_right:
            hero_name = Config.hero_entity_name

        image, clip = AssetManager.instance().get(AssetType.SpriteSheet, hero_name, sheet_name = Config.entities_name)
        surface.blit(image, self.render_rect, clip)

        if Config.debug:
            pygame.draw.rect(surface, Config.debug_collider_color, self.rect, 1)
            pygame.draw.rect(surface, Config.debug_render_color, self.render_rect, 1)

    def release(self):
        pass

    def __fire_bullet(self):
        self.__world.spawn_bullet(ProjectileType.AlliedBullet, self.render_rect.midtop, pygame.math.Vector2(Config.allied_bullet_velocity))
        self.__cool_down_time = Config.hero_fire_cooldown

    def check_bounds(self):
        if self.position.x < 0:
            self.position.x = 0
        elif self.position.x > Config.screen_size[0]:
            self.position.x = Config.screen_size[0]

        if self.position.y > Config.screen_size[1]:
            self.position.y = Config.screen_size[1]
        elif self.position.y < Config.screen_size[1] - (Config.screen_size[1] / 2):
            self.position.y = Config.screen_size[1] / 2

        return

    def get_pos(self):
        return self.position
