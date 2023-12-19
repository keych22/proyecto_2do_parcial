import pygame
import random
import time
from animaciones import *

class Enemigo:
    def __init__(self):
        self.imagen = pygame.image.load(r"recursos\imagenes\enemigos\1.png")
        self.rect = self.imagen.get_rect()
        self.velocidad_y = 1
        self.tiempo_anterior = time.time()

        # Generar posición y lado aleatorios
        self.lado = random.randint(0, 1)
        self.posicion_y = random.randint(0, pantalla_alto - self.rect.height)

        if self.lado == 0:
            self.posicion_x = 0 - self.rect.width
        else:
            self.posicion_x = pantalla_ancho

    def actualizar(self):
        # Mover verticalmente cada 4 segundos
        tiempo_actual = time.time()
        if tiempo_actual - self.tiempo_anterior >= 4:
            self.velocidad_y *= -1
            self.tiempo_anterior = tiempo_actual

        self.posicion_y += self.velocidad_y

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.posicion_x, self.posicion_y))


# Ejemplo de uso:
pygame.init()

# Configuración de la pantalla
pantalla_ancho = 800
pantalla_alto = 600
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption("Ejemplo de Enemigo")

reloj = pygame.time.Clock()

# Crear un enemigo
enemigo = Enemigo()

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar enemigo
    enemigo.actualizar()

    # Limpiar pantalla
    pantalla.fill((255, 255, 255))

    # Dibujar enemigo
    enemigo.dibujar(pantalla)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(60)

pygame.quit()