import pygame, random
from configurar_imagenes import *
from configuraciones import *
from animaciones import Imagen
from proyectiles_monstruo import ProyectilMonstruo

class Monstruo:
    def __init__(self, ancho_monstruo, alto_monstruo, pantalla_ancho: int, pantalla_alto: int, imagen_monstruo):
        self.imagen_izquierda = reescalar_imagenes(imagen_monstruo, ancho_monstruo, alto_monstruo)  # Puedes reemplazar esto con la imagen del enemigo
        self.imagen_derecha = pygame.transform.flip(self.imagen_izquierda, True, False)
        self.imagen_actual = self.imagen_izquierda
        self.rect = self.imagen_actual.get_rect()
        self.pantalla_ancho = pantalla_ancho
        self.pantalla_alto = pantalla_alto
        self.intervalo_disparo = 1000
        self.ultimo_disparo = pygame.time.get_ticks()
        self.vidas_monstruo = 5
        self.lista_disparos = []

        self.velocidad_y = 3  # Velocidad de movimiento vertical
        self.tiempo_movimiento = 12000  # Tiempo en milisegundos para cambiar de dirección

        # Definir posición inicial aleatoria
        self.rect.x = random.choice([0, pantalla_ancho - self.rect.width])
        self.rect.y = random.randint(0, pantalla_alto - self.rect.height)

        # Guardar el tiempo actual para el siguiente cambio de dirección
        self.tiempo_cambio = pygame.time.get_ticks() + self.tiempo_movimiento

    def disparar(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.intervalo_disparo:
            if self.rect.x == 0:
                proyectil_monstruo = ProyectilMonstruo(self.rect.right, self.rect.centery, 25, 25, 12, self.rect)
                self.lista_disparos.append(proyectil_monstruo)
                self.ultimo_disparo = tiempo_actual
            else:
                proyectil_monstruo = ProyectilMonstruo(self.rect.left, self.rect.centery, 25, 25, -12, self.rect)
                self.lista_disparos.append(proyectil_monstruo)
                self.ultimo_disparo = tiempo_actual

    def actualizar(self):
        self.disparar()
        # Verificar si es el momento de cambiar de dirección
        if pygame.time.get_ticks() >= self.tiempo_cambio:
            self.velocidad_y *= -1  # Cambiar la dirección del movimiento
            self.tiempo_cambio = pygame.time.get_ticks() + self.tiempo_movimiento

        # Mover verticalmente
        self.rect.y += self.velocidad_y

        if self.rect.x == self.pantalla_ancho - self.rect.width:
            self.imagen_actual = self.imagen_izquierda
        else:
            self.imagen_actual = self.imagen_derecha

        # Verificar si el enemigo ha salido de la pantalla y reposicionarlo
        if self.rect.bottom <= 0 or self.rect.top >= self.pantalla_alto:
            self.rect.x = random.choice([0, self.pantalla_ancho - self.rect.width])
            self.rect.y = random.randint(0, self.pantalla_alto - self.rect.height)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen_actual, self.rect)

monstruo = Monstruo(110, 140, ANCHO_PANTALLA, ALTO_PANTALLA, Imagen.monstruo)
