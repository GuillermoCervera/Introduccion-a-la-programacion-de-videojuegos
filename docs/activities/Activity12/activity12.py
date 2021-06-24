# Guillermo José Cervera Cervera

import pygame
import os

class Sprite:
    sprite_filename=["res","16X16-F9.png"]
    sprite_dimensions=(16,16)
    text_message="Hello World! What is up? How is it going? - "
    text_message_speed=0.15
    def __init__(self,screen_size):
        self.__picture=pygame.image.load(os.path.join(*self.sprite_filename))    
        self.__letters_sign=0
        self.__display_letters=1
        self.__position=pygame.math.Vector2(screen_size[1]/2)  
        self.__letters_sprite={
            " ":self.__picture.subsurface((0*self.sprite_dimensions[0],0*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "!":self.__picture.subsurface((1*self.sprite_dimensions[0],0*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "-":self.__picture.subsurface((13*self.sprite_dimensions[0],0*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "?":self.__picture.subsurface((11*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "a":self.__picture.subsurface((13*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "b":self.__picture.subsurface((14*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "c":self.__picture.subsurface((15*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "d":self.__picture.subsurface((16*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "e":self.__picture.subsurface((17*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "f":self.__picture.subsurface((18*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "g":self.__picture.subsurface((19*self.sprite_dimensions[0],1*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "h":self.__picture.subsurface((0*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "i":self.__picture.subsurface((1*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "j":self.__picture.subsurface((2*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "k":self.__picture.subsurface((3*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "l":self.__picture.subsurface((4*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "m":self.__picture.subsurface((5*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "n":self.__picture.subsurface((6*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "o":self.__picture.subsurface((7*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "p":self.__picture.subsurface((8*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "q":self.__picture.subsurface((9*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "r":self.__picture.subsurface((10*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "s":self.__picture.subsurface((11*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "t":self.__picture.subsurface((12*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "u":self.__picture.subsurface((13*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "v":self.__picture.subsurface((14*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "w":self.__picture.subsurface((15*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "x":self.__picture.subsurface((16*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "y":self.__picture.subsurface((17*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
            "z":self.__picture.subsurface((18*self.sprite_dimensions[0],2*self.sprite_dimensions[1]),(self.sprite_dimensions[0],self.sprite_dimensions[1])),
        }

    def update_screen(self,delta_time,screen_size):
        display=pygame.math.Vector2()
        display.x=display.x-self.text_message_speed
        self.__position=self.__position+(display*delta_time)
        if ((screen_size[0]-self.sprite_dimensions[0])>=self.__position.x):
            self.__position.x=screen_size[0]
            if ((screen_size[0]/self.sprite_dimensions[0])>=self.__display_letters):
                self.__display_letters=self.__display_letters+1
            self.__letters_sign=self.__letters_sign+1
            if (len(self.text_message)<=self.__letters_sign):
                self.__letters_sign=0

    def render_screen(self,screen):
        for letter in range(self.__display_letters):
            screen.blit(self.__letters_sprite[self.text_message[self.__letters_sign-letter].lower()], 
                (self.__position.x-Sprite.sprite_dimensions[0]*letter,self.__position.y))

class Execution:
    title="Activity 1.2"
    background_color=(0)
    screen_size=(640,480)
    time_frame=1
    def __init__(self):
        pygame.init()
        self.__run=0
        self.__screen=pygame.display.set_mode(self.screen_size,0,32)
        self.__sprite=Sprite(self.__screen.get_size())
        pygame.display.set_caption(self.title)

    def __calculate_delta_time(self,final_frame):
        present_time=pygame.time.get_ticks()
        delta_time=present_time-final_frame
        return delta_time,present_time

    def run(self):
        self.__run=1
        time_update=0
        final_frame=pygame.time.get_ticks()
        while self.__run:
            delta_time,final_frame=self.__calculate_delta_time(final_frame)
            time_update=time_update+delta_time
            while (self.time_frame<time_update):
                self.__update_screen(self.time_frame)
                time_update=time_update-self.time_frame
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
