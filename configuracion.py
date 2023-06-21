import pygame
import json
import re

ANCHO_VENTANA = 1200
ALTO_VENTANA = 800
RESOLUCION = (ANCHO_VENTANA, ALTO_VENTANA)
FPS = 70
VELOCIDAD_BALA_ENEMIGO = 1
TIEMPO = 55


def guardar_datos_json(nombre_jugador, score, tiempo, archivo_json):
    try:
        with open(archivo_json, 'r') as file:
            datos = json.load(file)
    except FileNotFoundError:
        print("El archivo no existe y se creo un nuevo JSON.")
        datos = []
    except json.JSONDecodeError:
        print("El archivo JSON estaba vacío y se creo una nueva lista.")
        datos = []

    if not nombre_jugador:
        nombre_jugador = "No name"

    nuevo_dato = {
        "nombre": nombre_jugador,
        "score": score,
        "tiempo": tiempo
    }

    datos.append(nuevo_dato)

    with open(archivo_json, 'w') as file:
        json.dump(datos, file, separators=(",\n", ": "))









def parse_puntos (archivo:str) -> list:
    i = 0
    with open(archivo, "r") as archivo:
        lista_puntos = []
        todo = archivo.read ()
        nombre = re.findall (r'"nombre:" "([a-zA-Z0-9]+)'), todo
        tiempo = re.findall(r'"tiempo": ([0-9])', todo)
        puntos = re.findall(r'"puntos: " ([0-9]+)', todo)
        for i in range(len(nombre)):
            dic_puntajes = {}
            dic_puntajes["nombre"] = nombre [i]
            dic_puntajes["tiempo"] = tiempo [i]
            dic_puntajes["puntos"] = puntos [i]
            lista_puntos.append(dic_puntajes)
            i += 1
    return lista_puntos

# puntaje = parse_puntos("data_juego_json")