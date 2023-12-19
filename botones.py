import pygame
from configurar_imagenes import *
from animaciones import *
from configuraciones import Colores

class Boton:
    def __init__(self, x: int, y: int, ancho: int, alto: int, ruta_imagen: pygame.Surface, color_texto: tuple = None, texto: str = None):
        self.imagen = reescalar_imagenes(ruta_imagen, ancho, alto)
        self.rect = self.imagen.get_rect(topleft = (x, y))
        self.texto = texto
        self.color_texto = color_texto
        self.nivel_actual = None

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
        fuente = pygame.font.Font(None, 24)
        texto = fuente.render(self.texto, True, self.color_texto)
        texto_rect = texto.get_rect(center = self.rect.center)
        pantalla.blit(texto, texto_rect)

boton_nivel_1 = Boton(250, 480, 150, 70, Imagen.boton, Colores.BLANCO, "Nivel 1")
boton_nivel_2 = Boton(420, 480, 150, 70, Imagen.boton, Colores.BLANCO, "Nivel 2")
boton_nivel_3 = Boton(590, 480, 150, 70, Imagen.boton, Colores.BLANCO, "Nivel 3")

boton_sonido_on = Boton(700, 80, 50, 50, Imagen.sonido["on"], Colores.BLANCO, "")
boton_sonido_off = Boton(780, 80, 50, 50, Imagen.sonido["off"], Colores.BLANCO, "")
boton_pausa = Boton(350, 220, 350, 100, Imagen.boton_pausa, Colores.BLANCO, "")
boton_game_over = Boton(250, 180, 520, 250, Imagen.boton_game_over, Colores.BLANCO, "")
boton_jugar = Boton(395, 380, 210, 40, Imagen.boton_jugar, Colores.BLANCO, "")

botones = [boton_nivel_1, boton_nivel_2, boton_nivel_3, boton_sonido_on, boton_sonido_off]