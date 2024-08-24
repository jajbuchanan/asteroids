import pygame
from constants import *

pygame.init()


def main():
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()


if __name__ == "__main__":
    main()
