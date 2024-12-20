from circleshape import *
from Shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.add(*self.containers) # added in 8.
        self.timer = 0 # added in 12. (CH3 - 4)
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        
    def rotate(self, dt): # added in 6
        self.rotation += PLAYER_TURN_SPEED * dt
        
    def update(self, dt): # added in 6
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]: # added in 7
            self.move(dt)
        if keys[pygame.K_s]: # added in 7
            self.move(dt * -1)
        if keys[pygame.K_SPACE]: # added in 11. (CH3 - 3)
            self.shoot()
        
        self.timer -= dt # added in 12. (CH3 - 4)
    
    def move(self, dt): # added in 7
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self): # added in 11. (CH3 - 3) modified in (CH3 - 4)
        if self.timer <= 0: # added in 12. (CH3 - 4)
            new_shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            new_shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN 
        
        
        
            
    