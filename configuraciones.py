import pygame
import pygame.mixer
pygame.mixer.init()
# sonido_disparo = pygame.mixer.Sound(r"recursos\sonidos\bumeran.wav")
# sonido_GUI = pygame.mixer.Sound(r"recursos\sonidos\GUI.wav")

pygame.font.init()

ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 600
TAMAÑO_PANTALLA = (ANCHO_PANTALLA, ALTO_PANTALLA)
ORIGEN_COORDENADAS = (0, 0)

PISO = 580

FPS = 40
pausado = False

sonido_disparo = pygame.mixer.Sound(r"recursos\sonidos\bumeran.wav")
sonido_GUI = pygame.mixer.Sound(r"recursos\sonidos\GUI.wav")
sonido_nivel = pygame.mixer.Sound(r"recursos\sonidos\sonido_nivel.wav")

class Colores:
    ROJO = (255, 0, 0)
    VERDE = (0, 255, 0)
    AZUL = (0, 0, 255)
    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    AZUL_CLARO = (255, 0, 0)
    MAGENTA = (255, 0, 255)
    AMARILLO = (255, 255, 0)

# Tiempo de juego
tiempo_restante = 90
tiempo_anterior = pygame.time.get_ticks()
fuente_tiempo = pygame.font.Font(None, 30)

# Score
fuente_puntaje = pygame.font.Font(None, 30)


