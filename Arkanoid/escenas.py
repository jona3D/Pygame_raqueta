import pygame as pg

from Arkanoid.entities import Bola, Raqueta, Ladrillo
from Arkanoid import niveles, FPS


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.titulo = pg.display.set_caption("Juego Arkanoid")
        self.reloj = pg.time.Clock()

    def bucle_ppal() -> bool:
        pass

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.bola = Bola(self.pantalla,self.pantalla.get_width()// 2, 
                        self.pantalla.get_height() // 2)
        self.raqueta = Raqueta(self.pantalla,self.pantalla.get_width()// 2, 
                        self.pantalla.get_height() -30, 100,15)
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
        
        while self.contador_vidas > 0 and nivel < len(niveles):
            self.bola.reset()
            self.CreaLadrillos(nivel)

            while self.contador_vidas > 0 and len(self.ladrillos) > 0:

                # Comprueba que la lista de la drillos está vacia cuando se acaban todos y sale del programa
                if len(self.ladrillos) == 0:
                    game_over = True

                # Ajuste de los FPS a 60
                milisegundos = self.reloj.tick(FPS)
                

                eventos = pg.event.get()
                for evento in eventos:
                    if evento.type == pg.QUIT:
                        return False

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


class GameOver(Escena):
    def __init__(self, pantalla):
        pg.Rect
        super().__init__(pantalla)
        self.fuente = pg.font.Font("resources/fonts/FredokaOne-Regular.ttf", 25)

    def bucle_ppal(self):
        while True:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    return False

                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        return True

            self.pantalla.fill((30,30,255))
            texto = self.fuente.render("GAME OVER", True, (255,255,0))
            rectexto = texto.get_rect()

            self.pantalla.blit(texto, (10,10))

            pg.display.flip()