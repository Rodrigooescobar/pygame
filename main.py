import pygame
import sys
import colores
import random
from configuracion import *
#from config import guardar_datos_json
from intro import Intro_game
from player import *
from enemy import *
from colisiones import *
from game_over import GameOver


class Game:
    def __init__(self) -> None:
       pygame.init()
       self.pantalla = pygame.display.set_mode(RESOLUCION)
       self.fondo = pygame.image.load("imagenes/fondo.png")
       self.fondo = pygame.transform.scale(
           self.fondo, (ANCHO_VENTANA, ALTO_VENTANA))
       self.rect_fondo = self.fondo.get_rect()
       self.fps = FPS
       self.gameover = True
       self.score = 0
       self.temporizador = 0
       self.timer_shot_enemy = pygame.USEREVENT  
       self.event_temporizador = pygame.USEREVENT
       self.mostrar_intro()        
       #self.new_game()
    #    pygame.mixer.music.load("music/stranger.wav")
    #    pygame.mixer.music.play(-1)

    def mostrar_intro (self):
        intro_game = Intro_game(self.pantalla,3)
        # intro_game.run()
        self.nombre_jugador = intro_game.run()  # Se guarda el nombre ingresado
        # self.nombre_jugador = nombre_jugador
        #self.new_game()

    def eventos(self):
        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                self.gameover = False
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.player.shot_player()
            elif evento.type == self.event_temporizador:
                self.timer -= 1
                if self.timer == 0:
                    self.guardar_datos("./juego2/datos.json")
                    self.gameover = False
                    GameOver(self.pantalla, self).run()
                    #self.gameover = False
            if evento.type == self.timer_shot_enemy: 
                for enemy in self.lista_enemy:
                    if random.random() < 0.1:
                        enemy.shot_enemy()
                        #print("disparo enemigo")
            #print(self.nombre_jugador)    


    def new_game(self):
        self.mostrar_intro()
        pygame.time.set_timer(self.timer_shot_enemy, 600)
        pygame.time.set_timer(self.event_temporizador, 1000)
        self.timer = 15 
        self.score = 0
        self.lista_proyectil_player = []
        self.player = Player(self, 2000, 1, self.lista_proyectil_player)
        self.lista_proyectil_enemy = []
        self.lista_enemy = Enemy.crear_lista_ovnis(self, 2, 14, 80, 100, 100, 0.5 , 10, self.lista_proyectil_enemy)
        self.colisiones = Colisiones(self,self.player, self.lista_proyectil_player, self.lista_enemy, self.lista_proyectil_enemy, self.score)
        

    def draw(self):
        self.pantalla.blit(self.fondo, self.rect_fondo)
        self.pantalla.blit(self.puntos, (10, 10))
        self.pantalla.blit(self.temporizador, (ANCHO_VENTANA/2-60, 10))
        self.player.draw_player(self.pantalla)
        
        for enemy in self.lista_enemy:
            enemy.draw_enemy(self.pantalla)
            enemy.update_enemy()

        for proyectil_enemy in self.lista_proyectil_enemy:
            proyectil_enemy.draw_disparo_enemigo(self.pantalla)
            proyectil_enemy.update_disparo_enemigo(self.lista_proyectil_enemy) 
            #print(len(self.lista_proyectil_enemy))


    def update(self):
        self.player.update_player(5)
        
        

    def actualizar_pantalla(self):
        self.font = pygame.font.SysFont("Arial", 30)        
        self.puntos = self.font.render(
            "SCORE: {0}".format(self.score), True, colores.WHITE)        
        self.score = self.colisiones.verificar_colisiones(self.score)
        self.temporizador = self.font.render(
            "TIME: {0}".format(self.timer), True, colores.WHITE)
        
    def guardar_datos(self, archivo_json):
        nombre_jugador = self.nombre_jugador
        score = self.score
        tiempo = self.timer

        # Llamar a la función guardar_datos_json() desde constntes.py
        guardar_datos_json(nombre_jugador, score, tiempo, archivo_json)
        

    def run(self):
        self.clock = pygame.time.Clock()
        self.new_game()
        while self.gameover:
            self.clock.tick(FPS)
            self.eventos()
            self.update()
            self.actualizar_pantalla()
            self.draw()
            pygame.display.flip()
        pygame.quit()

juego = Game()
juego.run()
