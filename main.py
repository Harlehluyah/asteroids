import pygame
from constants import *
from Player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot # added in 11. (CH3 - 3)

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
    
    # added in 11 (CH3 - 3)
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
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
         
        # added in 10 (CH3 - 2)
        for item in asteroids:
            if item.checkcollision(player):
                raise Exception("Game Over!")
        
        # added in 13 (CH3 - 5)
        for item in asteroids:
            hit_list = pygame.sprite.spritecollide(item, shots, True)
            
            if (len(hit_list) > 0): 
                item.split() # modified to split from kill in 14 (CH3 - 6)
        
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        
        
    

if __name__ == "__main__":
    main()