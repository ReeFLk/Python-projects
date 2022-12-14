import pygame
import sys
from tiles import Tile
from player import Player
from pytmx.util_pygame import load_pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2(300, 100)
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        # self.box_target_camera(player)
        self.center_target_camera(player)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            # pygame.draw.rect(self.display_surface, 'yellow', self.camera_rect, 5)
            self.display_surface.blit(sprite.image, offset_pos)


class Level:
    def __init__(self, surface):
        self.display_surface = surface
        self.tmx_data = load_pygame(
            "C:/Users/sipha/Documents/Tiled_project/2dPlatformer/basic.tmx")
        self.camera_group = CameraGroup()
        self.player = Player(self.camera_group)
        self.setup_level()

    def setup_level(self):
        self.tiles_group = pygame.sprite.Group()
        for x, y, surf in self.tmx_data.layers[0].tiles():
            pos = (x*24, y*24)
            self.camera_group.add(
                Tile(pos=pos, surf=surf, groups=self.tiles_group))

    def horiz_collision(self):
        player = self.player
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def verti_collision(self):
        player = self.player
        player.apply_gravity()
        for sprite in self.tiles_group.sprites():
            if sprite.rect.colliderect(player.rect):
                
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    

    def run(self):
        self.player.update()
        # self.horiz_collision()
        self.verti_collision()
        self.camera_group.custom_draw(self.player)
