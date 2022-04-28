import pygame
import random

pygame.init()
health = 5
win = pygame.display.set_mode((1000, 1000))
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
        self.hitbox = (self.x + 20, self.y, 28, 60)

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
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


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
        self.hitbox = (self.x + 20, self.y, 28, 60)
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

    def hit(self):
        print('hit')


def hitCheck(slimes, bullets):
    for s in range(len(slimes)):
        for bullet in bullets:
            if pygame.Rect.colliderect(slimes[s].rect, bullet.rect):
                slimes[s].hp -= 1
        if slimes[s].hp <= 0:
            slimes.pop(s)
            bullets.pop(bullets.index(bullet))


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    for slime in slimes:
        for x in range(3):
            slime.move()
        slime.animate()
        win.blit(slime.image, (slime.x, slime.y))
    hitCheck(slimes, bullets)
    pygame.display.update()


def Gameover():
    pygame.quit()


# mainloop
man = player(200, 410, 64, 64)
bullets = []
shootLoop = 0
o = Slime(60, 60, False)
slimes = []
slimes.append(o)
run = True
while run:
    clock.tick(27)
    pygame.time.delay(10)

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.y - bullet.radius < o.hitbox[1] + o.hitbox[3] and bullet.y + bullet.radius > o.hitbox[1]:
            if bullet.x + bullet.radius > o.hitbox[0] and bullet.x - bullet.radius < o.hitbox[0] + o.hitbox[2]:
                o.hit()  # calls enemy hit method
                bullets.pop(bullets.index(bullet))  # removes bullet from bullet list
        if man.left or man.right:
            if 1000 > bullet.x > 0:
                bullet.x += bullet.vel
                bullet.rect = pygame.Rect(bullet.x, bullet.y, bullet.radius, bullet.radius)
            else:
                bullets.pop(bullets.index(bullet))
        else:
            if 1000 > bullet.x > 0:
                bullet.y += bullet.vel
                bullet.rect = pygame.Rect(bullet.x, bullet.y, bullet.radius, bullet.radius)
            else:
                bullets.pop(bullets.index(bullet))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
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
