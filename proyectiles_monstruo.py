from animaciones import *
from configurar_imagenes import *
from monstruos import *
from personaje import *

class ProyectilMonstruo:
    def __init__(self, x: int, y: int, ancho: int, alto: int, velocidad: int, monstruo):
        self.proyectil = reescalar_imagenes(Imagen.proyectil, ancho, alto)
        self.frame_actual = 0
        self.imagen = self.proyectil[self.frame_actual]
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad

    def actualizar(self):
        self.colisionar_jugador(jugador)
        self.rect.x += self.velocidad

    def colisionar_jugador(self, jugador):
        if self.rect.colliderect(jugador.rect):
            jugador.perder_vida()
        
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
    