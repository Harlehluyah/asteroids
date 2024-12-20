# added in 11. (CH3 - 3) 
from circleshape import *
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, 2)
       
    def update(self, dt):
        self.position += self.velocity * dt