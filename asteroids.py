from circleshape import *
from constants import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.position = pygame.Vector2(x,y)
        self.radius = radius
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.randint(20, 50)
            v1 = self.velocity.rotate(angle)
            v2 = self.velocity.rotate(-angle)
            radiusN = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position[0],self.position[1],radiusN)
            a1.velocity = v1 * 1.2
            a2 = Asteroid(self.position[0],self.position[1],radiusN)
            a2.velocity = v2 * 1.2
        self.kill()


    def update(self,dt):
        self.position += self.velocity*dt