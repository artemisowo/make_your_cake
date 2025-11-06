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
    base_vainilla = pygame.image.load('assets/bases/base-vainilla.png').convert_alpha()
    base_size = (350, 350)
    
    #otras opciones de bases
    base_choco = pygame.image.load('assets/bases/base-chocolate.png').convert_alpha()
    base_straw = pygame.image.load('assets/bases/base-strawberry.png').convert_alpha()

    # Escalar todas las bases una vez
    bases = {
        'choco': pygame.transform.scale(base_choco, base_size),
        'straw': pygame.transform.scale(base_straw, base_size),
        'vainilla': pygame.transform.scale(base_vainilla, base_size)
    }

    base = bases['vainilla']
    base_rect = base.get_rect()
    base_rect.center = ((screen_width // 2) - 150, (screen_height // 2))

    # BOTONES PARA ELEGIR BASE
    button_choco_base = pygame.image.load('assets/botones/btn-choco.png').convert_alpha()
    button_choco_base_rect = button_choco_base.get_rect(center = (600, 100))

    button_straw_base = pygame.image.load('assets/botones/btn-straw.png').convert_alpha()
    button_straw_base_rect = button_straw_base.get_rect(center = (600, 220))

    button_vainilla_base = pygame.image.load('assets/botones/btn-vainilla.png').convert_alpha()
    button_vainilla_base_rect = button_straw_base.get_rect(center = (600, 340))

    # definir botones (rects fijos) con su clave para seleccionar la base
    button_bases_specs = [
        {'key': 'choco', 'img': button_choco_base, 'rect': button_choco_base_rect},
        {'key': 'straw', 'img': button_straw_base, 'rect': button_straw_base_rect},
        {'key': 'vainilla', 'img': button_vainilla_base, 'rect': button_vainilla_base_rect},
    ]

    #bucle para mantener la ventana abierta
    run = True
    while run:
        # bucle que se ejecuta cada vez que el usuario hace una accion (event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for spec in button_bases_specs:
                    if spec['rect'].collidepoint(event.pos):
                        base = bases[spec['key']]
        
        # Copiar imágenes a coords
        screen.blit(background, (0,0))
        screen.blit(table, table_rect)
        screen.blit(base, base_rect)
        
        #botones de prueba
        for spec in button_bases_specs:
            screen.blit(spec['img'], spec['rect'])

        # actualiza la ventana completa
        pygame.display.flip()

start_game()
pygame.quit()