import pygame
import random

pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chuck the Weezard")
# Player
walkUp = [pygame.image.load("cwchuckweezardb1.png"), pygame.image.load("cwchuckweezardb1.png"),
          pygame.image.load("cwchuckweezardb1.png"), pygame.image.load("cwchuckweezardb1.png"),
          pygame.image.load("cwchuckweezardb1.png"), pygame.image.load("cwchuckweezardb1.png"),
          pygame.image.load("cwchuckweezardb1.png"), pygame.image.load("cwchuckweezardb1.png"),
          pygame.image.load("cwchuckweezardb1.png")]
walkDown = [pygame.image.load("cwchuckweezardf1.png"), pygame.image.load("cwchuckweezardf1.png"),
            pygame.image.load("cwchuckweezardf1.png"), pygame.image.load("cwchuckweezardf1.png"),
            pygame.image.load("cwchuckweezardf1.png"), pygame.image.load("cwchuckweezardf1.png"),
            pygame.image.load("cwchuckweezardf1.png"), pygame.image.load("cwchuckweezardf1.png"),
            pygame.image.load("cwchuckweezardf1.png")]
walkLeft = [pygame.image.load("cwchuckweezardl1.png"), pygame.image.load("cwchuckweezardl1.png"),
            pygame.image.load("cwchuckweezardl1.png"), pygame.image.load("cwchuckweezardl1.png"),
            pygame.image.load("cwchuckweezardl1.png"), pygame.image.load("cwchuckweezardl1.png"),
            pygame.image.load("cwchuckweezardl1.png"), pygame.image.load("cwchuckweezardl1.png"),
            pygame.image.load("cwchuckweezardl1.png")]
walkRight = [pygame.image.load("cwchuckweezardr1.png"), pygame.image.load("cwchuckweezardr1.png"),
             pygame.image.load("cwchuckweezardr1.png"), pygame.image.load("cwchuckweezardr1.png"),
             pygame.image.load("cwchuckweezardr1.png"), pygame.image.load("cwchuckweezardr1.png"),
             pygame.image.load("cwchuckweezardr1.png"), pygame.image.load("cwchuckweezardr1.png"),
             pygame.image.load("cwchuckweezardr1.png")]
char = pygame.image.load('cwchuckweezardf1.png')
bg = pygame.image.load("bg.png")
# x = 50
# y = 50
# width = 40
# height = 60
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
        self.rect = char.get_rect()
        self.hp = 5

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


class Xprojectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        print("n")


class Yprojectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 20 * facing
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
        print("y")


class Slime(pygame.sprite.Sprite):

    def __init__(self, x, y, boss):
        pygame.sprite.Sprite.__init__(self)
        self.frames = ['cwslime1.png', 'cwslime2.png', 'cwslime3.png']
        self.bframes = ['cwboss1.png', 'cwboss2.png', 'cwboss3.png']
        self.n = 0
        self.x = x
        self.y = y
        self.gx = 0
        self.gy = 0
        self.boss = boss
        if self.boss == True:
            self.image = pygame.image.load(self.bframes[self.n])
            self.rect = self.image.get_rect()
            self.lwid = 544
            self.lhei = 344
            self.hp = 5
        else:
            self.image = pygame.image.load(self.frames[self.n])
            self.rect = self.image.get_rect()
            self.lwid = 672
            self.lhei = 472
            self.hp = 1
        self.rect = self.image.get_rect()

    def rangen_x(self):
        self.gx = random.randint(0, self.lwid)

    def rangen_y(self):
        self.gy = random.randint(0, self.lhei)

    def move(self):
        if self.x < self.gx:
            self.x += 1
        elif self.x > self.gx:
            self.x -= 1
        else:
            self.rangen_x()

        if self.y < self.gy:
            self.y += 1
        elif self.y > self.gy:
            self.y -= 1
        else:
            self.rangen_y()
        self.rect = self.image.get_rect()

    def animate(self):
        if self.n >= 2:
            self.n = 0
        self.n += 1
        if self.boss == True:
            self.image = pygame.image.load(self.bframes[self.n])
        else:
            self.image = pygame.image.load(self.frames[self.n])


def hitCheck(slimes, bullets):
    for s in range(len(slimes)):
        for bullet in bullets:
            if pygame.Rect.colliderect(slimes[s].rect, bullet.rect):
                slimes[s].hp -= 1
        if slimes[s].hp <= 0:
            slimes.pop(s)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    hitCheck(slimes, xbullets)
    hitCheck(slimes, ybullets)
    for bullet in xbullets:
        bullet.draw(win)
    for bullet in ybullets:
        bullet.draw(win)
    for slime in slimes:
        for x in range(3):
            slime.move()
        slime.animate()
        win.blit(slime.image, (slime.x, slime.y))
    pygame.display.update()


def Gameover():
    pygame.quit()


# mainloop
man = player(200, 410, 64, 64)
xbullets = []
ybullets = []
o = Slime(60, 60, False)
slimes = []
slimes.append(o)
run = True
while run:
    print(ybullets)
    clock.tick(27)
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for xbullet in xbullets:
        if 800 > xbullet.x > 0:
            xbullet.x += xbullet.vel
            xbullet.rect = pygame.Rect(xbullet.x, xbullet.y, xbullet.radius, xbullet.radius)
        else:
            xbullets.pop(xbullets.index(xbullet))
    for ybullet in ybullets:
        if 800 > ybullet.y > 0:
            ybullet.y += ybullet.vel
            ybullet.rect = pygame.Rect(ybullet.x, ybullet.y, ybullet.radius, ybullet.radius)
        else:
            ybullets.pop(ybullets.index(ybullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left or man.up:
            facing = -1
        else:
            facing = 1
        if man.left or man.right:
            if len(xbullets) < 5 and len(ybullets) < 5:
                xbullets.append(
                    Xprojectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 255, 0), facing))
        if man.up or man.down:
            if len(xbullets) < 5 and len(ybullets) < 5:
                ybullets.append(
                    Yprojectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 255, 0),
                                facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.down = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
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
    elif keys[pygame.K_DOWN] and man.y < 800 - man.width - man.vel:
        man.y += man.vel
        man.up = False
        man.down = True
        man.left = False
        man.right = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if man.hp == 0:
        Gameover()
    redrawGameWindow()

pygame.quit()
