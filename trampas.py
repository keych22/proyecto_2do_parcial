import pygame
from animaciones import pygame
from personaje import pygame
from plataformas import *


class Trampa(Plataforma):
    def __init__(self, x: int, y: int, ancho: int, alto: int, imagen: dict[str, pygame.Surface], nombre_trampa: str):
        super().__init__(x, y, ancho, alto, imagen)

    def colisionar_jugador(self, jugador):
        if self.rect.colliderect(jugador):
            jugador.perder_vida()

    def actualizar(self):
        if not jugador.murio:
            self.colisionar_jugador(jugador)


trampas_1 = [Trampa(155, 430, 65, 50, Imagen.trampa["cuchillas"], "cuchillas"),
           Trampa(818, 525, 80, 90, Imagen.trampa["sustancia"], "sustancia")
           ]

trampas_2 = [
    Trampa(215, 565, 100, 35, Imagen.trampa["lanzas"], "lanzas"),
    Trampa(890, 565, 110, 35, Imagen.trampa["lanzas"], "lanzas")
]

trampas_3 = [Trampa(10, 700, 100, 35, Imagen.trampa["cuchillas_3"], "cuchillas_3"),]
