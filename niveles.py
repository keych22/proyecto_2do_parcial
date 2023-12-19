from plataformas import *
from personaje import *
from animaciones import *
from misiles import *
from enemigos import *
from trampas import *
from recompensas import *
from objetos import *

class Nivel:
    def __init__(self, plataformas: list[Plataforma], jugador: Personaje, trampas: list[Trampa], recompensas: list[Recompensa], objetos: list[Objeto], enemigos: list[Enemigo]):
        self.plataformas = plataformas
        self.jugador = jugador
        self.trampas = trampas
        self.recompensas = recompensas
        self.objetos = objetos 
        self.enemigos = enemigos
        self.misiles_personaje = []
        self.misiles_enemigos = []

    def crear_misil_personaje(self, nuevo_misil):
        self.misiles_personaje.append(nuevo_misil)

    def crear_misil_enemigo(self, nuevo_misil):
        self.misiles_enemigos.append(nuevo_misil)

    def actualizar(self):

        jugador.actualizar()

        for trampa in self.trampas:
            trampa.actualizar() 

        for misil in self.misiles_personaje:
            misil.actualizar()

        for disparo_enemigo in self.misiles_enemigos:
            disparo_enemigo.actualizar()

        for objeto in self.objetos:
            objeto.actualizar(jugador)

        for recompensa in self.recompensas:
            recompensa.actualizar(jugador)

        for plataforma in self.plataformas:
            plataforma.actualizar(self.plataformas)

    def dibujar(self, pantalla):

        for plataforma in self.plataformas:
            plataforma.dibujar(pantalla)

        for trampa in self.trampas:
            trampa.dibujar(pantalla)

        for objeto in self.objetos:
            if objeto.esta:
                objeto.dibujar(pantalla)

        for recompensa in self.recompensas:
            recompensa.dibujar(pantalla)

        jugador.dibujar(pantalla)

        for enemigo in self.enemigos:
            enemigo.dibujar(pantalla)

        for misil in self.misiles_personaje:
            misil.dibujar(pantalla)

        for misil in self.misiles_enemigos:
            misil.dibujar(pantalla)

# Creacion de los niveles
nivel_1 = Nivel(plataformas_1, jugador, trampas_1, recompensas_1, objetos_1, enemigos_1)
nivel_2 = Nivel(plataformas_2, jugador, trampas_2, recompensas_2, objetos_2, enemigos_2)
nivel_3 = Nivel(plataformas_3, jugador, trampas_3, recompensas_3, objetos_3, enemigos_3)
        
        