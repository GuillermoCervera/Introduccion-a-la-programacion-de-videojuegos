# Guillermo José Cervera Cervera

import pygame
import os
import math

class Sprite:
    sprite_filename=["res","walking_animation.png"]
    sprite_dimensions=(64,130)
    girl_speed=0.3
    frames=60
    def __init__(self,window_size):
        self.__image=pygame.image.load(os.path.join(*self.sprite_filename))
        self.__position=pygame.math.Vector2(0,window_size[1]-self.sprite_dimensions[1])
        self.__move_girl=0
        self.__walk_girl=1
        self.__halt_movement=0
        self.__add_movement=1

    def render_screen(self,destination):
        surf_y=0
        surf_x=1
        steps,steps=math.modf(self.__add_movement)
        if self.__walk_girl==1:
            surf_x=0
        if self.__move_girl==1:
            surf_y=steps
        destination.blit(self.__image,self.__position.xy,(self.sprite_dimensions[0]*surf_y,self.sprite_dimensions[1]*surf_x,self.sprite_dimensions[0],self.sprite_dimensions[1]))

    def update_screen(self,delta_time,window_size):
        add_movement=pygame.math.Vector2()
        if self.__move_girl!=0:
            if self.__walk_girl!=0:
                if (window_size[0]-self.sprite_dimensions[0]>self.__position.x):
                    add_movement.x=self.girl_speed+add_movement.x
                    self.__add_movement=(self.girl_speed*0.45)+self.__add_movement
                    if self.__add_movement>9:
                        self.__add_movement=1
                else:
                    self.__move_girl=0
                    self.__walk_girl=0
            else:
                if self.__position.x>=1:
                    add_movement.x-=self.girl_speed
                    self.__add_movement=(self.girl_speed*0.45)+self.__add_movement
                    if self.__add_movement>9:
                        self.__add_movement=1
                else:
                    self.__move_girl=0
                    self.__walk_girl=1
        else:
            self.__halt_movement=(self.girl_speed*50)+self.__halt_movement
            if (self.frames<self.__halt_movement):
                self.__halt_movement=0
                self.__move_girl=1
                self.__add_movement=1
        self.__position=self.__position+(add_movement*delta_time)

class Execution:
    screen_size=(640,480)
    title="Activity 1.1"
    time_frame=10
    background_color=(255,255,255)
    def __init__(self):
        pygame.init()
        self.__screen=pygame.display.set_mode(self.screen_size)
        self.__sprite=Sprite(self.__screen.get_size())
        self.__run=0
        pygame.display.set_caption(self.title)

    def __calculate_delta_time(self,final_frame):
        present_time=pygame.time.get_ticks()
        delta_time=present_time-final_frame
        return delta_time,present_time

    def run(self):
        self.__run=1
        final_frame=pygame.time.get_ticks()
        time_update=0
        while self.__run:
            delta_time,final_frame=self.__calculate_delta_time(final_frame)
            time_update=delta_time+time_update
            while (self.time_frame<time_update):
                time_update=self.time_frame-time_update
                self.__update_screen(self.time_frame)
                self.__events()
            self.__render_screen()
        self.__quit()

    def __render_screen(self):
        self.__screen.fill(self.background_color)
        self.__sprite.render_screen(self.__screen)
        pygame.display.update()

    def __update_screen(self,delta_time):
        self.__sprite.update_screen(delta_time,self.__screen.get_size())
    
    def __events(self):
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                self.__run=0

    def __quit(self):
        pygame.quit()
