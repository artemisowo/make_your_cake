import pygame

pygame.display.init()

pygame.display.set_mode(size=(500, 500), flags=0, display=0, vsync=0)
pygame.display.set_caption("Auxilio")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Check if the user closed the window
            run = False
    pygame.display.update()

pygame.quit()