import pygame
from common import defs
class MenuForm:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.estado = 0
        self.TitleFont = pygame.font.Font("./fonts/Emulogic.ttf", 72)
        self.ButtonFont = pygame.font.Font("./fonts/Emulogic.ttf", 36)
        self.TitleText = self.TitleFont.render("GALAGA", True, "white")
        self.ButtonText = self.ButtonFont.render("Jugar", True, "Green")
    
    def __del__(self):
        del self.TitleFont
        del self.ButtonFont

    
    def dibujar(self):
        self.screen.fill("black")
        self.screen.blit(self.TitleText, (defs.SCREEN_WIDTH/2 - self.TitleText.get_width()/2, defs.SCREEN_HEIGHT/2 - self.TitleText.get_height()/2))
        self.screen.blit(self.ButtonText, (defs.SCREEN_WIDTH/2 - self.ButtonText.get_width()/2, defs.SCREEN_HEIGHT/2 - self.ButtonText.get_height()/2 + 100))
        


    def procesar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                defs.stop_running()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if defs.SCREEN_WIDTH/2 - self.ButtonText.get_width()/2 <= event.pos[0] <= defs.SCREEN_WIDTH/2 + self.ButtonText.get_width()/2 and defs.SCREEN_HEIGHT/2 - self.ButtonText.get_height()/2 + 100 <= event.pos[1] <= defs.SCREEN_HEIGHT/2 + self.ButtonText.get_height()/2 + 100:
                        defs.cambiar_estado(defs.Estados.ST_GAME)


    def tick(self):
        self.procesar_eventos()
        self.dibujar()
    
