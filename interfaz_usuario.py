import pygame, sys
from botones import *
from configuraciones import *
from inputs import *
from personaje import *
from gestor_archivos import *

def mostrar_GUI(pantalla, caja_texto):
    while True:
        # sonido_GUI.play()
        evento = pygame.event.wait()
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if caja_texto.rect.collidepoint(evento.pos):
                caja_texto.active = True
            elif boton_nivel_1.rect.collidepoint(evento.pos):
                boton_nivel_1.nivel_actual = 1
                break
            elif boton_nivel_2.rect.collidepoint(evento.pos):
                boton_nivel_2.nivel_actual = 2
                break
            elif boton_nivel_3.rect.collidepoint(evento.pos):
                boton_nivel_3.nivel_actual = 3
                break
            elif boton_sonido_on.rect.collidepoint(evento.pos):
                print("Sonido activar")
            elif boton_sonido_off.rect.collidepoint(evento.pos):
                print("Sonido desactivar")
            else:
                caja_texto.active = False
        elif evento.type == pygame.KEYDOWN and caja_texto.active:
            if evento.key == pygame.K_RETURN:
                almacenar_datos(caja_texto.texto, jugador.puntaje, tiempo_restante)
                caja_texto.texto = ""
                boton_nivel_1.nivel_actual = 1
                break
            elif evento.key == pygame.K_BACKSPACE:
                caja_texto.texto = caja_texto.texto[:-1]
            else:
                caja_texto.texto += evento.unicode

        imagen_fondo = pygame.image.load(r"recursos\imagenes\fondos\invasion_zombie.png")
        imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
        pantalla.blit(imagen_fondo, (0, 0))

        imagen_zombie = pygame.image.load(r"recursos\imagenes\fondos\zombie.png")
        imagen_fondo = pygame.transform.scale(imagen_zombie, (200, 300))
        pantalla.blit(imagen_fondo, (400, 50))

        fuente = pygame.font.Font(None, 30)
        texto = fuente.render("Nombre jugador", True, Colores.BLANCO)
        texto_rect = texto.get_rect(center = (190, 60))
        pantalla.blit(texto, texto_rect)

        # Dibuja los botones y la casilla de texto
        for boton in botones:
            boton.dibujar(pantalla)

        caja_texto.dibujar(pantalla)
        pygame.display.flip()