import pygame as pg
from ARKANOID.entities import Bola, Raqueta, Ladrillo
from ARKANOID import FPS, niveles


class Game:
    def __init__(self, ancho = 600, alto = 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.titulo = pg.display.set_caption("Juego Raquetas")
        self.bola = Bola(self.pantalla,ancho // 2, alto // 2, (255,255,0))
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto-30, 100,15)
        self.ladrillos = []  
        self.contador_vidas = 3    

        self.reloj = pg.time.Clock()

    # Pinta 4 filas de 10 columnas de ladrillos. 40 ladrillos
    """def CreaLadrillos(self):
        for col in range(10):
            for fil in range(4):
                l = Ladrillo(self.pantalla, 5 + 60 * col, 20 + 30 * fil, 50, 20)
                self.ladrillos.append(l)
    """
    
    # Pinta mapa de ladrillos de mapa_nivel
    def CreaLadrillos(self, nivel):
        for col, fil in niveles[nivel]:
            l = Ladrillo(self.pantalla, 5 + 60 * col, 20 + 30 * fil, 50, 20)
            self.ladrillos.append(l)
            

    def bucle_ppal(self):
        game_over = False
        nivel = 0
        
        while self.contador_vidas > 0 and not game_over and nivel < len(niveles):
            self.bola.reset()
            self.CreaLadrillos(nivel)

            while self.contador_vidas > 0 and not game_over and len(self.ladrillos) > 0:

                # Comprueba que la lista de la drillos está vacia cuando se acaban todos y sale del programa
                if len(self.ladrillos) == 0:
                    game_over = True

                # Ajuste de los FPS a 60
                milisegundos = self.reloj.tick(FPS)
                

                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        game_over = True

                self.pantalla.fill ((255,0,0))
                
                self.bola.mover()
                self.raqueta.mover()
                self.bola.compruebaChoque(self.raqueta)
                if not self.bola.esta_viva:
                    self.contador_vidas -= 1
                    self.bola.reset()
                
                self.bola.dibujar()
                self.raqueta.dibujar()
            
                for ladrillo in self.ladrillos:
                    if ladrillo.comprobarToque(self.bola):
                        self.ladrillos.remove(ladrillo)
                    ladrillo.dibujar()
                
                
                                
                

                pg.display.flip()
            nivel += 1
