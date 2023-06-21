import pygame
import sys
import colores
from constantes import *
import json


class Intro_game:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.fondo = pygame.image.load("imagenes/fondo.png")
        self.fondo = pygame.transform.scale(
            self.fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rect_fondo = self.fondo.get_rect()
        self.intro_font = pygame.font.SysFont("Arial", 48)
        self.intro_title = self.intro_font.render(
            "Galaxy Game", True, colores.WHITE)
        self.intro_subtitle = self.intro_font.render(
            "Press SPACE to play", True, colores.WHITE)
        self.clock = pygame.time.Clock()

    def run(self):
        nombre = ""
        input_rect = pygame.Rect(
            ANCHO_VENTANA / 2 - 200, ALTO_VENTANA / 2, 400, 50)
        input_active = False

        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return  # Salir del bucle y comenzar el juego
                    elif evento.key == pygame.K_RETURN:
                        # Guardar el puntaje con el nombre ingresado
                        puntaje = 100  # Puntaje de ejemplo
                        self.guardar_puntaje(nombre, puntaje)
                    elif evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    else:
                        nombre += evento.unicode

            self.pantalla.blit(self.fondo, self.rect_fondo)
            pygame.draw.rect(self.pantalla, colores.WHITE, input_rect, 2)
            text_surface = self.intro_font.render(nombre, True, colores.WHITE)
            self.pantalla.blit(
                text_surface, (input_rect.x + 5, input_rect.y + 5))

            self.pantalla.blit(
                self.intro_title, (ANCHO_VENTANA / 2 - self.intro_title.get_width() / 2, 250))
            self.pantalla.blit(self.intro_subtitle, (ANCHO_VENTANA /
                               2 - self.intro_subtitle.get_width() / 2, 350))

            pygame.display.flip()

    # def guardar_puntaje(self, nombre, puntaje):
    #     puntaje_actual = {
    #         "nombre": nombre,
    #         "puntaje": puntaje
    #     }

    #     with open("puntajes.json", "a") as archivo:
    #         json.dump(puntaje_actual, archivo)
    #         archivo.write('\n')
