import pygame
from constants import *
from Player import *

def main():
    pygame.init()
    print("Starting asteroids!")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
    clock = pygame.time.Clock()
    dt = 0
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) # added in 5.
    
    while(True):
        for event in pygame.event.get(): # x-button to work on the window
            if event.type == pygame.QUIT:
                return 
        screen.fill("black") 
        player.draw(screen) # added in 5.
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        
        
    

if __name__ == "__main__":
    main()