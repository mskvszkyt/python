import pygame

pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption("Első képernyőm")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
pygame.quit()