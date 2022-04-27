import pygame
import random
pygame.init()

win=pygame.display.set_mode((800,600))

pygame.display.set_caption("Test Shell")

###################################
class Slime(pygame.sprite.Sprite):

    def __init__(self,x,y,boss):
        pygame.sprite.Sprite.__init__(self)
        self.frames=['cwslime1.png','cwslime2.png','cwslime3.png']
        self.bframes=['cwboss1.png','cwboss2.png','cwboss3.png']
        self.n=0
        self.x=x
        self.y=y
        self.gx=0
        self.gy=0
        self.boss=boss
        if self.boss == True:
            self.image = pygame.image.load(self.bframes[self.n])
            self.lwid = 544
            self.lhei = 344
            self.hp = 5
        else:
            self.image = pygame.image.load(self.frames[self.n])
            self.lwid = 672
            self.lhei = 472
            self.hp = 1
        self.rect=self.image.get_rect()
    def rangen_x(self):
        self.gx=random.randint(0,self.lwid)
        
    def rangen_y(self):
        self.gy=random.randint(0,self.lhei)
        
    def move(self):
        if self.x < self.gx:
                self.x+=1
        elif self.x > self.gx:
                self.x-=1
        else:
            self.rangen_x()
            
        if self.y < self.gy:
                self.y+=1
        elif self.y > self.gy:
                self.y-=1
        else:
            self.rangen_y()
        self.rect=self.image.get_rect()
    def animate(self):
        if self.n>=2:
            self.n=0
        self.n+=1
        if self.boss == True:
            self.image = pygame.image.load(self.bframes[self.n])
        else:
            self.image = pygame.image.load(self.frames[self.n])



test=Slime(0,0,True)
smol = Slime(400,300,False)
boi = Slime(600, 400,False)
###################################

run=True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

    #####################################
    for x in range(5):
        test.move()
        smol.move()
        boi.move()
    test.animate()
    smol.animate()
    boi.animate()
    #####################################

    pygame.draw.rect(win, (0,0,0), pygame.Rect(0,0,800,600))
    win.blit(test.image,(test.x,test.y))
    win.blit(smol.image,(smol.x,smol.y))
    win.blit(boi.image,(boi.x,boi.y))
    
    pygame.display.update()

pygame.quit()
