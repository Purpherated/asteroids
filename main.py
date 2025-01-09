import pygame
import sys
from constants import *
from player import Player
from asteroidfield import*
from shots import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable,drawable,asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    roidspawner = AsteroidField()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    

        for pingas in updatable:
            pingas.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Git fuggin ded idiot")
                sys.exit()
            
        for bullet in shots:
            for asteroid in asteroids:
                if asteroid.collide(bullet):
                    asteroid.split()
                    bullet.kill()
            
        
        screen.fill("black")
        
        for bepis in drawable:
            bepis.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        
    

if __name__ == "__main__":
        main()