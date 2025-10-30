import pygame

def rectangulos(screen, color):
    rect = pygame.draw.rect(screen, color, (50, 50, 100, 100))
    return rect

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
    base_vainilla = pygame.image.load('assets/bases/base-vainilla.png').convert_alpha()
    base_size = (350, 350)
    base = pygame.transform.scale(base_vainilla, base_size)
    base_rect = base.get_rect()
    base_rect.center = ((screen_width // 2) - 150, (screen_height // 2))

    #otras opciones de bases
    base_choco = pygame.image.load('assets/bases/base-chocolate.png').convert_alpha()
    base_straw = pygame.image.load('assets/bases/base-strawberry.png').convert_alpha()

    #colores de fondo de prueba
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)

    #bucle para mantener la ventana abierta
    run = True
    while run:
        # bucle que se ejecuta cada vez que el usuario hace una accion (event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_choco_base.collidepoint(event.pos):
                    base = base_choco
                    base = pygame.transform.scale(base, base_size)
                elif btn_straw_base.collidepoint(event.pos):
                    base = base_straw
                    base = pygame.transform.scale(base, base_size)
                elif btn_vainilla_base.collidepoint(event.pos):
                    base = base_vainilla
                    base = pygame.transform.scale(base, base_size)
        
        # Copiar imágenes a coords
        screen.blit(background, (0,0))
        screen.blit(table, table_rect)
        screen.blit(base, base_rect)
        
        #botones de prueba
        btn_choco_base = pygame.draw.rect(screen, RED, (500, 50, 100, 100))
        btn_straw_base = pygame.draw.rect(screen, BLUE, (500, 200, 100, 100))
        btn_vainilla_base = pygame.draw.rect(screen, GREEN, (500, 350, 100, 100))

        # actualiza la ventana completa
        pygame.display.flip()

start_game()
pygame.quit()