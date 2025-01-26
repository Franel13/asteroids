import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            angle = random.uniform(20, 50)
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = self.velocity.rotate(angle)
            asteroid_1.velocity = asteroid_1.velocity * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = self.velocity.rotate(-angle)
            asteroid_2.velocity = asteroid_2.velocity * 1.2

    def draw(self, screen):
        return pygame.draw.circle(screen, (255, 255, 255, 1.0), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)