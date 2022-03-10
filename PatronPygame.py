import pygame as pg


pg.init() #Inicialiador de pygame. Siempre debe estar en el código

pantalla = pg.display.set_mode((600,800)) #Creación de nuestra pantalla o lienzo donde vamos a hacer cosas

game_over = False #Booleano para inicializar el bucle

while not game_over: # Bucle del juego
    eventos = pg.event.get() #Detección de los eventos. Lista que captura los eventos. Deben estar en el bucle

    for evento in eventos: # Con este iterador haremos cosas con los eventos
        if evento.type == pg.QUIT: #Evento que produce la salida. Cerrar ventana
            game_over = True

    # Refrescar la pantalla
    pantalla.fill((255,0,0))

    # Paso a la memoria de pantalla para que se dibuje y aparezca en la pantalla
    pg.display.flip()

pg.quit() #Para cerrar la ventana y matar el juego
