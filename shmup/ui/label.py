import pygame

class UILabel:

    def __init__(self, position, font, text, text_color, bg_color=None):
        self.image = font.render(text, True, text_color, bg_color)
        self.rect = self.image.get_rect(center = position)
    
    def handle_input(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self, surface):        
        surface.blit(self.image, self.rect)