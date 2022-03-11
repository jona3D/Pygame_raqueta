import pygame as pg

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
           