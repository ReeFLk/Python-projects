import pygame


class Unicorn(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('img/unicorn.png').convert_alpha(),(42,42))
        self.rect = self.image.get_rect(center=(220,150))
    def update(self):
        pass