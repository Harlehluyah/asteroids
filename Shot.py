# added in 11. (CH3 - 3) 
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Create a rect for the shot
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2) # added in 13 (CH3 - 5)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
        # Update rect position to match the circle 
        self.rect.center = (self.position.x, self.position.y) # added in 13 (CH3 - 5)