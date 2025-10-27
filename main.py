import pygame

def start_game():
    # inicializa la pantalla
    pygame.display.init()
    screen_width = 735
    screen_height = 490

    #configura e inicializa la pantalla
    screen = pygame.display.set_mode(size=(screen_width, screen_height))
    pygame.display.set_caption("Make your cake")

    #cargar imagen de fondo
    background = pygame.image.load('assets/bg.jpg').convert()
    background = pygame.transform.scale( background, (screen_width, screen_height))

    #cargar imagen de mesa modo png y posicionar
    table = pygame.image.load('assets/table.png').convert_alpha()
    tamaño_mesa = (600, 600)
    table = pygame.transform.scale(table, tamaño_mesa)
    table_rect = table.get_rect()
    table_rect.center = ((screen_width // 2) - 150, (screen_height // 2) + 220)

    #cargar base png y posicionar
    base = pygame.image.load('assets/bases/base-vainilla.png').convert_alpha()
    base_size = (350, 350)
    base = pygame.transform.scale(base, base_size)
    base_rect = base.get_rect()
    base_rect.center = ((screen_width // 2) - 150, (screen_height // 2))

    #bucle para mantener la ventana abierta
    run = True
    while run:
        # bucle que se ejecuta cada vez que el usuario hace una accion (event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Copiar imágenes a coords
        screen.blit(background, (0,0))
        screen.blit(table, table_rect)
        screen.blit(base, base_rect)

        # actualiza la ventana completa
        pygame.display.flip()

start_game()
pygame.quit()