class Setting ():
    """Uma classe para armazenar todas as configurações"""
    def __init__(self):
        """inicializa as configurações do jogo"""
        #Configurações da tela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (152, 155, 255)

        #config da nave
        self.ship_limit = 3

        #config projéteis
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #config dos alienigenas
        self.fleet_drop_speed = 10

        #taxa com que a velocidade do jogo aumenta
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """inicia as configurações que mudam ao decorrer do jogo"""
        self.ship_speed_factor = 0.7
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1

        #fleet direction = 1 representa a direita, -1 a esquerda
        self.fleet_direction = 0.3
        
    def increase_speed(self):
        """aumenta as configurações de velocidade"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
