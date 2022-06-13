

import abc

class Drawable(metaclass = abc.ABCMeta):
    # Constructor
    def __init__(self, x = 0, y = 0, visible = True):
        self.__x = x
        self.__y = y
        self.__visible = visible

    # Location getter
    def getLoc(self):
        return (self.__x, self.__y)

    # Location setter
    def setLocation(self, point):
        self.__x = point[0]
        self.__y = point[1]

    # Visibility setter
    def setVisibility(self,visibility):
        self.__visible = visibility

    # Visibility getter
    def getVisibility(self):
        return self.__visible

    # Abstract functions to be implemented in child classes.
    @abc.abstractmethod
    def draw(self, surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass