import pygame
import random

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./img/enemigo.png')  # Carga la imagen del enemigo
        self.image = pygame.transform.scale(self.image, (40, 40))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(-300, -50)
        self.speed_x = random.randint(1, 2)  # Velocidad horizontal aleatoria
        self.speed_y = random.randint(1, 2)  # Velocidad vertical

    def __del__(self):
        del self.image

    def update(self):
        # Actualiza la posición del enemigo
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        # Cambia de dirección si llega al borde de la pantalla
        if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
            self.speed_x *= -1

    def draw(self):
        # Dibuja el enemigo en su posición actual
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        # Verifica si el enemigo ha salido de la pantalla
        return self.rect.top > self.screen.get_height()