

from drawable import Drawable
import pygame


class Block(Drawable):
    # Constructor
    def __init__(self, x=0, y=0, length=1, color=(0, 0, 0), visibility=True):
        super().__init__(x, y, visibility)
        self.__sideLength = length
        self.__color = color
        self.__rect = pygame.Rect(x, y, length, length)

    # Method used to draw a square with a black outline
    def draw(self, surface):
        outlineColor = (0, 0, 0)
        outlineWidth = 2
        pygame.draw.rect(surface, self.__color, self.__rect, 0)
        pygame.draw.rect(surface, outlineColor, self.__rect, outlineWidth)

    # Returns a rectangle that fits around the block
    def get_rect(self):
        return pygame.Rect(self.getLoc()[0], self.getLoc()[1], self.__sideLength, self.__sideLength)

    # Getter for square's side length
    def getLength(self):
        return self.__sideLength

    # Setter for square's side length
    def setLength(self, length):
        self.__sideLength = length

    # Getter for color
    def getColor(self):
        return self.__color

    # Setter for color
    def setColor(self, color):
        self.__color = color

