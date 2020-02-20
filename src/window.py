from player import *
pygame.init()

WIN_SIZE = (500,500)
win = pygame.display.set_mode(WIN_SIZE)


pygame.display.set_caption("First Game")
bg = pygame.image.load('img/bg.jpg')
clock = pygame.time.Clock()

man = Player(300, 418, 64, 64)

def redraw():
    # Fills background color
    win.blit(bg, (0,0))
    man.draw(win)
    pygame.display.update()

run = True
# main loop
while run:
    # clock for game (refresh/frame rate)
    clock.tick(27)


    # Event -> any input change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < WIN_SIZE[1] - man.width - man.velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
    else:
        man.right = False
        man.left = False
        man.walkCount = 0


    if not(man.isJump): 
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpctn >= -10:
            neg = 1
            if man.jumpctn < 0:
                neg = -1

            man.y -= neg * (man.jumpctn**2)/2
            man.jumpctn -= 1 
        else:
            man.isJump = False
            man.jumpctn = 10
    redraw()



pygame.quit()