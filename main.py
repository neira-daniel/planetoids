import pygame
from constants import *

def main():
    pygame.init()
    # screen is a Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill is a Surface method
        screen.fill("black")
        # update the full display Surface
        pygame.display.flip()


if __name__ == "__main__":
    main()
