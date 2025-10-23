import pygame

# inicializa la pantalla
pygame.display.init()

# dimensiones de la pantalla
screen_width = 735
screen_height = 490

#configura e inicializa la pantalla
screen = pygame.display.set_mode(size=(screen_width, screen_height))
pygame.display.set_caption("Auxilio")

#imagen de fondo
background = pygame.image.load('assets/bg.jpg').convert()
background = pygame.transform.scale( background, (screen_width, screen_height))

#bucle para mantener la ventana abierta
run = True

while run:
    # bucle que se ejecuta cada vez que el usuario hace una accion (event)
    for event in pygame.event.get():
        # si dicho event es QUIT (cerrar la ventana), run es false (se deja de ejecutar el bucle)
        if event.type == pygame.QUIT:
            run = False

    screen.blit(background, (0,0))

    pygame.display.flip()

#se cierra pygame una vez finalizado el ciclo de run
pygame.quit()