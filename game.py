import pygame as pg
pg.init()

class Bola:
    def __init__(self, padre: pg.Surface, x, y, color = (255,255,255), radio = 10):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = 1
        self.vy = 1
        self.padre = padre

        
    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self):
        pg.draw.circle(self.padre,self.color,
                (self.x, self.y), self.radio)

class Raqueta:
    def __init__(self, padre, x, y, ancho, alto,color = (255,255,0)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 1
        self.vy = 0

    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.x -= self.vx
        if teclas[pg.K_RIGHT]:
            self.x += self.vx

        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho

class Game:
    def __init__(self, ancho = 600, alto = 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.titulo = pg.display.set_caption("Juego Raquetas")
        self.bola = Bola(self.pantalla,ancho // 2, alto // 2, (255,255,0))
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto-30, 100,15)
          
    
    def bucle_ppal(self):
        game_over = False
        
        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

                """if evento.type == pg.KEYDOWN:
                    if evento.type == pg.K_LEFT:
                        self.raqueta.x -= self.raqueta.vx
                    
                    if evento.type == pg.K_RIGHT:
                        self.raqueta.x += self.raqueta.vx

                if evento.type == pg.KEYUP:
                    if evento.key in (pg.K_LEFT, pg.K_RIGHT):
                        self.raqueta.vx = 0"""


            self.bola.mover()
            self.raqueta.mover()
            self.pantalla.fill ((255,0,0))
            self.bola.dibujar()
            self.raqueta.dibujar()
            

            pg.display.flip()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()

    pg.quit()