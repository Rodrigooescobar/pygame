import pygame
import sys
import colores
from player import *
from enemy import *
from constantes import *
from colisiones import *
import random


pygame.init()
reloj = pygame.time.Clock()



#def Game():
pantalla = pygame.display.set_mode(RESOLUCION)
fondo = pygame.image.load("imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))
rect_fondo = fondo.get_rect()
gameover = True
score = 0
timer_shot_enemy = pygame.USEREVENT


pygame.time.set_timer(timer_shot_enemy, 600)
score = 0
lista_proyectil_player = []
player = Player(1500, score,
                lista_proyectil_player)
lista_proyectil_enemy = []
enemy = Enemy(0, 0, 0, 0, [], [])
lista_enemy = enemy.crear_lista_ovnis(1, 10, 80, 100, 100, 0, 10, lista_proyectil_enemy)
colisiones = Colisiones(player, lista_proyectil_player,
                        lista_enemy, lista_proyectil_enemy, score)

flag_correr = True
while flag_correr:
    milis = reloj.tick(60) #cada 8ms da una vuelta al whil
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                player.shot_player()
        if evento.type == timer_shot_enemy:
            for enemy in lista_enemy:
                if random.random() < 0.1:
                    enemy.shot_enemy()


    pantalla.blit(fondo, rect_fondo)
    #pantalla.blit(texto, (10, 10))
    player.draw_player(pantalla)
    player.update_player(5)

    for enemy in lista_enemy:
        enemy.draw_enemy(pantalla)

    font = pygame.font.SysFont("Arial", 30)
    texto = font.render(
        "SCORE: {0}".format(score), True, colores.WHITE)
    score = colisiones.verificar_colisiones(score)

    pygame.display.flip()
pygame.quit()
