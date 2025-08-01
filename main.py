import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	asteroids = pygame.sprite.Group()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroid_field = AsteroidField()

	Shot.containers = (shots, updatable, drawable)
	
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 0)
	

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		updatable.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print (f"Game over!\nScore: {player.score}")
				sys.exit()
			for shot in shots:
				if asteroid.collides_with(shot):
					shot.kill()
					asteroid.split(player)
				
			
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		
		# cap fps at 60
		dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()
