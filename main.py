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
    background = pygame.transform.scale(background, (screen_width, screen_height))

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

    # Crear una superficie para dibujar la crema (transparente)
    cream_surface = pygame.Surface(base_size, pygame.SRCALPHA)
    cream_surface_rect = base_rect

    # BOTONES PARA ELEGIR BASE
    button_choco_base = pygame.image.load('assets/botones/btn-choco.png').convert_alpha()
    button_choco_base_rect = button_choco_base.get_rect(center=(600, 100))

    button_straw_base = pygame.image.load('assets/botones/btn-straw.png').convert_alpha()
    button_straw_base_rect = button_straw_base.get_rect(center=(600, 220))

    button_vainilla_base = pygame.image.load('assets/botones/btn-vainilla.png').convert_alpha()
    button_vainilla_base_rect = button_vainilla_base.get_rect(center=(600, 340))

    # definir botones (rects fijos) con su clave para seleccionar la base
    button_bases_specs = [
        {'key': 'choco', 'img': button_choco_base, 'rect': button_choco_base_rect},
        {'key': 'straw', 'img': button_straw_base, 'rect': button_straw_base_rect},
        {'key': 'vainilla', 'img': button_vainilla_base, 'rect': button_vainilla_base_rect},
    ]

    # boton de siguiente
    next_button = pygame.image.load('assets/next.png').convert_alpha()
    next_size = (80,80)
    next_button = pygame.transform.scale(next_button, next_size)
    next_button_rect = next_button.get_rect(center=(600, 440))

    # boton de crema drag and drop
    piping_button = pygame.image.load('assets/botones/piping_bag.png').convert_alpha()
    piping_size = (200,200)
    piping_button = pygame.transform.scale(piping_button, piping_size)
    piping_button_rect = piping_button.get_rect(center=(600, 220))

    # manejar condiciones
    piping_visible = False
    piping_dragging = False
    visible_buttons = True
    is_clicked = True

    # config pincel de bolsa de crema
    brush_color = (248, 35, 57)
    brush_size = 10
    last_pos = None
    offset_x = 0
    offset_y = 0

    #bucle para mantener la ventana abierta
    run = True
    while run:
        # bucle que se ejecuta cada vez que el usuario hace una accion (event)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # evitar clicks en botones invisibles
                if is_clicked:
                    # seleccionar base segun boton
                    for spec in button_bases_specs:
                        if spec['rect'].collidepoint(event.pos):
                            base = bases[spec['key']]
                    # manejo de click de siguiente
                    if next_button_rect.collidepoint(event.pos):
                        visible_buttons = False
                        is_clicked = False
                        piping_visible = True

                # código de bolsa de crema        
                if piping_visible:
                    if piping_button_rect.collidepoint(event.pos):
                        piping_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = piping_button_rect.x - mouse_x
                        offset_y = piping_button_rect.y - mouse_y

            # no dragging de bolsa si se suelta
            elif event.type == pygame.MOUSEBUTTONUP:
                if piping_visible:
                    piping_dragging = False
                    last_pos = None

            # mover bolsa mientras que se mantiene clickeada
            elif event.type == pygame.MOUSEMOTION:
                if piping_visible and piping_dragging:
                    mouse_x, mouse_y = event.pos
                    piping_button_rect.x = mouse_x + offset_x
                    piping_button_rect.y = mouse_y + offset_y

                    # Calcular la posición del pico de la bolsa (bottom left)
                    tip_x = piping_button_rect.x + 20
                    tip_y = piping_button_rect.bottom - 20

                    # Verificar si estamos sobre la base del pastel
                    if base_rect.collidepoint((tip_x, tip_y)):
                        # Convertir coordenadas de pantalla a coordenadas de la superficie de crema
                        cream_x = tip_x - base_rect.x
                        cream_y = tip_y - base_rect.y
                        
                        # Dibujar en la superficie de crema
                        if last_pos:
                            pygame.draw.line(cream_surface, brush_color, last_pos, (cream_x, cream_y), brush_size)
                        last_pos = (cream_x, cream_y)
                    else:
                        last_pos = None

        # Copiar imágenes a coords
        screen.blit(background, (0,0))
        screen.blit(table, table_rect)
        screen.blit(base, base_rect)
        screen.blit(cream_surface, cream_surface_rect)  # Dibujar la crema sobre la base

        #botones de elección de bizcocho
        if visible_buttons:
            for spec in button_bases_specs:
                screen.blit(spec['img'], spec['rect'])
            
            # botón de siguiente
            screen.blit(next_button, next_button_rect)

        # botón de bolsa de crema
        if piping_visible:
            screen.blit(piping_button, piping_button_rect)
        
        # actualiza la ventana completa
        pygame.display.flip()

start_game()
pygame.quit()