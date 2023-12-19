import pygame
from personaje import *
from animaciones import *


class Plataforma:
    def __init__(self, x: int, y: int, ancho: int, alto: int, imagen: dict[str, pygame.Surface]):
        self.foto = reescalar_imagenes(imagen, ancho, alto)
        self.rect = self.foto.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.alto = alto

    def detectar_colision(self, plataformas):
        for plataforma in plataformas:
            if jugador.rect.colliderect(plataforma.rect):
                # Restaurar la posición del jugador si hay una colisión
                if jugador.velocidad_y > 0:
                    if plataforma.rect.right >= jugador.rect.centerx >= plataforma.rect.left:
                        jugador.rect.y = plataforma.rect.y - jugador.ALTURA
                        jugador.velocidad_y = 0
                        jugador.esta_saltando = False
                    else:
                        # Ajusta posicion horizontal para evitar atravesar la plataforma
                        if jugador.rect.centerx < plataforma.rect.left:
                            jugador.rect.right = plataforma.rect.left
                        else:
                            jugador.rect.left = plataforma.rect.right
                # Para que no pueda subir sobre una plataforma estando debajo de ella.
                elif jugador.velocidad_y < 0:
                    jugador.rect.y = plataforma.rect.y + plataforma.alto
                    jugador.velocidad_y = 0

                elif jugador.velocidad_y == 0:
                    if jugador.rect.right >= plataforma.rect.left and jugador.viendo_derecha:
                        jugador.rect.right = plataforma.rect.left
                    if jugador.rect.left <= plataforma.rect.right and not jugador.viendo_derecha:
                        jugador.rect.left = plataforma.rect.right

    def actualizar(self, plataformas):
        self.detectar_colision(plataformas)

    def dibujar(self, pantalla):
        pantalla.blit(self.foto, self.rect)

plataformas_1 = [
    Plataforma(0, 300, 80, 15, Imagen.plataforma["madera_metal"]),
    Plataforma(55, 245, 55, 55, Imagen.plataforma["caja"]),
    Plataforma(200, 375, 50, 50, Imagen.plataforma["caja"]),
    Plataforma(230, 425, 55, 55, Imagen.plataforma["caja"]),
    Plataforma(0, 480, 330, 20, Imagen.plataforma["viga"]),
    Plataforma(450, 370, 300, 40, Imagen.plataforma["bloques"]),
    Plataforma(810, 472, 60, 90, Imagen.plataforma["barril"]),
    Plataforma(225, 240, 320, 30, Imagen.plataforma["bloque_marron"]),
    Plataforma(640, 180, 360, 30, Imagen.plataforma["bloque_marron"])
]

plataformas_2 = [
    Plataforma(470, 480, 50, 50, Imagen.plataforma["caja_2"]),
    Plataforma(950, 360, 50, 50, Imagen.plataforma["caja_2"]),
    Plataforma(0, 450, 220, 150, Imagen.plataforma["monticulo_1"]),
    Plataforma(310, 530, 210, 70, Imagen.plataforma["monticulo_2"]),
    Plataforma(520, 390, 150, 210, Imagen.plataforma["monticulo_3"]),
    Plataforma(670, 480, 220, 120, Imagen.plataforma["monticulo_4"]),
    Plataforma(270, 280, 200, 40, Imagen.plataforma["monticulo_5"]),
    Plataforma(0, 210, 180, 40, Imagen.plataforma["monticulo_6"]),
    Plataforma(565, 210, 145, 40, Imagen.plataforma["monticulo_6"]),
    Plataforma(800, 130, 200, 150, Imagen.plataforma["monticulo_7"]),
    Plataforma(0, 0, 360, 75, Imagen.plataforma["monticulo_8"])
]

plataformas_3 = [
    Plataforma(100, 470, 150, 50, Imagen.plataforma["monticulo_9"]),
    Plataforma(280, 320, 150, 50, Imagen.plataforma["monticulo_9"]),
    Plataforma(480, 400, 150, 50, Imagen.plataforma["monticulo_9"]),
    Plataforma(700, 500, 150, 50, Imagen.plataforma["monticulo_9"])
    # Plataforma(550, 260, 250, 50, Imagen.plataforma["monticulo_9"]),
]
