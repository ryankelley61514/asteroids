import pygame
import random
from circleshape import CircleShape
from constants import *

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
            angle = random.uniform(20, 50)
            split_a_velocity = self.velocity.rotate(angle)
            split_b_velocity = self.velocity.rotate(-angle)
            split_radius = self.radius - ASTEROID_MIN_RADIUS
            split_a = Asteroid(self.position.x, self.position.y, split_radius)
            split_b = Asteroid(self.position.x, self.position.y, split_radius)
            split_a.velocity = split_a_velocity * 1.2
            split_b.velocity = split_b_velocity * 1.2