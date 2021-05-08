#!/usr/bin/env python3

class Config:

    screen_size = (640,480)
    game_title = "Hello World"

    font_name = "sansation"
    font_filename = ["shmup", "assets", "fonts", "Sansation.ttf"]

    font_fps_size = 24

    entities_name = "entities"
    entities_filename = ["shmup", "assets", "images", "entities.png"]
    entities_data_filename = ["shmup", "assets", "images", "entities.json"]

    hero_name = "eagle"
    hero_left_name = "eagle_left"
    hero_right_name = "eagle_right"
    allied_bullet_name = "allied_bullet"
    allied_bullet_velocity = (0.0, -0.6)

    hero_speed = 0.3

    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_time = 1000.0   
    
    background_color = (0,0,0)
    fps_foreground_color = (255,255,255)
    fps_background_color = (0,0,0)

    gunfire_name = "gunfire"
    gunfire_filename = ["shmup", "assets", "sfx", "gunfire.wav"]

    theme_name = "mission"
    theme_filename = ["shmup", "assets", "music", "mission.ogg"]

    debug = False
    debug_collider_color = (0, 255, 255)
    debug_render_color = (0, 0, 255)

    def __init__(self):
        pass