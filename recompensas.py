import pygame
from animaciones import pygame
from configurar_imagenes import pygame
from objetos import Objeto
from personaje import pygame
from animaciones import Imagen
from botones import *

class Recompensa(Objeto):
    tiempo_colision = None
    def __init__(self, x: int, y: int, ancho: int, alto: int, ruta_imagen: pygame.Surface, nombre_objeto: str):
        super().__init__(x, y, ancho, alto, ruta_imagen, nombre_objeto)

    def detectar_colision(self, jugador):  # Método adicional específico de esta clase
        if self.rect.colliderect(jugador):
            if self.nombre == "red_bull":
                self.esta = False
                # jugador.tomo_bebida = True
                jugador.poder_salto = True
                jugador.tomar()
                recompensas_1.remove(self)
                Recompensa.tiempo_colision = pygame.time.get_ticks()
            elif self.nombre == "auxilio":
                recompensas_1.remove(self) 
                self.esta = False
                if jugador.vidas == 2:
                    jugador.vidas += 1
                    recompensas_1.append(vida_3)
                if jugador.vidas == 1:
                    jugador.vidas += 1
                    recompensas_1.append(vida_2)
            elif self.nombre == "moneda":
                recompensas_2.remove(self) 
                jugador.puntaje += 100
                self.esta = False
            elif self.nombre == "diamante":
                recompensas_2.remove(self) 
                jugador.puntaje += 150
                self.esta = False
            elif self.nombre == "diamante_3":
                recompensas_3.remove(self) 
                jugador.puntaje += 150
                self.esta = False
            elif self.nombre == "pizza":
                recompensas_3.remove(self) 
                jugador.puntaje += 100
                self.esta = False
            elif self.nombre == "coca_cola":
                recompensas_3.remove(self) 
                jugador.puntaje += 100
                self.esta = False
            elif self.nombre == "bitcoin":
                jugador.puntaje += 150
                self.esta = False
                recompensas_1.remove(self)

    def desaparecer_recompensa(self, jugador):
        if self.tiempo_colision is not None:
            tiempo_actual = pygame.time.get_ticks()         
            if tiempo_actual - self.tiempo_colision >= 12000 and self.nombre == "auxilio":
                recompensas_1.remove(self)
        elif boton_nivel_1.nivel_actual == 1:
            if self.nombre == "vida_3" and jugador.vidas == 2:
                recompensas_1.remove(self)
            if self.nombre == "vida_2" and jugador.vidas == 1:
                recompensas_1.remove(self)
            if self.nombre == "vida_1" and jugador.vidas == 0:
                recompensas_1.remove(self)
        elif boton_nivel_2.nivel_actual == 2:
            if self.nombre == "vida_6" and jugador.vidas == 2:
                recompensas_2.remove(self)
            if self.nombre == "vida_5" and jugador.vidas == 1:
                recompensas_2.remove(self)
            if self.nombre == "vida_4" and jugador.vidas == 0:
                recompensas_2.remove(self)
        elif boton_nivel_3.nivel_actual == 3:
            if self.nombre == "vida_9" and jugador.vidas == 2:
                recompensas_3.remove(self)
            if self.nombre == "vida_8" and jugador.vidas == 1:
                recompensas_3.remove(self)
            if self.nombre == "vida_7" and jugador.vidas == 0:
                recompensas_3.remove(self)

    def actualizar(self, jugador):
        self.detectar_colision(jugador)
        self.desaparecer_recompensa(jugador)

red_bull = Recompensa(5, 430, 50, 55, Imagen.recompensa["red_bull"], "red_bull")
bitcoin = Recompensa(115, 255, 25, 25, Imagen.recompensa["bitcoin"], "bitcoin")
auxilio = Recompensa(930, 210, 60, 55, Imagen.recompensa["auxilio"], "auxilio")
vida_1 = Recompensa(20, 10, 25, 25, Imagen.recompensa["vida"], "vida_1")
vida_2 = Recompensa(50, 10, 25, 25, Imagen.recompensa["vida"], "vida_2")
vida_3 = Recompensa(80, 10, 25, 25, Imagen.recompensa["vida"], "vida_3")
vida_4 = Recompensa(20, 10, 25, 25, Imagen.recompensa["vida"], "vida_4")
vida_5 = Recompensa(50, 10, 25, 25, Imagen.recompensa["vida"], "vida_5")
vida_6 = Recompensa(80, 10, 25, 25, Imagen.recompensa["vida"], "vida_6")
vida_7 = Recompensa(20, 10, 25, 25, Imagen.recompensa["vida"], "vida_7")
vida_8 = Recompensa(50, 10, 25, 25, Imagen.recompensa["vida"], "vida_8")
vida_9 = Recompensa(80, 10, 25, 25, Imagen.recompensa["vida"], "vida_9")
diamante = Recompensa(700, 40, 25, 25, Imagen.recompensa["diamante"], "diamante")
moneda = Recompensa(70, 290, 25, 25, Imagen.recompensa["moneda"], "moneda")
pizza = Recompensa(5, 300, 50, 45, Imagen.recompensa["pizza"], "pizza")
coca_cola = Recompensa(900, 300, 50, 60, Imagen.recompensa["coca_cola"], "coca_cola")
diamante_3 = Recompensa(450, 250, 20, 30, Imagen.recompensa["diamante_3"], "diamante_3")

recompensas_1 = [red_bull, bitcoin, auxilio, vida_1, vida_2, vida_3]
recompensas_2 = [diamante, moneda, vida_4, vida_5, vida_6]
recompensas_3 = [pizza, coca_cola, diamante_3, vida_7, vida_8, vida_9]

