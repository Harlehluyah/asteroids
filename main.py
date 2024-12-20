import pygame
from constants import *
from Player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0
    
    # added in 8.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # added in 9 (CH3 - 1)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    
    AsteroidField.containers = (updatable,)
    asteroidfield = AsteroidField()
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # added in 5.
    
    while(True):
        for event in pygame.event.get(): # x-button to work on the window
            if event.type == pygame.QUIT:
                return 
        screen.fill("black") 
        
        for item in drawable:
            item.draw(screen)
        
        for item in updatable:
            item.update(dt)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        
        
    

if __name__ == "__main__":
    main()