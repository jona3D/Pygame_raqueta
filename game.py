import pygame as pg
pg.init()

# Clase patron para generar las otras clases de objetos del juego
class Vigneta:
    def __init__(self, padre, x, y, ancho, alto,color = (255,255,255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 0
        self.vy = 0

    def dibujar(self):
        pass

    def mover(self):
        pass

    def intersecta(self, otro):
        return (self.x in range(otro.x, otro.x + otro.ancho) or\
                self.x + self.ancho in range(otro.x, otro.x + otro.ancho)) and \
                (self.y in range(otro.y, otro.y + otro.alto) or \
                self.y + self.alto in range(otro.y, otro.y + otro.alto))

    

class Bola(Vigneta):
    def __init__(self, padre: pg.Surface, x, y, color = (255,255,255), radio = 10):
        super().__init__(padre, x-radio, y-radio,2*radio, 2*radio)
        self.radio = radio
        self.vx = 5
        self.vy = 5
        self.x_ini = x
        self.y_ini = y
        self.esta_viva = True

    def reset(self):
        self.x = self.x_ini
        self.y = self.y_ini
        self.vx = 5
        self.vy = 5
        self.esta_viva = True
        
        
    def mover(self):
        self.x += self.vx
        self.y += self.vy

        # Detección de colisión con laterales de la ventana
        if self.x <= 0 or self.x >= self.padre.get_width() - self.ancho:
            self.vx *= -1

        if self.y <= 0:
            self.vy *= -1

        if self.y >= self.padre.get_height() - self.alto:
            self.esta_viva = False

    def dibujar(self):
        pg.draw.circle(self.padre,self.color,(self.x + self.radio, self.y + self.radio), self.radio)

    # Comprobar choques con otro objeto
    def compruebaChoque(self, otro):
        if self.intersecta(otro):           
           self.vy *= -1
           



class Raqueta(Vigneta):
    def __init__(self, padre, x, y, ancho, alto,color = (255,255,0)):
        super().__init__(padre, x, y, ancho, alto, color)
        self.vx = 5
        

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
        if self.x + self.ancho >= self.padre.get_width(): # get_width -> Metodo de surface que devuelve el límite de la surface
            self.x = self.padre.get_width() - self.ancho

class Ladrillo(Vigneta):
    def __init__(self, padre, x, y, ancho, alto, color = (255,255,255)):
        super().__init__(padre, x, y, ancho, alto, color)
        self.vivo = True

    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def comprobarToque(self, bola):
        if self.intersecta(bola):
           bola.vy *= -1
           self.color=(60,60,60)
           self.vivo = False
           return True
        
        return False
           


class Game:
    def __init__(self, ancho = 600, alto = 800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.titulo = pg.display.set_caption("Juego Raquetas")
        self.bola = Bola(self.pantalla,ancho // 2, alto // 2, (255,255,0))
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto-30, 100,15)
        self.ladrillos = []  
        self.contador_vidas = 3

        self.CreaLadrillos()
    

        self.reloj = pg.time.Clock()

    def CreaLadrillos(self):
        for col in range(10):
            for fil in range(4):
                l = Ladrillo(self.pantalla, 5 + 60 * col, 20 + 30 * fil, 50, 20)
                self.ladrillos.append(l)
    

    def bucle_ppal(self):
        game_over = False
        
        while self.contador_vidas > 0 and not game_over:

            # Ajuste de los FPS a 60
            milisegundos = self.reloj.tick(60)
            

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
                if ladrillo.vivo:
                    ladrillo.comprobarToque(self.bola)
                    ladrillo.dibujar()
                
                            
            

            pg.display.flip()


if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucle_ppal()

    pg.quit()