import pygame
from configuracion import *


class Enemy:
    def __init__(self, x, y, movimiento_y, max_disparos, lista_enemy, lista_proyectiles_enemy):
        self.image = pygame.image.load("imagenes/nave_enemiga5.png")
        self.image = pygame.transform.scale(self.image, (60, 55))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.inicial_x = x
        self.inicial_y = y
        self.movimiento_y = movimiento_y
        self.lista_proyectil_enemy = lista_proyectiles_enemy
        self.lista_enemy = lista_enemy
        self.max_disparos = max_disparos

    def reset_position(self):
        self.rect.x = self.inicial_x
        self.rect.y = self.inicial_y

    def update_enemy(self):
        self.rect.y += self.movimiento_y
        

        #for proyectil in self.lista_proyectil_enemy:
   

    def draw_enemy(self, pantalla):
        pantalla.blit(self.image, self.rect)
        
            

        # for enemy in self.lista_enemy:
        #     enemy.draw_enemy(pantalla)
        
    def shot_enemy(self):
        if len(self.lista_proyectil_enemy) < self.max_disparos:
            proyectil_enemy = Disparos_enemy(self.rect.centerx, self.rect.bottom, 1)
            self.lista_proyectil_enemy.append(proyectil_enemy)

    # def actualizar_disparos(self):
    #     for proyectil in self.lista_proyectil_enemy:
    #         proyectil.update_disparo_enemigo()

    #     # Eliminar los disparos que salen de la pantalla
    #     self.lista_proyectil_enemy = [
    #         disparo for disparo in self.lista_proyectil_enemy if disparo.rect.bottom >= 0]

    def crear_lista_ovnis(self, filas, columnas, distancia, x, y, movimiento_y, max_disparos, lista_proyectiles_enemy):
        self.lista_enemy = []
        num_filas = filas
        num_columnas = columnas
        distancia_entre_enemigos = distancia
        x_start = x
        y_start = y
        for fila in range(num_filas):
            for columna in range(num_columnas):
                x = x_start + columna * distancia_entre_enemigos
                y = y_start + fila * distancia_entre_enemigos
                nuevo_enemigo = Enemy(x, y, movimiento_y, max_disparos, self.lista_enemy, lista_proyectiles_enemy)
                self.lista_enemy.append(nuevo_enemigo)
        return self.lista_enemy

class Disparos_enemy:
    def __init__(self, x, y, movimiento_y):
        self.image = pygame.image.load("imagenes/misil_enemigo.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.movimiento_y = movimiento_y


    def update_disparo_enemigo(self, lista_balas_enemigas):
        self.rect.y += 5

        if self.rect.bottom > ALTO_VENTANA or self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            lista_balas_enemigas.remove(self)
            #print(len(lista_balas_enemigas))
            
    def draw_disparo_enemigo(self, pantalla):
        pantalla.blit(self.image, self.rect)