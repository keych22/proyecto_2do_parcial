import pygame, sys, sqlite3
from configuraciones import *
from pygame.locals import *
from misiles import *
from monstruos import *
from niveles import *
from enemigos import *
from animaciones import *
from interfaz_usuario import *
from gestor_archivos import *

# Inicializo pygame
pygame.init()

# Conexion a base de datos
conexion = sqlite3.connect("puntaje_jugador.db")
conexion.execute("CREATE TABLE IF NOT EXISTS puntajes (id INTEGER PRIMARY KEY AUTOINCREMENT, puntaje INTEGER)")

# Inicializo el reloj
reloj = pygame.time.Clock()

PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
pygame.display.set_caption("Juego 2do parcial")

mostrar_GUI(PANTALLA, caja_texto)

# Bucle principal del juego
juego_ejecutandose = True
while juego_ejecutandose:
    reloj.tick(FPS)

    # Detectar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_ejecutandose = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_jugar.rect.collidepoint(evento.pos):
                # Reiniciar juego
                jugador.vidas = 3
                jugador.puntaje = 0
                tiempo_restante = 90
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not jugador.murio:
                jugador.saltar()
            elif evento.key == pygame.K_d and jugador.armado:
                # sonido_disparo.play()
                # Posicion desde donde saldra el misil disparado
                if boton_nivel_1.nivel_actual == 1:
                    nuevo_misil_personaje = Misil(25, 25, 5, jugador.direccion, plataformas_1, nivel_1, enemigos_1)
                    nivel_1.crear_misil_personaje(nuevo_misil_personaje)
                elif boton_nivel_2.nivel_actual == 2:
                    nuevo_misil_personaje = Misil(25, 25, 5, jugador.direccion, plataformas_2, nivel_2, enemigos_2)
                    nivel_2.crear_misil_personaje(nuevo_misil_personaje)
                elif boton_nivel_3.nivel_actual == 3:
                    nuevo_misil_personaje = Misil(25, 25, 5, jugador.direccion, plataformas_3, nivel_3, enemigos_3)
                    nivel_3.crear_misil_personaje(nuevo_misil_personaje)
            elif evento.key == pygame.K_p:
                pausado = not pausado

    if jugador.vidas <= 0 or tiempo_restante <= 0:
        boton_game_over.dibujar(PANTALLA)
        boton_jugar.dibujar(PANTALLA)
        
    elif not pausado:
        
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_anterior >= 1000:
            tiempo_restante -= 1
            tiempo_anterior = tiempo_actual

        mensaje_tiempo = fuente_tiempo.render(f'Tiempo: {tiempo_restante}', True, Colores.BLANCO)
        rect_tiempo = mensaje_tiempo.get_rect(topleft = (450, 10))

        mensaje_puntaje = fuente_puntaje.render(f'Puntaje: {jugador.puntaje}', True, Colores.BLANCO)
        rect_puntaje = mensaje_puntaje.get_rect(topleft = (850, 10))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and not jugador.murio and not jugador.tomo_bebida:
            jugador.mover_derecha()
        elif keys[pygame.K_LEFT] and not jugador.murio and not jugador.tomo_bebida:
            jugador.mover_izquierda()
        else:
            if not jugador.murio and not jugador.tomo_bebida:
                jugador.quieto()

        # Procesa el Nivel 1
        if boton_nivel_1.nivel_actual == 1:

            for enemigo in enemigos_1:
                proyectil = enemigo.actualizar()
                if proyectil:
                    nivel_1.crear_misil_enemigo(proyectil)

            for misil in nivel_1.misiles_enemigos:
                if misil.colisionar_jugador(jugador):           
                    jugador.perder_vida()
                    nivel_1.misiles_enemigos.remove(misil)

            nivel_1.misiles_personaje = [misil for misil in nivel_1.misiles_personaje if 0 < misil.rect.x < ANCHO_PANTALLA]
            nivel_1.misiles_enemigos = [misil for misil in nivel_1.misiles_enemigos if 0 < misil.rect.x < ANCHO_PANTALLA]

            nivel_1.actualizar()

            PANTALLA.blit(fondo_nivel_1, ORIGEN_COORDENADAS)
            PANTALLA.blit(mensaje_tiempo, rect_tiempo)
            PANTALLA.blit(mensaje_puntaje, rect_puntaje)
            # sonido_nivel.play()

            nivel_1.dibujar(PANTALLA)

        # Procesa el Nivel 2
        elif boton_nivel_2.nivel_actual == 2:

            for enemigo in enemigos_2:
                proyectil = enemigo.actualizar()
                if proyectil:
                    nivel_2.crear_misil_enemigo(proyectil)

            for misil in nivel_2.misiles_enemigos:
                if misil.colisionar_jugador(jugador):           
                    jugador.perder_vida()
                    nivel_2.misiles_enemigos.remove(misil)

            nivel_2.misiles_personaje = [misil for misil in nivel_2.misiles_personaje if 0 < misil.rect.x < ANCHO_PANTALLA]           
            nivel_2.misiles_enemigos = [misil for misil in nivel_2.misiles_enemigos if 0 < misil.rect.x < ANCHO_PANTALLA]
            
            nivel_2.actualizar()
            PANTALLA.blit(fondo_nivel_2, ORIGEN_COORDENADAS)
            PANTALLA.blit(mensaje_tiempo, rect_tiempo)
            PANTALLA.blit(mensaje_puntaje, rect_puntaje)

            nivel_2.dibujar(PANTALLA)

        # # Procesa el Nivel 3
        elif boton_nivel_3.nivel_actual == 3:

            monstruo.actualizar()

            for enemigo in enemigos_3:
                proyectil = enemigo.actualizar()
                if proyectil:
                    nivel_3.crear_misil_enemigo(proyectil)

            for misil in nivel_3.misiles_enemigos:
                if misil.colisionar_jugador(jugador):           
                    jugador.perder_vida()
                    nivel_3.misiles_enemigos.remove(misil)

            for disparo in monstruo.lista_disparos:
                disparo.actualizar()

            monstruo.lista_disparos =  [disparo for disparo in monstruo.lista_disparos if 0 < disparo.rect.x < ANCHO_PANTALLA]

            nivel_3.actualizar()

            PANTALLA.blit(fondo_nivel_3, ORIGEN_COORDENADAS)
            PANTALLA.blit(mensaje_tiempo, rect_tiempo)
            PANTALLA.blit(mensaje_puntaje, rect_puntaje)

            for disparo in monstruo.lista_disparos:
                disparo.dibujar(PANTALLA)

            nivel_3.dibujar(PANTALLA)
            monstruo.dibujar(PANTALLA)

    elif pausado:
        boton_pausa.dibujar(PANTALLA)

    pygame.display.flip()

conexion.execute("INSERT INTO puntajes (puntaje) VALUES (?)", (jugador.puntaje,))
conexion.commit()

almacenar_datos(caja_texto.texto, jugador.puntaje, tiempo_restante)
conexion.close()
pygame.quit()
sys.exit()