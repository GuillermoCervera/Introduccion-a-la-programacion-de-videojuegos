import pygame
from os import path

def stereo_pan(x_coord, screen_width):
    right_volume = float(x_coord) / screen_width
    left_volume = 1.0 - right_volume

    return (left_volume, right_volume)

pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

screen_size = (640,480)
screen = pygame.display.set_mode(screen_size, 0, 32)

gunfire_filename = ["shmup" , "assets", "sfx", "gunfire.wav"]
gunfire_sound = pygame.mixer.Sound(path.join(*gunfire_filename))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            gunfire_channel = gunfire_sound.play()
            if gunfire_channel is not None:
                left, right = stereo_pan(event.pos[0], screen_size[0])
                gunfire_channel.set_volume(left, right)

    pygame.display.update()

pygame.quit()