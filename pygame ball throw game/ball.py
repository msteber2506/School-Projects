

import pygame
from drawable import Drawable

class Ball(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, visible=True, radius = 0, color = (255,0,0)):
        super().__init__(x, y, visible)
        self.__radius = radius
        self.__color = color

    # Method used to draw a circle
    def draw(self, surface):
        pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)

    # Return the rectangle that fits around the circle
    def get_rect(self):
        return pygame.Rect(self.getLoc()[0]-self.__radius,self.getLoc()[1]-self.__radius,self.__radius*2,self.__radius*2)

    # Radius getter
    def getRadius(self):
        return self.__radius

    # Radius setter
    def setRadius(self, radius):
        self.__radius = radius

    # Color getter
    def getColor(self):
        return self.__color
   
    # Color setter
    def setColor(self, color):
        self.__color = color