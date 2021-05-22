#!/usr/bin/env python3

class Config:

    screen_size = (480, 640)
    game_title = "ShMUp"
    background_color = (0, 0, 0)

    entities_name = "entities"
    entities_image_filename = ["shmup", "assets", "images", "entities.png"]
    entities_data_filename = ["shmup", "assets", "images", "entities.json"]

    explosion_name = "explosion"
    explosion_image_filename = ["shmup", "assets", "images", "explosion.png"]
    explosion_size = (4,4)
    explosion_time_per_sequence = 40

    jungle_name = "jungle"
    jungle_image_filename = ["shmup", "assets", "images", "jungle.png"]
    jungle_speed = 0.3
    clouds_name = "clouds"
    clouds_image_filename = ["shmup", "assets", "images", "clouds.png"]
    clouds_speed = 0.4

    hero_entity_name = "eagle"
    hero_left_entity_name = "eagle_left"
    hero_right_entity_name = "eagle_right"
    allied_bullet_entity_name = "allied_bullet"
    enemy_bullet_entity_name = "enemy_bullet"

    font_name = "sansation"
    font_filename = ["shmup", "assets", "fonts", "Sansation.ttf"]

    allied_gunfire_name = "allied_gunfire"
    allied_gunfire_filename = ["shmup", "assets", "sfx", "allied_gunfire.wav"]
    enemy_gunfire_name = "enemy_gunfire"
    enemy_gunfire_filename = ["shmup", "assets", "sfx", "enemy_gunfire.wav"]
    explosion1_name = "explosion1"
    explosion1_filename = ["shmup", "assets", "sfx", "explosion1.wav"]
    explosion2_name = "explosion2"
    explosion2_filename = ["shmup", "assets", "sfx", "explosion2.wav"]

    mission_theme_name = "mission"
    mission_theme_filename = ["shmup", "assets", "music", "mission.ogg"]

    hero_speed = 0.25
    hero_fire_cooldown = 300
    allied_bullet_velocity = (0.0, -0.3)

    fps = 60
    time_per_frame = 1000.0 / fps
    refresh_stats_time = 1000.0
    fps_stats_pos = (0, 2)

    debug = False
    debug_collider_color = (0, 255, 255)
    debug_render_color = (0, 0, 255)
    debug_way_point_color = (0,255,0)

    waypoints_area = (screen_size[0], screen_size[1] / 2)
    waypoints_separation = (120, 100)

    enemy_raptor_name = "raptor"
    enemy_avenger_name = "avenger"

    enemies_spawn_probability = 0.01
    enemies_max_waypoints = 5
    enemies_projectile_speed_range = (0.1, 0.4)
    enemies_kamikaze_probability = 0.3
    enemies_data = {
        "raptor" : { "fire_rate" : 0.005, "speed" : 0.1, "acceleration" : 0.005},
        "avenger" : { "fire_rate" : 0.01, "speed" : 0.12, "acceleration" : 0.005} }

    enemies_spawn_points = [(-100, 0),
                            (100, -100),
                            (screen_size[0]/2, -100),
                            (screen_size[0] - 100 , -100),
                            (screen_size[0] + 100, 0)]

    enemies_end_points = [(-100, 0),
                            (100, -100),
                            (-100, screen_size[1]),
                            (100, screen_size[1] + 100),
                            (screen_size[0]/2, screen_size[1] + 100),
                            (screen_size[0] - 100 , screen_size[1] + 100),
                            (screen_size[0] + 100, screen_size[1])]

    game_over_time = 5000

    def __init__(self):
        pass
