import pygame
from configuraciones import *
from configurar_imagenes import *
from animaciones import *
from botones import *

class Personaje:
    ANCHO_JUGADOR = 45
    ALTURA = 60
    # TODO --> Agregar velocidad en x de argumento como parametro al constructor
    def __init__(self, x: int, y: int, velocidad_corriendo: int, velocidad_saltando: int):

        self.personaje_quieto_derecha = reescalar_imagenes(
            Imagen.personaje_quieto_derecha, self.ANCHO_JUGADOR, self.ALTURA)
        self.personaje_quieto_izquierda = girar_imagenes(
            self.personaje_quieto_derecha)
        self.personaje_corre_derecha = reescalar_imagenes(
            Imagen.personaje_corre_derecha, self.ANCHO_JUGADOR, self.ALTURA)
        self.personaje_corre_izquierda = girar_imagenes(self.personaje_corre_derecha)
        self.personaje_salta_derecha = reescalar_imagenes(
            Imagen.personaje_salta_derecha, self.ANCHO_JUGADOR, self.ALTURA)
        self.personaje_salta_izquierda = girar_imagenes(
            self.personaje_salta_derecha)
        
        # modificar valores ancho y alto:
        self.personaje_muere_derecha = reescalar_imagenes(Imagen.personaje_muere_derecha, self.ANCHO_JUGADOR, self.ALTURA)
        self.personaje_muere_izquierda = girar_imagenes(self.personaje_muere_derecha)

        self.personaje_toma_derecha = reescalar_imagenes(Imagen.personaje_toma_derecha, self.ANCHO_JUGADOR, self.ALTURA)
        self.personaje_toma_izquierda = girar_imagenes(self.personaje_toma_derecha)

        self.frame_actual = 0
        self.animaciones_actual = self.personaje_quieto_derecha
        self.rect = self.animaciones_actual[self.frame_actual].get_rect(topleft = (x,y))

        self.viendo_derecha = True
        self.direccion = 1 # TODO Para cambiar la direccion del disparo
        self.velocidad_y = 0
        self.velocidad_x = velocidad_corriendo
        self.velocidad_saltando = velocidad_saltando
        self.esta_saltando = False
        self.murio = False
        self.vidas = 3
        self.puntaje = 0
        self.ultimo_tiempo = 0
        self.velocidad_frame = 200
        self.armado = False
        self.tomo_bebida = False
        self.poder_salto = False

    def quieto(self):
        if self.viendo_derecha:
            self.animaciones_actual = self.personaje_quieto_derecha
        else:
            self.animaciones_actual = self.personaje_quieto_izquierda

    def mover_derecha(self):
        self.viendo_derecha = True
        self.direccion = 1
        self.animaciones_actual = self.personaje_corre_derecha 
        if self.rect.right < ANCHO_PANTALLA: # Limita la parte derecha de la pantalla
            if not self.esta_saltando: # Para que si esta en el aire no pueda correr
                self.rect.x += self.velocidad_x                                    
            elif self.esta_saltando: # Para que en el aire el alcance sea una distancia prudente
                self.rect.x += self.velocidad_saltando

    def mover_izquierda(self):
        self.viendo_derecha = False
        self.direccion = -1
        self.animaciones_actual = self.personaje_corre_izquierda 
        if self.rect.left > 0: # Limita la parte izquierda de la pantalla
            if not self.esta_saltando: # Para que si esta en el aire no pueda correr
                self.rect.x -= self.velocidad_x
            elif self.esta_saltando: # Para que en el aire el alcance sea una distancia prudente
                self.rect.x -= self.velocidad_saltando

    def saltar(self):
        if not self.esta_saltando and self.velocidad_y == 0 and not self.poder_salto: # velocidad_y = 0 para que no pueda saltar en el aire
            self.esta_saltando = True
            self.velocidad_y = -17
        elif self.velocidad_y == 0: 
            self.velocidad_y = -18
            self.esta_saltando = True
            
    def aplicar_gravedad(self):
        if self.esta_saltando:
            self.animaciones_actual = self.personaje_salta_derecha if self.viendo_derecha else self.personaje_salta_izquierda

        if self.rect.y < PISO - self.ALTURA or self.velocidad_y < 0:
            self.velocidad_y += 1
        else:
            self.velocidad_y = 0  # Lo frena si esta en el piso
            self.esta_saltando = False
            self.rect.y = PISO - self.ALTURA

    def perder_vida(self):
        self.murio = True
        self.vidas -= 1
        self.frame_actual = 0
        self.poder_salto = False
        self.ultimo_tiempo = pygame.time.get_ticks()

        if self.puntaje > 0:
            self.puntaje -= 50

        if self.viendo_derecha:
            self.animaciones_actual = self.personaje_muere_derecha
        else:
            self.animaciones_actual = self.personaje_muere_izquierda

    def tomar(self):
        self.tomo_bebida = True
        self.ultimo_tiempo = pygame.time.get_ticks()
        self.frame_actual = 0
        if self.viendo_derecha:
            self.animaciones_actual = self.personaje_toma_derecha
        else:
            self.animaciones_actual = self.personaje_toma_izquierda


    def actualizar(self): # TODO --> Eliminar luego comentario
        tiempo_actual = pygame.time.get_ticks()

        if not self.murio:
            self.aplicar_gravedad()  
            self.rect.y += self.velocidad_y  # Actualizar posicion del jugador

        if self.murio:
            if tiempo_actual - self.ultimo_tiempo >= 200:
                self.frame_actual += 1
                self.ultimo_tiempo = tiempo_actual
                if self.frame_actual >= len(self.animaciones_actual):
                    self.frame_actual = len(self.animaciones_actual) - 1
                    if boton_nivel_1.nivel_actual == 1:
                        self.rect.x = 300
                        self.rect.y = 420
                        self.murio = False
                    elif boton_nivel_2.nivel_actual == 2:
                        self.rect.x = 390
                        self.rect.y = 420
                        self.murio = False
                    elif boton_nivel_3.nivel_actual == 3:
                        self.rect.x = 390
                        self.rect.y = 420
                        self.murio = False

        elif self.tomo_bebida:
            if tiempo_actual - self.ultimo_tiempo >= self.velocidad_frame:
                self.frame_actual += 1
                self.ultimo_tiempo = tiempo_actual
                if self.frame_actual >= len(self.animaciones_actual):
                    self.frame_actual = len(self.animaciones_actual) - 1
                    self.tomo_bebida = False

        else:
            self.frame_actual = (self.frame_actual + 1) % len(self.animaciones_actual)
        
    def dibujar(self, pantalla):
        pantalla.blit(self.animaciones_actual[self.frame_actual], self.rect)

jugador = Personaje(380, 470, 8, 4)

