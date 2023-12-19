import pygame, random
from configurar_imagenes import *
from animaciones import Imagen
from configuraciones import *
from personaje import *
from disparo_enemigo import DisparoEnemigo

class Enemigo:
    def __init__(self, x: int, y: int, ancho: int, alto: int, velocidad: int, puede_atacar: bool,  imagen_caminando: list[pygame.Surface], imagen_atacando: list[pygame.Surface], puede_disparar: bool,  rango_movimiento: tuple = None):
        self.animacion_camina_derecha = reescalar_imagenes(imagen_caminando, ancho, alto)
        self.animacion_camina_izquierda = girar_imagenes(self.animacion_camina_derecha)

        self.animacion_ataca_derecha = reescalar_imagenes(imagen_atacando, ancho, alto)
        self.animacion_ataca_izquierda = girar_imagenes(self.animacion_ataca_derecha)

        self.animacion_actual = self.animacion_ataca_izquierda
        self.frame_actual = 0
        self.rect = self.animacion_actual[self.frame_actual].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = velocidad
        self.rango_movimiento = rango_movimiento
        self.atacando = False
        self.direccion = 1
        self.puede_atacar = puede_atacar
        self.puede_disparar = puede_disparar

        self.ultimo_disparo = pygame.time.get_ticks() # Tiempo del último disparo en milisegundos
        self.intervalo_disparo = random.randint(2000, 5000) # Intervalo de 1 a 5 segundos

    def disparar(self):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.intervalo_disparo:
            misil_enemigo = DisparoEnemigo(20, 20, 12, self.direccion, self.rect)
            self.ultimo_disparo = tiempo_actual
            return misil_enemigo
        else:
            return None

    def atacar(self, jugador):
        distancia_x = jugador.rect.centerx - self.rect.centerx

        proximidad = 120
        
        if abs(distancia_x) < proximidad:
            if distancia_x > 0 and jugador.rect.top < self.rect.bottom:
                self.atacando = True
                self.animacion_actual = self.animacion_ataca_derecha
            if distancia_x < 0 and jugador.rect.top < self.rect.bottom:
                    self.atacando = True
                    self.animacion_actual = self.animacion_ataca_izquierda
        else:
            self.atacando = False
            self.animacion_actual = self.animacion_camina_derecha

    def colisionar_jugador(self, jugador):
        if self.rect.colliderect(jugador):
            jugador.perder_vida()

    def actualizar(self):
        proyectil = None
        if not jugador.murio:
            self.colisionar_jugador(jugador)
        if self.puede_atacar:
            self.atacar(jugador)
        if self.puede_disparar:
            proyectil = self.disparar()
        if self.rango_movimiento:
            if self.rect.x < self.rango_movimiento[0] or self.rect.x > self.rango_movimiento[1]:
                self.velocidad *= -1
                if self.velocidad > 0:
                    self.direccion = 1
                else:
                    self.direccion = -1
        if not self.atacando:
            self.animacion_actual = self.animacion_camina_derecha if self.velocidad > 0 else self.animacion_camina_izquierda       
        self.frame_actual = (self.frame_actual +
                             1) % len(self.animacion_actual)
        self.rect.x += self.velocidad
        return proyectil

    def dibujar(self, pantalla):
        pantalla.blit(self.animacion_actual[self.frame_actual], self.rect)

enemigos_1 = [
    Enemigo(55, 190, 45, 55, 1, False, Imagen.villano,Imagen.villano, False, (55, 70)),
    Enemigo(225, 185, 45, 55, 1, False, Imagen.villano,Imagen.villano, True, (225, 490)),
    Enemigo(600, ALTO_PANTALLA - 90, 45, 55, 2, False, Imagen.villano,Imagen.villano, True, (600, 1500)),
    Enemigo(-500, ALTO_PANTALLA - 70, 45, 55, 2, False, Imagen.villano,Imagen.villano, True, (-500, 600)),
    Enemigo(-300, ALTO_PANTALLA - 90, 60, 60, 2, False, Imagen.perro, Imagen.perro, False,(-300, 3000)),
    Enemigo(-2000, ALTO_PANTALLA - 80, 60, 60, 2, False, Imagen.perro, Imagen.perro, False,(-2000, 2500)),
    Enemigo(450, 310, 60, 60, 1, True, Imagen.mino_tauro_caminando, Imagen.mino_tauro_atacando,False, (450, 690)),
    Enemigo(0, 420, 60, 60, 1, True, Imagen.mino_tauro_caminando, Imagen.mino_tauro_atacando,False, (0, 100)),
    Enemigo(640, 120, 60, 60, 1, True, Imagen.mino_tauro_caminando, Imagen.mino_tauro_atacando,False, (640, 860))
]

enemigos_2 = [
    Enemigo(790, 50, 95, 80, 1, True, Imagen.zombie_mujer_caminando, Imagen.zombie_mujer_atacando, True, (790, 930)),
    Enemigo(250, 210, 85, 70, 1, True, Imagen.zombie_hombre_caminando, Imagen.zombie_hombre_atacando, False, (250, 385)),
    Enemigo(-200, 370, 95, 80, 1, True, Imagen.zombie_mujer_caminando, Imagen.zombie_mujer_atacando, False, (-200, 160)),
    Enemigo(-150, 130, 95, 80, 1, True, Imagen.zombie_mujer_caminando, Imagen.zombie_mujer_atacando, False, (-150, 130)),
    Enemigo(660, 435, 90, 45, 1, True, Imagen.zombie_hombre_caminando, Imagen.zombie_hombre_atacando, False, (660, 815)),
    Enemigo(-700, 370, 95, 80, 1, True, Imagen.zombie_hombre_caminando, Imagen.zombie_hombre_atacando, False, (-700, 160))
]

enemigos_3 = [
    Enemigo(-100, 50, 50, 40, 4, False, Imagen.cuervo, Imagen.cuervo, False, (-100, 3000)),
    Enemigo(-500, 280, 50, 40, 4, False, Imagen.cuervo, Imagen.cuervo, False, (-500, 2000)),
    Enemigo(-900, 460, 50, 40, 4, False, Imagen.cuervo, Imagen.cuervo, False, (-900, 1500)),
]
