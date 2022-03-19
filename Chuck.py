import pygame

pygame.init()
health = 5
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Chuck the Weezard")
# Player
walkUp = [pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png"),pygame.image.load("cwchuckweezardb1.png")]
walkDown = [pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png"),pygame.image.load("cwchuckweezardf1.png")]
walkLeft = [pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png"),pygame.image.load("cwchuckweezardl1.png")]
walkRight = [pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png"),pygame.image.load("cwchuckweezardr1.png")]
char = pygame.image.load('Generic_Wizard_Frontsprite.png')
bg = pygame.image.load("bg.png")
#x = 50
#y = 50
#width = 40
#height = 60
vel = 2
facing = 1
clock = pygame.time.Clock()
class player(object):
    def __init__(self, x, y, width, height):
        self.standing = True
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.down:
                win.blit(walkDown[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.up:
                win.blit(walkUp[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            elif self.down:
                win.blit(walkDown[0], (self.x, self.y))
            elif self.up:
                win.blit(walkUp[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0,0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()

def Gameover():
    pygame.quit()


# mainloop
man = player(200, 410, 64,64)
bullets = []
run = True
while run:
    clock.tick(27)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if man.left or man.right:
            if 1000 > bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
        else:
            if 1000 > bullet.x > 0:
                bullet.y += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left or man.up:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5000:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 255, 0), facing))
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 1000 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.down = False
        man.up = False
        man.standing = False

    elif keys[pygame.K_UP] and man.y > man.vel:
        man.y -= man.vel
        man.down = False
        man.up = True
        man.left = False
        man.right = False
        man.standing = False
    elif keys[pygame.K_DOWN] and man.y < 1000 - man.width - man.vel:
        print()
        man.y += man.vel
        man.up = False
        man.down = True
        man.left = False
        man.right = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if health == 0:
        Gameover()
    redrawGameWindow()

pygame.quit()
