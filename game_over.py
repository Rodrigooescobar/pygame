import pygame
import sys
from configuracion import *


class GameOver:
    def __init__(self, pantalla, game):
        self.game = game
        self.pantalla = pantalla
        self.fondo = pygame.image.load("imagenes/fondo_gameover.jpg")
        self.fondo = pygame.transform.scale(
            self.fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rect_fondo = self.fondo.get_rect()
        self.imagen_return = pygame.image.load("imagenes/return.png")
        self.imagen_return = pygame.transform.scale(self.imagen_return, (100, 50))
        self.rect_return = self.imagen_return.get_rect()
        self.rect_return.centerx = ANCHO_VENTANA / 2 - 60
        self.rect_return.centery = ALTO_VENTANA - 100
        self.imagen_salir = pygame.image.load("imagenes/salir.png")
        self.imagen_salir = pygame.transform.scale(self.imagen_salir, (100, 50))
        self.rect_salir = self.imagen_salir.get_rect()
        self.rect_salir.centerx = ANCHO_VENTANA / 2 + 60
        self.rect_salir.centery = ALTO_VENTANA - 100
        self.clock = pygame.time.Clock()
        self.run()
        


    def run(self):
        while True:
            self.clock.tick(FPS)
            self.game.gameover = True
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:  
                        if self.rect_salir.collidepoint(evento.pos):
                            pygame.quit()
                            sys.exit() 
                        elif self.rect_return.collidepoint(evento.pos):
                            self.game.run()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_BACKSPACE:
                        self.game.run()

            # blit del fondo
            self.pantalla.blit(self.fondo, self.rect_fondo)
            # blit del boton salir
            self.pantalla.blit(self.imagen_salir, self.rect_salir)
            # blit del boton return
            self.pantalla.blit(self.imagen_return, self.rect_return)
            # blite del ranking
            #self.mostrar_ranking()
            pygame.display.flip()
