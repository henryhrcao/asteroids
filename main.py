import pygame
from constants import *
from circleshape import *
from player import *
from asteroids import *
from asteroidfield import *
import sys
def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable,updatable)
    Shot.containers = (drawable,updatable, shots)
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for drawing in drawable:
            drawing.draw(screen)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()


if __name__ == "__main__":
    main()
