import pygame

class Ship():
    def __init__(self, ai_settings , screen):
        """inicializa a nave e define sua posição"""
        self.screen = screen
        self.ai_settings = ai_settings

        #carrega a imagem da nave e obtem seu rect
        self.image = pygame.image.load('images/navebmp-1.bmp')
        self.image = pygame.transform.scale(self.image,(50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova nave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #armazena um valor decimal para o movimento da nave
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        #flag de movimento
        self.moving_right = False
        self.moving_left = False
        # self.moving_top = False
        # self.moving_bottom = False
    
    def update(self):
        """Atualiza a posição da nave de acordo com a flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #move para direita
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            #move para esquerda
            self.center -= self.ai_settings.ship_speed_factor

        # if self.moving_top and self.rect.top > self.screen_rect.top:
        #     #move para cima
        #     self.centery -= self.ai_settings.ship_speed_factor

        # if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
        #     #move pra baixo
        #     self.centery += self.ai_settings.ship_speed_factor

            
        #atualiza o objeto self rect com o self center
        self.rect.centerx = self.center
        # self.rect.centery = self.centery
    
    def blitme(self):
        """desenha a nave na posição atual"""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """centraliza a nave"""
        self.center = self.screen_rect.centerx

