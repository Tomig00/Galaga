from enum import Enum

# Class syntax
class Estados(Enum):
    # Estados
    ST_INIT = 0
    ST_MENU = 1
    ST_GAME = 2
    ST_GAMEOVER = 3
    ST_WIN = 4

class Forms(Enum):
    # Forms
    FM_MENU = 0
    FM_GAME = 1
    FM_GAMEOVER = 2
    FM_WIN = 3

# Variables globales
running = True
estado = Estados.ST_INIT
puntuacion = 0

def cambiar_puntuacion(nueva_puntuacion):
    global puntuacion
    puntuacion = nueva_puntuacion

def get_puntuacion():
    global puntuacion
    return puntuacion

def start_running():
    global running
    running = True

def stop_running():
    global running
    running = False

def get_running():
    global running
    return running

def cambiar_estado(nuevo_estado):
    global estado
    estado = nuevo_estado



SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720


