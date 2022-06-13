

from drawable import Drawable
import pygame

class Text(Drawable):
    # Constructor
    def __init__(self, message = "Pygame", x = 0, y = 0, color = (0,0,0)):
        super().__init__(x, y)
        fontObj = pygame.font.Font("freesansbold.ttf", 26)
        self.__surface = fontObj.render(message, True, color)

    # Displays the message 
    def draw(self, surface):
        surface.blit(self.__surface, self.getLoc())

    # Returns a rectangle that fits around the text
    def get_rect(self):
        return self.__surface.get_rect()
