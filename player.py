import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__(self, x, y, score):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.pt = 0
        self.score = score

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
            
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.pt <= 0:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            velocity = forward * PLAYER_SHOOT_SPEED
            Shot(self.position.x, self.position.y, velocity)
            self.pt += PLAYER_SHOOT_COOLDOWN

    def increase_score(self, points):
        self.score += points

    def update(self, dt):
        if self.pt > 0:
            self.pt -= dt
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
