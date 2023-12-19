import pygame
from configuraciones import *

class CajaTexto:
    def __init__(self, x, y, ancho, alto):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color = Colores.BLANCO
        self.texto = ""
        self.active = False

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, self.rect)
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render(self.texto, True, Colores.ROJO)
        ancho = max(200, texto.get_width()+10)
        self.rect.w = ancho
        pantalla.blit(texto, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(pantalla, Colores.VERDE, self.rect, 2)

caja_texto = CajaTexto(100, 80, 200, 50)