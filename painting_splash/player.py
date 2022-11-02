import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.loc = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.image = pygame.image.load('img/hand.png').convert_alpha()
        self.rect = self.image.get_rect(center=self.loc)
            
    def click(self):
        if pygame.mouse.get_pressed()[0]:
            return self.loc

    def update(self):
        self.loc = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        self.rect = self.rect = self.image.get_rect(center=self.loc)