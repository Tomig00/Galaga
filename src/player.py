import pygame

class Player:
    def __init__(self, screen):
        self.screen = screen
        original_image = pygame.image.load('./img/nave.png')  # Carga la imagen de la nave
        self.image = pygame.transform.scale(original_image, (70, 70))  # Escala la imagen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.speed = 5
        self.moving_right = False
        self.moving_left = False

    def __del__(self):
        del self.image

    def update(self):
        # Actualiza la posición de la nave del jugador basado en el movimiento
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed

    def draw(self):
        # Dibuja la nave en su posición actual
        self.screen.blit(self.image, self.rect)

    def handle_event(self, event):
        # Maneja eventos de teclado para mover la nave
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.moving_left = False