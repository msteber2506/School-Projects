

# Importing all the classes that will be used.
import pygame
import random
from drawable import Drawable
from ball import Ball
from text import Text
from block import Block

# Defined a line class here that will be used to draw a line that represents the ground.
class Line(Drawable):
    def __init__(self, x=0, y=0, visible=True):
        super().__init__(x, y, visible)

    def draw(self, surface):
        pygame.draw.line(surface,(100,20,100),(0,650),(1000,650),5)

    def get_rect(self):
        return pygame.Rect(0,650,1000,5)

# A function that will return True if two rectangle objects intersect.
def intersect(rect1, rect2) :
    if (rect1.x < rect2.x + rect2.width) and (rect1.x + rect1.width > rect2.x) and (rect1.y < rect2.y + rect2.height) and (rect1.height + rect1.y > rect2.y) :
          return True
    return False

if __name__ == "__main__":

    pygame.init()   # Initialize pygame
    surface = pygame.display.set_mode((1000, 800))
    ballIsMoving = False # True if ball is moving
    ballLaunched = False # True if ball is already launched
    # Variables are declared
    score = 0
    dt = 0.1
    g= 6.67
    R = 0.7
    eta = 0.5
    xv = 0
    yv = 0
    drawables = []

    ball = Ball(100,630,True,20,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))  # Ball object
    scoreText = Text("Score: " + str(score),50,50) # Text object that displays the score
    ground = Line() # Ground
    blockSize = 30
    blocks =[]

    # Blocks are drawn in the loop
    for row in range(0, 4):
        for column in range(1, 5):
            blocks.append(Block(800 + row * blockSize, 650 - column * blockSize, blockSize, (random.randint(0,255), random.randint(0,255), random.randint(0,255))))

    drawables.append(ball)
    drawables.append(ground)

    pygame.display.set_caption('Ball Throwing Game')
    fpsclock = pygame.time.Clock()
    pauseGame = True
    
    while True: # Main game loop

        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit()
            
            # If ball is not launched yet, it can be launched by pressing and releasing the mouse button.
            if not ballLaunched:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseDownPos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP:
                    mouseUpPos = pygame.mouse.get_pos()

                    xv = mouseUpPos[0] - mouseDownPos[0]
                    yv = -(mouseUpPos[1] - mouseDownPos[1])
                    ballIsMoving = True
                    ballLaunched = True

        scoreText = Text("Score: " + str(score),50,50)
        scoreText.draw(surface)

        # Ball will stop if it hits the edge of display or slows down too much.
        if (yv < 0.0001 and xv < 0.0001) or ball.getLoc()[0]>1000 or ball.getLoc()[1]<0:
                ballIsMoving = False


        if ballIsMoving:
            if ball.getLoc()[1]>630:    # Ball's motion on ground
                yv = -R * yv
                xv = eta * xv
                ball.setLocation((ball.getLoc()[0]+int(dt*xv),630))

            else:   # Ball's motion in air
                yv = yv + g * dt
                ball.setLocation((ball.getLoc()[0]+int(dt*xv),ball.getLoc()[1]+int(dt*yv)))

        surface.fill((160,200,200))
        scoreText.draw(surface)
        
        for item in drawables:
                item.draw(surface)

        # Loop will be used to make the blocks that are hit by the ball invisible
        for block in blocks:
            if block.getVisibility():
                block.draw(surface)
            if intersect(block.get_rect(), ball.get_rect()):
                if block.getVisibility():
                    score += 1
                block.setVisibility(False)

        pygame.display.update()
        fpsclock.tick(60)
