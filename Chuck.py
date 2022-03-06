import pygame

pygame.init()
health = 5
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Chuck the Weezard")
# Player
playerImg = pygame.image.load('Generic_Wizard_Frontsprite.png')
x = 50
y = 50
width = 40
height = 60
vel = 2


def redrawGameWindow():
    win.fill((0, 0, 0))  # Fills the screen with black
    win.blit(playerImg, (x, y))
    pygame.display.update()


def Gameover():
    pygame.quit()


# mainloop
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel

    if health == 0:
        Gameover()
    redrawGameWindow()

pygame.quit()
