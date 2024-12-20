from circleshape import *

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
    
        
        