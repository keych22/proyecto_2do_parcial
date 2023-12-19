import pygame
from configuraciones import *


class Imagen:

    personaje_quieto_derecha = [
        pygame.image.load(r"recursos\imagenes\quieto\0.png"),
        pygame.image.load(r"recursos\imagenes\quieto\1.png")
    ]

    personaje_corre_derecha = [
        pygame.image.load(r"recursos\imagenes\corre\4.png"),
        pygame.image.load(r"recursos\imagenes\corre\5.png"),
        pygame.image.load(r"recursos\imagenes\corre\6.png"),
        pygame.image.load(r"recursos\imagenes\corre\7.png"),
        pygame.image.load(r"recursos\imagenes\corre\8.png"),
        pygame.image.load(r"recursos\imagenes\corre\9.png"),
        pygame.image.load(r"recursos\imagenes\corre\10.png"),
    ]

    personaje_salta_derecha = [
        pygame.image.load(r"recursos\imagenes\salta\11.png"),
        pygame.image.load(r"recursos\imagenes\salta\12.png"),
        pygame.image.load(r"recursos\imagenes\salta\13.png"),
        pygame.image.load(r"recursos\imagenes\salta\14.png"),
        pygame.image.load(r"recursos\imagenes\salta\15.png"),
        pygame.image.load(r"recursos\imagenes\salta\16.png"),
    ]

    personaje_muere_derecha = [
        pygame.image.load(r"recursos\imagenes\muriendo\0.png"),
        pygame.image.load(r"recursos\imagenes\muriendo\1.png"),
        pygame.image.load(r"recursos\imagenes\muriendo\2.png"),
        pygame.image.load(r"recursos\imagenes\muriendo\3.png"),
        pygame.image.load(r"recursos\imagenes\muriendo\4.png")
    ]

    personaje_toma_derecha = [
        pygame.image.load(r"recursos\imagenes\toma\0.png"),
        pygame.image.load(r"recursos\imagenes\toma\1.png"),
        pygame.image.load(r"recursos\imagenes\toma\2.png"),
        pygame.image.load(r"recursos\imagenes\toma\3.png"),
        pygame.image.load(r"recursos\imagenes\toma\4.png"),
        pygame.image.load(r"recursos\imagenes\toma\5.png")
    ]

    fondo = {"nivel_1": pygame.transform.scale(pygame.image.load(
        r"recursos\imagenes\fondos\nivel_1.png"), TAMAÑO_PANTALLA),
        "nivel_2": pygame.transform.scale(pygame.image.load(
            r"recursos\imagenes\fondos\nivel_2.png"), TAMAÑO_PANTALLA),
        "nivel_3": pygame.transform.scale(pygame.image.load(
            r"recursos\imagenes\fondos\nivel_3.png"), TAMAÑO_PANTALLA)
    }

    plataforma = {
        "caja": pygame.image.load(r"recursos\imagenes\plataformas\1.png"),
        "viga": pygame.image.load(r"recursos\imagenes\plataformas\2.png"),
        "pulla": pygame.image.load(r"recursos\imagenes\plataformas\pulla.png"),
        "madera_metal": pygame.image.load(r"recursos\imagenes\plataformas\madera_metal.png"),
        "bloques": pygame.image.load(r"recursos\imagenes\plataformas\bloques.png"),
        "barril": pygame.image.load(r"recursos\imagenes\plataformas\barril.png"),
        "bloque_marron": pygame.image.load(r"recursos\imagenes\plataformas\bloque_marron.png"),
        "caja_2": pygame.image.load(r"recursos\imagenes\plataformas\caja_2.png"),
        "monticulo_1": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_1.png"),
        "monticulo_2": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_2.png"),
        "monticulo_3": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_3.png"),
        "monticulo_4": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_4.png"),
        "monticulo_5": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_5.png"),
        "monticulo_6": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_6.png"),
        "monticulo_7": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_7.png"),
        "monticulo_8": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_8.png"),
        "monticulo_9": pygame.image.load(r"recursos\imagenes\plataformas\monticulo_9.png")
    }

    trampa = {
        "cuchillas": pygame.image.load(r"recursos\imagenes\trampas\cuchillas.png"),
        "cuchillas_3": pygame.image.load(r"recursos\imagenes\trampas\cuchillas_3.png"),
        "sustancia": pygame.image.load(r"recursos\imagenes\trampas\sustancia.png"),
        "lanzas": pygame.image.load(r"recursos\imagenes\trampas\lanzas.png")
    }

    bumeran = [
        pygame.image.load(r"recursos\imagenes\bumeran\0.png"),
        pygame.image.load(r"recursos\imagenes\bumeran\1.png")
    ]

    proyectil = [
        pygame.image.load(r"recursos\imagenes\balas\0.png")
    ]

    villano = [
        pygame.image.load(r"recursos\imagenes\enemigos\1.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\2.png")
    ]

    monstruo = pygame.image.load(r"recursos\imagenes\enemigos\monstruo.png")

    perro = [
        pygame.image.load(r"recursos\imagenes\perro\1.png"),
        pygame.image.load(r"recursos\imagenes\perro\2.png"),
        pygame.image.load(r"recursos\imagenes\perro\3.png"),
        pygame.image.load(r"recursos\imagenes\perro\4.png"),
        pygame.image.load(r"recursos\imagenes\perro\5.png"),
        pygame.image.load(r"recursos\imagenes\perro\6.png"),
        pygame.image.load(r"recursos\imagenes\perro\7.png"),
        pygame.image.load(r"recursos\imagenes\perro\8.png")
    ]

    cuervo = [
        pygame.image.load(r"recursos\imagenes\enemigos\cuervo\0.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\cuervo\1.png")
    ]

    mino_tauro_caminando = [
        pygame.image.load(r"recursos\imagenes\enemigos\mino_tauro\0.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\mino_tauro\1.png")
    ]

    mino_tauro_atacando = [
        pygame.image.load(r"recursos\imagenes\enemigos\mino_tauro\2.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\mino_tauro\3.png")
    ]

    zombie_hombre_caminando = [
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\0.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\1.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\2.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\3.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\4.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\5.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\6.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\7.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\8.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\9.png"),
    ]

    zombie_hombre_atacando = [
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\10.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\11.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\12.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\13.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\14.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\15.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\16.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\17.png")
    ]

    zombie_mujer_atacando = [
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\18.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\19.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\20.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\21.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\22.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\23.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\24.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\25.png")
    ]

    zombie_mujer_caminando = [
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\26.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\27.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\28.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\29.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\30.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\31.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\32.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\33.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\34.png"),
        pygame.image.load(r"recursos\imagenes\enemigos\zombie\35.png")
    ]

    objeto = {"llave_plata": pygame.image.load(r"recursos\imagenes\objetos\llave_plata.png"),
        "llave_oro": pygame.image.load(r"recursos\imagenes\objetos\llave_oro.png"),
        "baul_oro": pygame.image.load(r"recursos\imagenes\objetos\baul_oro.png"),
        "baul_plateado": pygame.image.load(r"recursos\imagenes\objetos\baul_plateado.png"),
        "bumeran": pygame.image.load(r"recursos\imagenes\objetos\bumeran.png"),
        "calavera": pygame.image.load(r"recursos\imagenes\objetos\calavera.png"),
        "cruz": pygame.image.load(r"recursos\imagenes\objetos\cruz.png"),
        "señal": pygame.image.load(r"recursos\imagenes\objetos\señal.png"),
        "arbol": pygame.image.load(r"recursos\imagenes\objetos\arbol.png"),
        "grama": pygame.image.load(r"recursos\imagenes\objetos\grama.png"),
        "urna": pygame.image.load(r"recursos\imagenes\objetos\urna.png"),
        "palos": pygame.image.load(r"recursos\imagenes\objetos\palos.png"),
        "letrero": pygame.image.load(r"recursos\imagenes\objetos\letrero.png")
    }

    recompensa = {"red_bull": pygame.image.load(r"recursos\imagenes\recompensas\red_bull.png"),
        "bitcoin": pygame.image.load(r"recursos\imagenes\recompensas\bitcoin.png"),
        "auxilio": pygame.image.load(r"recursos\imagenes\recompensas\auxilio.png"),
        "vida": pygame.image.load(r"recursos\imagenes\recompensas\vida.png"),
        "moneda": pygame.image.load(r"recursos\imagenes\recompensas\moneda.png"),
        "diamante": pygame.image.load(r"recursos\imagenes\recompensas\diamante.png"),
        "pizza": pygame.image.load(r"recursos\imagenes\recompensas\pizza.png"),
        "coca_cola": pygame.image.load(r"recursos\imagenes\recompensas\coca_cola.png"),
        "diamante_3": pygame.image.load(r"recursos\imagenes\recompensas\diamante_3.png")
    }

    boton = pygame.image.load(r"recursos\imagenes\objetos\boton.png")
    boton_pausa = pygame.image.load(
        r"recursos\imagenes\objetos\boton_pausa.png")
    boton_game_over = pygame.image.load(
        r"recursos\imagenes\objetos\game_over.png")
    boton_jugar = pygame.image.load(r"recursos\imagenes\objetos\jugar.png")

    sonido = {
        "on": pygame.image.load(r"recursos\imagenes\objetos\sonido_on.png"),
        "off": pygame.image.load(r"recursos\imagenes\objetos\sonido_off.png")
    }

fondo_nivel_1 = Imagen.fondo["nivel_1"]
fondo_nivel_2 = Imagen.fondo["nivel_2"]
fondo_nivel_3 = Imagen.fondo["nivel_3"]
