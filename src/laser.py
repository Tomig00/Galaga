import pygame


class Laser:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load('./img/laser.png')  # Carga la imagen del laser
        self.image = pygame.transform.scale(self.image, (10, 20))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = -10  # Velocidad del laser

    def __del__(self):
        del self.image

    def update(self):
        # Mueve el laser por la pantalla
        self.rect.y += self.speed

    def draw(self):
        # Dibuja el laser en su posición actual
        self.screen.blit(self.image, self.rect)

    def off_screen(self):
        # Verifica si el laser ha salido de la pantalla
        return self.rect.bottom < 0
