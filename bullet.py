import pygame
from pygame.sprite import Group, Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela nave"""
    def __init__(self, ai_settings, screen, ship):
        """cria um objeto projetil na posição atual da nave"""
        super(Bullet, self).__init__()
        self.screen = screen

        #cria um retangulo para o projetil em (0, 0) e depois define 
        # a posição correta 
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #armazena a posição do projetil em um valor decimal 
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

        
    def update(self):
        """move o projetil para cima na tela"""

        #atualiza a posição decimal do projetil
        self.y -= self.speed_factor

        #atualiza a posição do projetil
        self.rect.y = self.y

    
    def draw_bullet(self):
        """Desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)