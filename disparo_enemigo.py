import pygame
from configurar_imagenes import *
from animaciones import *
from enemigos import *
from personaje import *

class DisparoEnemigo:
    def __init__(self, ancho: int, alto: int, velocidad: int, direccion: int, enemigo: pygame.Rect):
        self.proyectil = reescalar_imagenes(Imagen.proyectil, ancho, alto)
        self.frame_actual = 0
        self.imagen = self.proyectil[self.frame_actual]
        self.rect = self.imagen.get_rect()
        self.rect.x = enemigo.right if direccion > 0 else enemigo.left - self.rect.width
        self.rect.y = enemigo.centery
        self.velocidad = velocidad * direccion

    def actualizar(self):
        self.rect.x += self.velocidad

    def colisionar_jugador(self, jugador):
        return self.rect.colliderect(jugador.rect)
    
    def dibujar(self, pantalla):
        pantalla.blit(self.proyectil[self.frame_actual], self.rect)
    

