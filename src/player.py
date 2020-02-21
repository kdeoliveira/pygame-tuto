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
        self.left = True
        self.right = False
        self.walkCount = 0
        self.hitbox = (self.x + 20, self.y + 10, 23, 51)


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
        
        #Debugging only - hitbox
        self.hitbox = (self.x + 20, self.y + 10, 23, 51)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)



# PROJECTILE CLASS FOR BULLETS
class Projectile:
    def __init__(self,x , y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.velocity = 8 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemies:
    walkRight = [pygame.image.load('img/R1E.png'), pygame.image.load('img/R2E.png'), pygame.image.load('img/R3E.png'), pygame.image.load('img/R4E.png'), pygame.image.load('img/R5E.png'), pygame.image.load('img/R6E.png'), pygame.image.load('img/R7E.png'), pygame.image.load('img/R8E.png'), pygame.image.load('img/R9E.png'),pygame.image.load('img/R10E.png'),pygame.image.load('img/R11E.png')]
    walkLeft = [pygame.image.load('img/L1E.png'), pygame.image.load('img/L2E.png'), pygame.image.load('img/L3E.png'), pygame.image.load('img/L4E.png'), pygame.image.load('img/L5E.png'), pygame.image.load('img/L6E.png'), pygame.image.load('img/L7E.png'), pygame.image.load('img/L8E.png'), pygame.image.load('img/L9E.png'),pygame.image.load('img/L10E.png'),pygame.image.load('img/L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.velocity = 3
        self.hitbox = (self.x + 15, self.y, 25, 60)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        
        if self.velocity > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x - 10, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 15, self.y, 25, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        pass

    def move(self):
        if self.velocity > 0:
                if self.x + self.velocity < self.path[1]:
                    self.x += self.velocity
                else:
                    self.velocity *= -1
                    self.walkCount = 0
        else:
            if self.x - self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.walkCount = 0
        pass
    
    def hit(self):
        print("Enemie hit")
        pass