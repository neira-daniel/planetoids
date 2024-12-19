import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # when there's a hit, the planetoid should always disappear from the screen
        self.kill()
        # when the planetoid is small enough, it disappears without splitting
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # everything else do split
        new_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        planetoid_A = Asteroid(self.position.x, self.position.y, new_radius)
        planetoid_A.velocity = 1.2 * self.velocity.rotate(-new_angle)
        planetoid_B = Asteroid(self.position.x, self.position.y, new_radius)
        planetoid_B.velocity = 1.2 * self.velocity.rotate(new_angle)
