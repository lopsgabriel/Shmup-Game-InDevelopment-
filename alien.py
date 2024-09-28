from pygame.sprite import Sprite
import pygame

class Alien(Sprite):
    """Cria uma classe para um único Alien da frota"""
    def __init__(self, ai_settings, screen):
        """Inicializa o alien e define sua posição inicial"""
        super(Alien, self).__init__() 
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega uma imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image,(45, 45))
        self.rect = self.image.get_rect()

        #inicia cada novo alien na parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazena a posição exata do alienigena
        self.x = float(self.rect.x)
    def blitme(self):
        """Desenha o alien em sua posição atual"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """move o alienigena para a direita"""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """retorna true se o alienigena atingir a borda"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False


        


