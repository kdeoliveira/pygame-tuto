from player import *
pygame.init()

WIN_SIZE = (500,500)
win = pygame.display.set_mode(WIN_SIZE)


pygame.display.set_caption("First Game")
bg = pygame.image.load('img/bg.jpg')
clock = pygame.time.Clock()

man = Player(300, 418, 64, 64)
enemy = Enemies(100, 418, 64, 64, 450)
bullets = []

def redraw():
    # Fills background color
    win.blit(bg, (0,0))
    #Drawing elements
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    enemy.draw(win)
    pygame.display.update()


shoot = 0
run = True
# main loop
while run:
    # clock for game (refresh/frame rate)
    clock.tick(27)

    #Manual timer for shooting
    if shoot > 2:
        shoot = 0
    else:
        shoot += 1

    # Event -> any input change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        #Checking for collisions
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                enemy.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))


    keys = pygame.key.get_pressed()
    
    #Shooting
    if keys[pygame.K_SPACE] and not(shoot):
        if man.left:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(Projectile(
                round(man.x + man.width//2), 
                round(man.y + man.height//2), 6, (0,0,0), facing))
        shoot = 1

    if keys[pygame.K_LEFT] and man.x > man.velocity:
        man.x -= man.velocity
        man.left = True
        man.right = False
    elif keys[pygame.K_RIGHT] and man.x < WIN_SIZE[1] - man.width - man.velocity:
        man.x += man.velocity
        man.left = False
        man.right = True
    else:
        man.walkCount = 0
        if man.right:
            man.left = False
        elif man.left:
            man.right = False
        else:    
            man.right = False
            man.left = False


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
