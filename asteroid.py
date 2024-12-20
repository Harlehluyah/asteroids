from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random


# added in 9 (CH3 - 1)
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Create a rect that encompasses the circle
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2) # added in 13 (CH3 - 5)
    
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, 2)
       
    def update(self, dt):
        self.position += self.velocity * dt
        # Convert Vector2 to tuple of (x,y) coordinates
        self.rect.center = (self.position.x, self.position.y) # added in 13 (CH3 - 5)
        
    # added in 14 (CH3 - 6)
    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            rand_angle = random.uniform(20, 50)
            vector_1 = self.velocity.rotate(rand_angle)
            vector_2 = self.velocity.rotate(-rand_angle)
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = vector_1 * 1.2
            asteroid_2.velocity = vector_2 * 1.2
            asteroid_1.add(self.containers)
            asteroid_2.add(self.containers)
            


            
            
            
    
        
        