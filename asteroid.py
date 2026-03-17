from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_state, log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        vel_after_split = self.velocity.rotate(random_angle)
        other_vel_after_split = self.velocity.rotate(-(random_angle))
        radius_after_split = self.radius - ASTEROID_MIN_RADIUS
        split_asteroid_1 = Asteroid(self.position.x, self.position.y, radius_after_split)
        split_asteroid_2 = Asteroid(self.position.x, self.position.y, radius_after_split)
        split_asteroid_1.velocity = vel_after_split * 1.2
        split_asteroid_2.velocity = other_vel_after_split * 1.2