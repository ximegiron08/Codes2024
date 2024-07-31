import pygame
import sys
import random
pygame.init()
WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("El anillo perdido")
font = pygame.font.SysFont(None, 24)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
def cargar(nombre):
    img = pygame.image.load(nombre)
    img = pygame.transform.scale(img,(WIDTH,HEIGHT))
    screen.blit(img, (0,0))
    pygame.display.update()
    #CARGA DE IMAGENES
img_anillo = pygame.image.load('historiagrafica1.png')
img_anillo = pygame.transform.scale(img_anillo,(WIDTH,HEIGHT))
screen.blit(img_anillo, (0,0))
texto = font.render('El anillo perdido', True, WHITE)
screen.blit(texto, (20, 20))
texto = font.render('By: Ximena Giron', True, WHITE)
screen.blit(texto, (50, 50))
pygame.display.update()
pantalla = 1
    # Definir las transiciones para cada tecla
transiciones = {
    pygame.K_RIGHT: {
        6: 9,
        10: 12,
        11: 13,
    },
    pygame.K_1: {
        4: 5,
        9: 10,
        15: 16,
        17: 19,
        19: 22,
    },
    pygame.K_2: {
        4: 7,
        9: 11,
        15: 17,
        17: 18,
        19: 21,
    }
}
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in transiciones:
                # Obtener la transición para la tecla presionada
                pantalla = transiciones[event.key].get(pantalla, pantalla + 1)
                print(pantalla)
    if pantalla== 2:
        cargar('contextoinicial.png')
    elif pantalla == 3:
        cargar('_historiagrafica2.png')    
    elif pantalla == 4:
        cargar('decision1.1.png')    
    elif pantalla == 5:
        cargar('_historiagrafica3.png')    
    elif pantalla == 6:
        cargar('contextodecision1.png')    
    elif pantalla == 7:
        cargar('jardin.png')     
    elif pantalla == 8:
        cargar('contextodecision2.png')
    elif pantalla == 9:
        cargar('decision2.png')
    elif pantalla == 10:
        cargar('enmayordomo.png')
    elif pantalla == 11:
        cargar('enjardinero.png')
    elif pantalla == 12:
        cargar('final1.png')
    elif pantalla == 13:
        cargar('contextoenjardinero.png')
    elif pantalla == 14:
        cargar('bodega.png')   
    elif pantalla == 15:
        cargar('decision3.png')   
    elif pantalla == 16:
        cargar('final2.png')
    elif pantalla == 17:
        cargar('decision44.png')
    elif pantalla == 18:
        cargar('camino5.png')
    elif pantalla == 19:
        cargar('decision5.png')   
    elif pantalla == 20:
        cargar('cocina.png')
    elif pantalla == 21:
        cargar('final33.png')
    elif pantalla == 22:
        cargar('final4.png')