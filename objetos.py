import pygame
from configurar_imagenes import *
from animaciones import *
from personaje import *

class Objeto:
    agarre_llave = False
    def __init__(self, x: int, y: int, ancho: int, alto: int, ruta_imagen: pygame.Surface, nombre_objeto: str):
        self.imagen = reescalar_imagenes(ruta_imagen, ancho, alto)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.nombre = nombre_objeto
        self.esta = True

    def detectar_colision(self, jugador):
        if self.rect.colliderect(jugador):
            if self.nombre == "llave_oro":
                self.esta = False
                objetos_2.remove(self)
                Objeto.agarre_llave = True
            elif self.nombre == "baul_oro" and Objeto.agarre_llave:
                self.esta = False
                objetos_2.remove(self)
                boton_nivel_2.nivel_actual = "pase_nivel_3"
                jugador.armado = False
                Objeto.agarre_llave = False
                boton_nivel_3.nivel_actual = 3
            elif self.nombre == "llave_plata":
                self.esta = False
                objetos_1.remove(self)
                Objeto.agarre_llave = True
            elif self.nombre == "baul_plateado" and Objeto.agarre_llave:
                self.esta = False
                objetos_1.remove(self)
                boton_nivel_1.nivel_actual = "pase_nivel_2"
                jugador.armado = False
                Objeto.agarre_llave = False
                boton_nivel_2.nivel_actual = 2
            elif self.nombre == "bumeran":
                self.esta = False
                objetos_1.remove(self)
                jugador.armado = True
            elif self.nombre == "bumeran_2":
                self.esta = False
                objetos_2.remove(self)
                jugador.armado = True
            elif self.nombre == "bumeran_3":
                self.esta = False
                objetos_3.remove(self)
                jugador.armado = True

    def actualizar(self, jugador):
        self.detectar_colision(jugador)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)

llave_plata = Objeto(10, 270, 25, 20, Imagen.objeto["llave_plata"], "llave_plata")
llave_oro = Objeto(30, 100, 25, 20, Imagen.objeto["llave_oro"], "llave_oro")
baul_plateado = Objeto(925, 130, 70, 50, Imagen.objeto["baul_plateado"], "baul_plateado")
baul_oro = Objeto(925, 80, 70, 50, Imagen.objeto["baul_oro"], "baul_oro")
bumeran = Objeto(900, 400, 30, 30, Imagen.objeto["bumeran"], "bumeran")
bumeran_2 = Objeto(960, 300, 30, 30, Imagen.objeto["bumeran"], "bumeran_2")
bumeran_3 = Objeto(180, 200, 30, 30, Imagen.objeto["bumeran"], "bumeran_3")
calavera = Objeto(275, 250, 50, 30, Imagen.objeto["calavera"], "calavera")
calavera_3 = Objeto(800, 550, 50, 30, Imagen.objeto["calavera"], "calavera_3")
cruz = Objeto(540, 320, 30, 70, Imagen.objeto["cruz"], "cruz")
señal = Objeto(690, 410, 70, 70, Imagen.objeto["señal"], "señal")
arbol = Objeto(320, 100, 180, 180, Imagen.objeto["arbol"], "señal")
grama = Objeto(5, 390, 120, 60, Imagen.objeto["grama"], "señal")
urna = Objeto(135, 410, 40, 40, Imagen.objeto["urna"], "señal")
letrero = Objeto(10, 150, 60, 60, Imagen.objeto["letrero"], "señal")

objetos_1 = [llave_plata, baul_plateado, bumeran]
objetos_2 = [calavera, cruz, señal, arbol, urna, grama, letrero, llave_oro, baul_oro, bumeran_2]
objetos_3 = [calavera_3, bumeran_3]