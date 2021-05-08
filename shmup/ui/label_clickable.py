import pygame

from shmup.ui.label import UILabel

class UILabelClickable(UILabel):

    def __init__(self, position, font, text, text_color, hover_color, bg_color=None, action = None):
        super().__init__(position, font, text, text_color, bg_color)

        self.mouse_over = False
        self.hover_image = font.render(text, True, hover_color, bg_color)
        self.action = action

    def handle_input(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.mouse_over = True
            else:
                self.mouse_over = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.mouse_over:
                return self.action

    def render(self, surface):
        image = self.hover_image if self.mouse_over else self.image
        surface.blit(image, self.rect)