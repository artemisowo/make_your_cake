import pygame

# inicializa la pantalla
pygame.display.init()

#configura la pantalla
pygame.display.set_mode(size=(500, 500), flags=0, display=0, vsync=0)
pygame.display.set_caption("Auxilio")

#variable True para bucle
run = True

#mientras que "run" sea true...
while run:
    # bucle que se ejecuta cada vez que el usuario hace una accion (event)
    for event in pygame.event.get():
        # si dicho event es QUIT (cerrar la ventana), run es false (se deja de ejecutar el bucle)
        if event.type == pygame.QUIT:
            run = False
    
    #se actualiza la ventana automáticamente siempre que corra el ciclo
    pygame.display.update()

#se cierra pygame una vez finalizado el ciclo de run
pygame.quit()