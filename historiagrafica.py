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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(pantalla)
                if pantalla == 6:
                    pantalla = 9
                elif pantalla == 10:
                    pantalla = 12
                elif pantalla == 11:
                    pantalla = 13
                else:    
                    pantalla=pantalla+1

            if event.key == pygame.K_1:
                if pantalla == 4:
                    pantalla = 5
                elif pantalla == 9:
                    pantalla = 10
                elif pantalla == 15:
                    pantalla = 16
                elif pantalla == 17:
                    pantalla = 19
                elif pantalla == 19:
                    pantalla = 22


            if event.key == pygame.K_2:
                if pantalla == 4:
                    pantalla = 7
                elif pantalla == 9:
                    pantalla = 11
                elif pantalla == 15:
                    pantalla = 17
                elif pantalla == 17:
                    pantalla = 18
                elif pantalla == 19:
                    pantalla = 21

    if pantalla ==2:
        img_contextoinicial = pygame.image.load('contextoinicial.png')
        img_contextoinicial = pygame.transform.scale(img_contextoinicial,(WIDTH,HEIGHT))
        screen.blit(img_contextoinicial, (0,0))      
        pygame.display.update()

    elif pantalla == 3:
        img_psospechosos = pygame.image.load('_historiagrafica2.png')
        img_psospechosos = pygame.transform.scale(img_psospechosos,(WIDTH,HEIGHT))
        screen.blit(img_psospechosos, (0,0))
        pygame.display.update()

    elif pantalla == 4:
        img_decision1 = pygame.image.load('decision1.1.png')
        img_decision1 = pygame.transform.scale(img_decision1,(WIDTH,HEIGHT))
        screen.blit(img_decision1, (0,0))
        pygame.display.update()  

    elif pantalla == 5:
        img_habitacion = pygame.image.load('_historiagrafica3.png')
        img_habitacion = pygame.transform.scale(img_habitacion,(WIDTH,HEIGHT))
        screen.blit(img_habitacion, (0,0))
        pygame.display.update()

    elif pantalla == 6:
        img_contextod1 = pygame.image.load('contextodecision1.png')
        img_contextod1 = pygame.transform.scale(img_contextod1,(WIDTH,HEIGHT))
        screen.blit(img_contextod1, (0,0))
        pygame.display.update()

    elif pantalla == 7:
        img_jardin = pygame.image.load('jardin.png')
        img_habitacion = pygame.transform.scale(img_jardin,(WIDTH,HEIGHT))
        screen.blit(img_jardin, (0,0))
        pygame.display.update()

    elif pantalla == 8:
        img_contextod2 = pygame.image.load('contextodecision2.png')
        img_contextod2 = pygame.transform.scale(img_contextod2,(WIDTH,HEIGHT))
        screen.blit(img_contextod2, (0,0))
        pygame.display.update()

    elif pantalla == 9:
        img_decision2 = pygame.image.load('decision2.png')
        img_decision2 = pygame.transform.scale(img_decision2,(WIDTH,HEIGHT))
        screen.blit(img_decision2, (0,0))
        pygame.display.update()

    elif pantalla == 10:
        img_enmayordomo = pygame.image.load('enmayordomo.png')
        img_enmayordomo = pygame.transform.scale(img_enmayordomo,(WIDTH,HEIGHT))
        screen.blit(img_enmayordomo, (0,0))
        pygame.display.update()

    elif pantalla == 11:
        img_enjardinero = pygame.image.load('enjardinero.png')
        img_enjardinero = pygame.transform.scale(img_enjardinero,(WIDTH,HEIGHT))
        screen.blit(img_enjardinero, (0,0))
        pygame.display.update()

    elif pantalla == 12:
        img_final1 = pygame.image.load('final1.png')
        img_final1 = pygame.transform.scale(img_final1,(WIDTH,HEIGHT))
        screen.blit(img_final1, (0,0))
        pygame.display.update()

    elif pantalla == 13:
        img_contextojardinero = pygame.image.load('contextoenjardinero.png')
        img_contextojardinero = pygame.transform.scale(img_contextojardinero,(WIDTH,HEIGHT))
        screen.blit(img_contextojardinero, (0,0))
        pygame.display.update()

    elif pantalla == 14:
        img_bodega = pygame.image.load('bodega.png')
        img_bodega = pygame.transform.scale(img_bodega,(WIDTH,HEIGHT))
        screen.blit(img_bodega, (0,0))
        pygame.display.update()

    elif pantalla == 15:
        img_decision3 = pygame.image.load('decision3.png')
        img_decision3 = pygame.transform.scale(img_decision3,(WIDTH,HEIGHT))
        screen.blit(img_decision3, (0,0))
        pygame.display.update()

    elif pantalla == 16:
        img_final2 = pygame.image.load('final2.png')
        img_final2 = pygame.transform.scale(img_final2,(WIDTH,HEIGHT))
        screen.blit(img_final2, (0,0))
        pygame.display.update()

    elif pantalla == 17:
        img_decision4 = pygame.image.load('decision44.png')
        img_decision4 = pygame.transform.scale(img_decision4,(WIDTH,HEIGHT))
        screen.blit(img_decision4, (0,0))
        pygame.display.update()

    elif pantalla == 18:
        img_esposa = pygame.image.load('camino5.png')
        img_esposa = pygame.transform.scale(img_esposa,(WIDTH,HEIGHT))
        screen.blit(img_esposa, (0,0))
        pygame.display.update()

    elif pantalla == 19:
        img_decision5 = pygame.image.load('decision5.png')
        img_decision5 = pygame.transform.scale(img_decision5,(WIDTH,HEIGHT))
        screen.blit(img_decision5, (0,0))
        pygame.display.update()

    elif pantalla == 20:
        img_cocina = pygame.image.load('cocina.png')
        img_cocina = pygame.transform.scale(img_cocina,(WIDTH,HEIGHT))
        screen.blit(img_cocina, (0,0))
        pygame.display.update()

    elif pantalla == 21:
        img_final3 = pygame.image.load('final33.png')
        img_final3 = pygame.transform.scale(img_final3,(WIDTH,HEIGHT))
        screen.blit(img_final3, (0,0))
        pygame.display.update()

    elif pantalla == 22:
        img_final4 = pygame.image.load('final4.png')
        img_final4 = pygame.transform.scale(img_final4,(WIDTH,HEIGHT))
        screen.blit(img_final4, (0,0))
        pygame.display.update()