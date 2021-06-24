# Guillermo José Cervera Cervera

import pygame
import random
import os

pygame.display.set_caption("FinalActivity")
pygame.font.init()

W=640
H=480
SCREEN=pygame.display.set_mode((W,H))
CHARMANDER=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","charmander.png"))
SQUIRTLE=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","squirtle.png"))
BULBASAUR=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","bulbasaur.png"))
TRAINER=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","trainer.png"))
CHARMANDER_ATTACK=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","charmander_attack.png"))
SQUIRTLE_ATTACK=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","squirtle_attack.png"))
BULBASAUR_ATTACK=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","bulbasaur_attack.png"))
POKEBALL=pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","pokeball.png"))
BACKGROUND=pygame.transform.scale(pygame.image.load(os.path.join("docs","activities","FinalActivity","assets","background.jpg")),(W,H))

class Pokeball:
    def __init__(self,x,y,picture):
        self.x=x
        self.y=y
        self.image=picture
        self.hide=pygame.mask.from_surface(self.image)
    def sketch(self,screen):
        screen.blit(self.image,(self.x,self.y))
    def impact(self,object):
        return crash(self,object)
    def move(self,velocity):
        self.y=velocity+self.y
    def out_window(self,h):
        return not(self.y>=0 and self.y<=h)

class Pokemon:
    def __init__(self,x,y,state=100):
        self.x=x
        self.y=y
        self.state=state
        self.pokemon_image=None
        self.attack_image=None
        self.attacks=[]
        self.calm_counting=0
    def height(self):
        return self.pokemon_image.get_height()
    def width(self):
        return self.pokemon_image.get_width()
    def sketch(self,screen):
        screen.blit(self.pokemon_image,(self.x,self.y))
        for attack in self.attacks:
            attack.sketch(screen)
    def movements(self,velocity,object):
        self.calm()
        for attack in self.attacks:
            attack.move(velocity)
            if attack.out_window(H):
                self.attacks.remove(attack)
            elif attack.impact(object):
                object.state-=20
                self.attacks.remove(attack)
    def onslaught(self):
        if self.calm_counting==0:
            attack=Pokeball(self.x,self.y,self.attack_image)
            self.attacks.append(attack)
            self.calm_counting=1
    CALM=20
    def calm(self):
        if self.calm_counting>=self.CALM:
            self.calm_counting=0
        elif self.calm_counting>0:
            self.calm_counting=self.calm_counting+1

class Wild(Pokemon):
    MAP={"R":(CHARMANDER,CHARMANDER_ATTACK),"G":(BULBASAUR,BULBASAUR_ATTACK),"B":(SQUIRTLE,SQUIRTLE_ATTACK),}
    def __init__(self,x,y,color,state=100):
        super().__init__(x,y,state)
        self.pokemon_image,self.attack_image=self.MAP[color]
        self.hide=pygame.mask.from_surface(self.pokemon_image)
    def move(self,velocity):
        self.y=velocity+self.y

class Trainer(Pokemon):
    def __init__(self,x,y,state=100):
        super().__init__(x,y,state)
        self.pokemon_image=TRAINER
        self.attack_image=POKEBALL
        self.hide=pygame.mask.from_surface(self.pokemon_image)
        self.max_state=state
    def movements(self,velocity,objects):
        self.calm()
        for attack in self.attacks:
            attack.move(velocity)
            if attack.out_window(H):
                self.attacks.remove(attack)
            else:
                for object in objects:
                    if attack.impact(object):
                        objects.remove(object)
                        if attack in self.attacks:
                            self.attacks.remove(attack)
    def sketch(self,screen):
        super().sketch(screen)
        self.statebar(screen)
    def statebar(self,screen):
        pygame.draw.rect(screen,(250,0,0),(self.x,self.y+self.pokemon_image.get_height()+5,self.pokemon_image.get_width(),5))
        pygame.draw.rect(screen,(0,250,0),(self.x,self.y+self.pokemon_image.get_height()+5,self.pokemon_image.get_width()*(self.state/self.max_state),5))

def crash(object1,object2):
    offset_x=object2.x-object1.x
    offset_y=object2.y-object1.y
    return object1.hide.overlap(object2.hide,(offset_x,offset_y))!=None

def principal():
    run=1
    frames=60
    difficulty=0
    lives=3
    principal_letter=pygame.font.SysFont("arial",30)
    lost_letter=pygame.font.SysFont("arial",40)
    enemies=[]
    wave_length=5
    enemy_velocity=1
    trainer_velocity=5
    attack_velocity=5
    trainer=Trainer(300,630)
    time=pygame.time.Clock()
    lost_counting=0
    lost=0

    def resketch_screen():
        SCREEN.blit(BACKGROUND,(0,0))
        lives_message=principal_letter.render(f"YOUR LIVES: {lives}",1,(0,0,0))
        difficulty_message=principal_letter.render(f"DIFFICULTY: {difficulty}",1,(0,0,0))
        SCREEN.blit(difficulty_message,(425,425))
        SCREEN.blit(lives_message,(W-lives_message.get_width()-425,425))
        for enemy in enemies:
            enemy.sketch(SCREEN)
        trainer.sketch(SCREEN)
        if lost:
            lost_message=lost_letter.render("You lost :(",1,(0,0,0))
            SCREEN.blit(lost_message,(W/2-lost_message.get_width()/2,350))
        pygame.display.update()
    while run:
        time.tick(frames)
        resketch_screen()
        if lost:
            if lost_counting>frames*3:
                run=0
            else:
                continue
        if (trainer.state<=0)or(lives<=0):
            lost_counting=lost_counting+1
            lost=1
        for occurrence in pygame.event.get():
            if occurrence.type==pygame.QUIT:
                quit()
        if len(enemies)==0:
            wave_length=wave_length+7
            difficulty=difficulty+1
            for i in range(wave_length):
                enemy=Wild(random.randrange(60,W-90),random.randrange(-1400,-90),random.choice(["R","G","B"]))
                enemies.append(enemy)
        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            enemy.movements(attack_velocity,trainer)
            if crash(enemy,trainer):
                trainer.state=trainer.state-25
                enemies.remove(enemy)
            if enemy.y+enemy.height()>H:
                lives-=1
                enemies.remove(enemy)
            elif random.randrange(0,2*50)==1:
                enemy.onslaught()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]and(trainer.y-trainer_velocity>=1):
            trainer.y-=trainer_velocity
        if keys[pygame.K_DOWN]and(trainer.y+trainer_velocity+trainer.height()+20<H):
            trainer.y+=trainer_velocity
        if keys[pygame.K_LEFT]and(trainer.x-trainer_velocity>=1):
            trainer.x-=trainer_velocity
        if keys[pygame.K_RIGHT]and(trainer.x+trainer_velocity+trainer.width()<W):
            trainer.x+=trainer_velocity
        if keys[pygame.K_SPACE]:
            trainer.onslaught()
        trainer.movements(-attack_velocity,enemies)

def principal_menu():
    run=1
    title_letter=pygame.font.SysFont("arial",60)
    while run:
        title_message=title_letter.render("Click here to play",1,(0,0,0))
        SCREEN.blit(BACKGROUND,(0,0))
        SCREEN.blit(title_message,(W/2-title_message.get_width()/2,350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=0
            if event.type==pygame.MOUSEBUTTONDOWN:
                principal()
    pygame.quit()
principal_menu()
