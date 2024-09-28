import pygame

class Button():
    def __init__(self, ai_settings, screen, msg):
        """inicializa atributos do botão"""
        self.screen = screen 
        self.screen_rect = screen.get_rect()

        #define as proporções e propriedade do botão
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #controi o objeto rect do botão e o centraliza
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #a msg do botão deve ser preparada apenas uma vez
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """transforma msg em uma imagem renderizada e centraliza texto no botão"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """desenha o botão em branco e em seguida, a imagem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
