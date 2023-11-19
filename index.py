import pygame
from common import defs
from src.menuForm import MenuForm
from src.gameForm import GameForm
from src.gameOverForm import GameOverForm
from src.winForm import WinForm




screen = pygame.display.set_mode((defs.SCREEN_WIDTH, defs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
forms = []

def main():
    # pygame setup
    pygame.init()

    global forms
    forms = [MenuForm(screen, clock), GameForm(screen, clock), GameOverForm(screen, clock), WinForm(screen, clock)]

    run()


def run():
    
    while defs.get_running():
        
        if defs.estado == defs.Estados.ST_INIT:
            defs.cambiar_estado(defs.Estados.ST_MENU)
        elif defs.estado == defs.Estados.ST_MENU:
            forms[defs.Forms.FM_MENU.value].tick()
        elif defs.estado == defs.Estados.ST_GAME:
            forms[defs.Forms.FM_GAME.value].tick()
        elif defs.estado == defs.Estados.ST_GAMEOVER:
            forms[defs.Forms.FM_GAMEOVER.value].tick()
        elif defs.estado == defs.Estados.ST_WIN:
            forms[defs.Forms.FM_WIN.value].tick()

        pygame.display.flip()

        clock.tick(60) 

    pygame.quit()




main()