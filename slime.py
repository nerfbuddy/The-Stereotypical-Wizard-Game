import pygame
#x and y refer to position
#boss is a true/false input determining the size and strength
class Slime(pygame.sprite.Sprite):

    def __init__(self,x,y,boss):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('cwslime1.png')
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.boss=boss
    def move():
        pass
        
test=Slime(0,0,True)
