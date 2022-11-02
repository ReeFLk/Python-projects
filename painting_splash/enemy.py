import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            'img/enemy/'+name+'.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(
            center=(random.randint(0, 448), random.randint(0, 328)))

    def get_coo(self):
        return self.rect.topleft

    def move(self):
        self.rect.x += random.randint(-6, 6)
        self.rect.y += random.randint(-6, 6)


    def update(self):
        self.move()

