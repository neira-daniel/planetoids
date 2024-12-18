import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)
    # screen is a Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill is a Surface method
        screen.fill("black")
        # draw player
        player.draw(screen)
        # update the full display Surface
        pygame.display.flip()
        # set max FPS to 60 Hz
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
