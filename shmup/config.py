#!/usr/bin/env python3

class Config:

    screen_size = (640,480)
    game_title = "Hello World"

    hero_filename = ["shmup", "assets", "images", "hero.png"]
    font_filename = ["shmup", "assets", "fonts", "Sansation.ttf"]
    font_fps_size = 24

    hero_speed = 0.3

    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_time = 1000.0   
    
    background_color = (0,0,0)
    fps_foreground_color = (255,255,255)
    fps_background_color = (0,0,0)

    def __init__(self):
        pass