import pygame
from constants import *
from circleshape import *


class Shot(CircleShape):
        def __init__(self, x, y, radius):
            super().__init__(x, y, radius)

        def draw(self, screen):
            self.screen = screen
            pygame.draw.circle(self.screen, "white", self.position, SHOT_RADIUS, LINE_WIDTH)

        def update(self, dt):
            self.position += (self.velocity * dt)
