# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize PyGame
    pygame.init()

    # Environment
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Player
    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)
    
    AsteroidField()

    while True:
        # Set "Quit"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for instance in updatable:
            instance.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        # Draw first screen
        screen.fill((0, 0, 0, 1.0))
        
        # Draw player
        for instance in drawable:
            instance.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Set framerate
        val = clock.tick(60)
        dt = val / 1000


if __name__ == "__main__":
    main()
