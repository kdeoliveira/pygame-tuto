import pygame
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width =width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpctn = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.walkRight = [pygame.image.load('img/R1.png'), pygame.image.load('img/R2.png'), pygame.image.load('img/R3.png'), pygame.image.load('img/R4.png'), pygame.image.load('img/R5.png'), pygame.image.load('img/R6.png'), pygame.image.load('img/R7.png'), pygame.image.load('img/R8.png'), pygame.image.load('img/R9.png')]
        self.walkLeft = [pygame.image.load('img/L1.png'), pygame.image.load('img/L2.png'), pygame.image.load('img/L3.png'), pygame.image.load('img/L4.png'), pygame.image.load('img/L5.png'), pygame.image.load('img/L6.png'), pygame.image.load('img/L7.png'), pygame.image.load('img/L8.png'), pygame.image.load('img/L9.png')]
        self.char = pygame.image.load('img/standing.png')


    def draw(self, win):

        # Drawing shapes on window
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.char, (self.x, self.y))