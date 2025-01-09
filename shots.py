from constants import *
import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,SHOT_RADIUS)

    def draw(self,screen):
        pygame.draw.circle(screen,"green",self.position,self.radius)

    def update(self,dt):
        self.position += self.velocity * dt
