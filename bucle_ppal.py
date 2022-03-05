import pygame as pg

pg.init()

pantalla = pg.display.set_mode((600,800))

game_over = False
x = 300
y = 400

velocidad_x = 1
velocidad_y = 1

while not game_over:
    eventos = pg.event.get() # Muy importante para que no se quede colgado porque si no los eventos no se gestionan

    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True

    # Modificar los objetos del juego
    x += velocidad_x
    y += velocidad_y

    # Gestión de los bordes del juego para rebotar
    if x >= 600 - 10 or x <= 0 + 10:
        velocidad_x *= -1

    if y >= 800 - 10 or y <= 0 + 10:
        velocidad_y *= -1

    
    # Aquí no hay nada que hacer

    # Refresca la pantalla
    pantalla.fill((255,0,0))
    bola = pg.draw.circle(pantalla,(255, 255, 0),(x,y),10)
    
    pg.display.flip() # Importante para refrescar pantalla porque si no no se actualiza lo que aparece por la pantalla

pg.quit()

