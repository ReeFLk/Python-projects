import pygame
from player import Player
from enemy import Enemy
from unicorn import Unicorn
from explosions import Explo


class Level:
    def __init__(self, surface):
        self.display_surf = surface
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.enemy = pygame.sprite.Group()
        self.unicorn = pygame.sprite.GroupSingle()
        self.unicorn.add(Unicorn())
        self.enemies = ['beholder', 'cerberus', 'cyclops', 'djinn',
                        'dragon', 'gargoyle', 'goblin', 'kitsune', 'kraken','mandrake','mermaid','mimic','phoenix','succubus','wendigo']
        for enemy in self.enemies:
            self.enemy.add(Enemy(enemy, self.enemy))
        self.explo = pygame.sprite.Group()

    def killing(self):
        for e in self.enemy.sprites():
            if self.player.sprite.click() != None and (e.get_coo()[0] <= self.player.sprite.click()[0] <= int(e.get_coo()[0])+20 and e.get_coo()[1] <= self.player.sprite.click()[1] <= int(e.get_coo()[1])+20):
                self.explo.add(Explo(e.get_coo(),self.explo))
                e.remove(self.enemy)

    def run(self):
            if self.explo != None:
                self.explo.update()
                self.explo.draw(self.display_surf)

            self.enemy.update()
            self.enemy.draw(self.display_surf)

            self.unicorn.draw(self.display_surf)

            self.player.update()
            self.player.draw(self.display_surf)

            self.killing()
            
