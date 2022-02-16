import pygame

pygame.init()
screen = pygame.display.set_mode((1260, 720))

pygame.display.set_caption("Example game")
icon = pygame.image.load('Gandalf.jpeg')
pygame.display.set_icon(icon)

running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
