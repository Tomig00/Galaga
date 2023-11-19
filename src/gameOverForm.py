import pygame
from common import defs
class GameOverForm:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.estado = 0
        self.TitleFont = pygame.font.Font("./fonts/Emulogic.ttf", 72)
        self.TitleText = self.TitleFont.render("GAME OVER", True, "RED")
        self.TextFont = pygame.font.Font("./fonts/Emulogic.ttf", 36)
        self.Text = self.TextFont.render("Presione ESC para volver al menu", True, "white")
        self.PuntajeFont = pygame.font.Font("./fonts/Emulogic.ttf", 36)
    
    def __del__(self):
        del self.TitleFont
        del self.TextFont
        del self.PuntajeFont

    def update_puntaje_text(self):
        # Actualizar y renderizar el puntaje aquí
        self.PuntajeText = self.PuntajeFont.render("Puntaje: " + str(defs.get_puntuacion()), True, "white")

    
    def dibujar(self):
        self.screen.fill("black")
        self.screen.blit(self.TitleText, (defs.SCREEN_WIDTH/2 - self.TitleText.get_width()/2, defs.SCREEN_HEIGHT/2 - self.TitleText.get_height()/2))
        self.screen.blit(self.Text, (defs.SCREEN_WIDTH/2 - self.Text.get_width()/2, defs.SCREEN_HEIGHT/2 - self.Text.get_height()/2 + 100))
        self.update_puntaje_text()  # Actualizar el puntaje justo antes de dibujarlo
        self.screen.blit(self.PuntajeText, (defs.SCREEN_WIDTH/2 - self.PuntajeText.get_width()/2, defs.SCREEN_HEIGHT/2 - self.PuntajeText.get_height()/2 + 200))


    def procesar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                defs.stop_running()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    defs.cambiar_estado(defs.Estados.ST_MENU)

    def tick(self):
        self.procesar_eventos()
        self.dibujar()