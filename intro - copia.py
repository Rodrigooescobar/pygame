import pygame
import sys
import colores
from constantes import *

class Intro_game:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = pygame.image.load("imagenes/fondo.png")
        self.fondo = pygame.transform.scale(
           self.fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rect_fondo = self.fondo.get_rect()
        self.fondo2 = pygame.image.load("imagenes/play.jpg")
        self.fondo2 = pygame.transform.scale(
           self.fondo2, (200, 100))
        self.rect_fondo2 = self.fondo2.get_rect()
        self.rect_fondo2.centerx = ANCHO_VENTANA / 2
        self.rect_fondo2.centery = ALTO_VENTANA - 200
        self.intro_font = pygame.font.SysFont("Arial", 48)
        self.intro_title = self.intro_font.render(
            "Galaxy Game", True, colores.WHITE)
        self.intro_subtitle = self.intro_font.render(
            "Press SPACE or PLAY to play", True, colores.WHITE)
        self.clock = pygame.time.Clock()
        
       


    def run(self):
        
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return  # Salir del bucle y comenzar el juego
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:  # Clic izquierdo del mouse
                        if self.rect_fondo2.collidepoint(evento.pos):
                            return  # Salir del bucle y comenzar el juego
            

            self.pantalla.blit(self.fondo, self.rect_fondo)
            self.pantalla.blit(self.fondo2, self.rect_fondo2)
            self.pantalla.blit(
                self.intro_title, (ANCHO_VENTANA / 2 - self.intro_title.get_width() / 2, ALTO_VENTANA/2 - 100))
            self.pantalla.blit(self.intro_subtitle, (ANCHO_VENTANA /
                               2 - self.intro_subtitle.get_width() / 2, 350))
            pygame.display.flip()
