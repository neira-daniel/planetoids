import sys
import pygame
from asteroidfield import AsteroidField
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # group logic
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    # player(s)
    player = Player(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)
    # other objects
    asteroid_field = AsteroidField()
    # screen is a Surface
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill is a Surface method
        screen.fill("black")
        # update position(s) of updatable Player's instances
        for thing in updatable:
            thing.update(dt)
        # draw drawable Player's instances
        for thing in drawable:
            thing.draw(screen)
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game over!")
                sys.exit(0)
            for bullet in shots:
                if bullet.is_colliding_with(asteroid):
                    bullet.kill()
                    asteroid.split()
                    break
        # update the full display Surface
        pygame.display.flip()
        # set max FPS to 60 Hz
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
