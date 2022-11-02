import sys
import pygame
from level import Level


def main():
    pygame.init()

    SIZE = width, height = 480, 360
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Platformer")
    bg_imgs = [pygame.image.load('background/background_layer_1.png').convert_alpha(), pygame.image.load(
        'background/background_layer_2.png').convert_alpha(), pygame.image.load('background/background_layer_3.png').convert_alpha()]

    level = Level(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode(
                    (event.w, event.h), pygame.RESIZABLE)

        # Background
        screen.blit(bg_imgs[0], (0, 0))
        screen.blit(bg_imgs[1], (0, 0))
        screen.blit(bg_imgs[2], (0, 0))

        level.run()
        pygame.display.update()
        print(clock.get_fps())
        clock.tick(60)


main()
