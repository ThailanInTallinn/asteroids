from circleshape import CircleShape
import pygame
import random

from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)




    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20, 50)
            v_1 = self.velocity.rotate(new_angle)
            v_2 = self.velocity.rotate(-(new_angle))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position, self.position, new_radius)
            new_asteroid_two = Asteroid(self.position, self.position, new_radius)
            new_asteroid_one.velocity = v_1 * 1.2
            new_asteroid_two.velocity = v_2 * 1.2
