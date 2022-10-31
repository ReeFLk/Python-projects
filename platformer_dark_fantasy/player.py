import imp
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.past_dir = 0
        self.gravity = 1.8
        self.jump_speed = -16
        self.speed = 6
        self.direction = pygame.math.Vector2((0, 0))
        self.sprites_idle = [pygame.image.load('anim/idle/tile000.png'), pygame.image.load('anim/idle/tile001.png'), pygame.image.load('anim/idle/tile002.png'), pygame.image.load('anim/idle/tile003.png'), pygame.image.load(
            'anim/idle/tile004.png'), pygame.image.load('anim/idle/tile005.png'), pygame.image.load('anim/idle/tile006.png'), pygame.image.load('anim/idle/tile007.png'), pygame.image.load('anim/idle/tile008.png'), pygame.image.load('anim/idle/tile009.png')]
        self.current_idle = 0
        self.sprites_run_r = [pygame.image.load('anim/run_r/tile000.png'), pygame.image.load('anim/run_r/tile001.png'), pygame.image.load('anim/run_r/tile002.png'), pygame.image.load('anim/run_r/tile003.png'), pygame.image.load(
            'anim/run_r/tile004.png'), pygame.image.load('anim/run_r/tile005.png'), pygame.image.load('anim/run_r/tile006.png'), pygame.image.load('anim/run_r/tile007.png'), pygame.image.load('anim/run_r/tile008.png'), pygame.image.load('anim/run_r/tile009.png')]
        self.current_sprite_run_r = 0
        self.sprites_run_l = [pygame.image.load('anim/run_l/tile000.png'), pygame.image.load('anim/run_l/tile001.png'), pygame.image.load('anim/run_l/tile002.png'), pygame.image.load('anim/run_l/tile003.png'), pygame.image.load(
            'anim/run_l/tile004.png'), pygame.image.load('anim/run_l/tile005.png'), pygame.image.load('anim/run_l/tile006.png'), pygame.image.load('anim/run_l/tile007.png'), pygame.image.load('anim/run_l/tile008.png'), pygame.image.load('anim/run_l/tile009.png')]
        self.current_sprite_run_l = 0
        self.turns_right_left = [pygame.image.load('anim/turn_r_to_l/tile000.png'), pygame.image.load(
            'anim/turn_r_to_l/tile001.png'), pygame.image.load('anim/turn_r_to_l/tile002.png')]
        self.current_turn_r_l = 0
        self.turns_left_right = [pygame.image.load('anim/turn_l_to_r/tile000.png'), pygame.image.load(
            'anim/turn_l_to_r/tile001.png'), pygame.image.load('anim/turn_l_to_r/tile002.png')]
        self.current_turn_l_r = 0
        self.image = self.sprites_run_r[self.current_sprite_run_r]
        self.rect = self.image.get_rect(midbottom=(35, 145))

    def player_input(self):

        def run_right():
            self.current_sprite_run_r += 0.6
            self.past_dir = 1
            if self.current_sprite_run_r >= len(self.sprites_run_r):
                self.current_sprite_run_r = 0
            self.image = self.sprites_run_r[int(self.current_sprite_run_r)]
            self.direction.x = 1

        def run_left():
            self.current_sprite_run_l += 0.6
            self.past_dir = -1
            if self.current_sprite_run_l >= len(self.sprites_run_l):
                self.current_sprite_run_l = 0
            self.image = self.sprites_run_l[int(self.current_sprite_run_l)]
            self.direction.x = -1

        def turn_r_l():
            self.current_turn_r_l += 0.5
            if self.current_turn_r_l >= len(self.turns_right_left):
                self.current_turn_r_l = 0
                self.past_dir = -1
                return 0
            self.image = self.turns_right_left[int(self.current_turn_r_l)]
            self.direction.x = -0.2

        def turn_l_r():
            self.current_turn_l_r += 0.5
            if self.current_turn_l_r >= len(self.turns_left_right):
                self.current_turn_l_r = 0
                self.past_dir = 1
                return 0
            self.image = self.turns_left_right[int(self.current_turn_l_r)]
            self.direction.x = 0.2

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            if self.past_dir == -1 and self.current_turn_l_r <= 3:
                turn_l_r()
            else:
                self.current_turn_l_r = 0
                run_right()

        elif keys[pygame.K_LEFT]:
            if self.past_dir == 1 and self.current_turn_r_l <= 3:
                turn_r_l()
            else:
                self.current_turn_r_l = 0
                run_left()
        else:
            self.direction.x = 0
            self.current_idle += 0.2
            if self.current_idle >= len(self.sprites_idle):
                self.current_idle = 0
            self.image = self.sprites_idle[int(self.current_idle)]
        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
            self.direction.y = self.jump_speed

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.player_input()
        self.rect.x += self.direction.x * self.speed
