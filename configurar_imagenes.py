import pygame

# TODO Documentar ambas funciones
def girar_imagenes(imagenes: list[pygame.Surface]) -> list:

    imagenes_invertidas = []

    invierte_x = True
    invierte_y = False
    for imagen in imagenes:
        imagenes_invertidas.append(pygame.transform.flip(imagen, invierte_x, invierte_y))

    return imagenes_invertidas

def reescalar_imagenes(imagenes: list[pygame.Surface] | pygame.Surface, ancho: int, alto: int) -> list | pygame.Surface :
    if isinstance(imagenes, list):
        return [pygame.transform.scale(img, (ancho, alto)) for img in imagenes]
    elif isinstance(imagenes, pygame.Surface):
        return pygame.transform.scale(imagenes, (ancho, alto))



    
