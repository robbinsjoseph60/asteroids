import pygame
import random
from circleshape import CircleShape
from constants import *
from player import Player

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, player):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            player.increase_score(10)
            return
        
        elif self.radius == ASTEROID_MAX_RADIUS:
            player.increase_score(1)

        else:
            player.increase_score(5)
        
        random_angle = random.uniform(20, 50)
        new_vector1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
        new_vector2 = pygame.math.Vector2.rotate(self.velocity, -(random_angle))
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = new_vector1 * 1.2
        

        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = new_vector2 * 1.2



        

        
        
        
