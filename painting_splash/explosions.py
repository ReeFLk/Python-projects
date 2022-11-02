import pygame


class Explo(pygame.sprite.Sprite):
    def __init__(self, coo, groups):
        super().__init__(groups)
        self.explosions = [pygame.image.load('img/explosion/48x48 - MidairExplosionFrame1.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame2.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame3.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame4.png').convert_alpha(), pygame.image.load(
            'img/explosion/48x48 - MidairExplosionFrame5.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame6.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame7.png').convert_alpha(), pygame.image.load('img/explosion/48x48 - MidairExplosionFrame8.png').convert_alpha(), pygame.transform.scale(pygame.image.load('img/tache de peinture.png').convert_alpha(), (40, 40))]
        self.current_explo = 0
        self.image = self.explosions[self.current_explo]
        self.rect = self.image.get_rect(topleft=coo)

    def death(self):
        if self.current_explo <= 8:
            self.image = self.explosions[int(self.current_explo)]
            self.current_explo += 0.5
        

    def update(self):
        self.death()
