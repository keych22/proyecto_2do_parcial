import pygame
from animaciones import Imagen
from configurar_imagenes import *
from personaje import *

class Misil:
    def __init__(self, ancho: int, alto: int, delta_x: int, direccion: int, plataformas: list, nivel: str, enemigos: list):
        self.animacion = reescalar_imagenes(Imagen.bumeran, ancho, alto)
        self.frame_actual = 0
        self.rect = self.animacion[self.frame_actual].get_rect()
        self.rect.x = jugador.rect.right if direccion > 0 else jugador.rect.left - self.rect.width
        self.rect.y = jugador.rect.centery
        self.delta_x = delta_x * direccion
        self.plataformas = plataformas
        self.nivel = nivel
        self.enemigos = enemigos

    def actualizar(self):
        self.colisionar_enemigos()
        self.colisionar_plataformas()
        self.frame_actual = (self.frame_actual + 1) % len(self.animacion)
        self.rect.x += self.delta_x

    def colisionar_enemigos(self):
        for misil in self.nivel.misiles_personaje:
            for enemigo in self.enemigos:
                if self.rect.colliderect(enemigo.rect):
                    jugador.puntaje += 100
                    self.nivel.misiles_personaje.remove(misil)
                    self.enemigos.remove(enemigo)

    def colisionar_plataformas(self):
        for misil in self.nivel.misiles_personaje:
            for plataforma in self.plataformas:
                if self.rect.colliderect(plataforma.rect):
                    self.nivel.misiles_personaje.remove(misil)
    
    def dibujar(self, pantalla):
        pantalla.blit(self.animacion[self.frame_actual], self.rect)
