import pygame
from common import defs
from src.player import Player
from src.enemy import Enemy
from src.laser import Laser

class GameForm:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.estado = 0
        self.player = Player(screen)  # Definir una clase Player
        self.enemies = []  # Lista para enemigos
        self.lasers = []  # Lista para lasers
        self.spawn_enemies()  # Método para generar enemigos
        self.score = 0  # Puntaje inicial
        self.ScoreFont = pygame.font.Font("./fonts/Emulogic.ttf", 30)  # Fuente para el puntaje
        self.game_over = False  # Estado para indicar si el juego ha terminado
        self.reset()  # Método para reiniciar el juego

    def __del__(self):
        del self.ScoreFont



    # Método para reiniciar el juego
    def reset(self):
        self.player.rect.centerx = self.screen.get_rect().centerx
        self.player.rect.bottom = self.screen.get_rect().bottom
        self.enemies = []
        self.lasers = []
        self.spawn_enemies()
        self.score = 0
        self.game_over = False
    
    # Método para generar enemigos
    def spawn_enemies(self):
        num_enemies = 10
        for i in range(num_enemies):
            enemy = Enemy(self.screen)
            self.enemies.append(enemy)

    # Método para dibujar
    def dibujar(self):
        self.screen.fill("black")
        self.player.draw()  # Dibujar jugador
        for enemy in self.enemies:
            enemy.draw()  # Dibujar enemigos
        for laser in self.lasers:
            laser.draw()  # Dibujar balas
        
        # Dibujar la puntuación
        score_text = self.ScoreFont.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Ajusta la posición según sea necesario

    # Método para agregar puntaje
    def add_score(self, points):
        self.score += points

    # Método para procesar eventos
    def procesar_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                defs.stop_running()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Disparar con la tecla espacio
                    laser = Laser(self.screen, self.player.rect.centerx, self.player.rect.top)
                    self.lasers.append(laser)
            self.player.handle_event(event)  # Manejar eventos del jugador

    # Método para manejar cuando no hay enemigos
    def handle_no_more_enemies(self):
        defs.cambiar_puntuacion(self.score)
        defs.cambiar_estado(defs.Estados.ST_WIN) 
        self.reset()

    def tick(self):
        self.procesar_eventos()
        self.update_game()
        self.player.update()  # Actualizar jugador

        if self.game_over:
            defs.cambiar_puntuacion(self.score)
            defs.cambiar_estado(defs.Estados.ST_GAMEOVER)  # Detiene el juego, esta función debe cambiar la variable running en defs.py
            self.reset()
            return  # Detiene la ejecución adicional de este método
        
        for laser in self.lasers:
            laser.update()
        self.lasers = [laser for laser in self.lasers if not laser.off_screen()]

        for enemy in self.enemies:
            enemy.update()
        self.enemies = [enemy for enemy in self.enemies if not enemy.off_screen()]
        self.dibujar()
    
    def update_game(self):
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.game_over = True

        # Comprobar si no quedan enemigos
        if not self.enemies:
            self.handle_no_more_enemies()

        for laser in self.lasers:
            laser.update()
            for enemy in self.enemies[:]:
                if laser.rect.colliderect(enemy.rect):
                    self.lasers.remove(laser)
                    self.enemies.remove(enemy)
                    self.add_score(1)  # Aumenta el puntaje por cada enemigo derribado
                    break  # Salir del bucle de enemigos para evitar modificar la lista durante la iteración
                    

        self.enemies = [enemy for enemy in self.enemies if not enemy.off_screen()]
        self.lasers = [laser for laser in self.lasers if not laser.off_screen()]