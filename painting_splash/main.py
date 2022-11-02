import sys
import pygame
from game import Level


def main():
    pygame.init()

    SIZE = width, height = 480, 360
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
    pygame.display.set_caption('Painting Splash')
    pygame.mouse.set_visible(False)
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
        screen.fill('white')
        level.run()
        pygame.display.update()
        # print(clock.get_fps())
        clock.tick(60)


main()
