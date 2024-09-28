class GameStats():
    """Armazena dados estatisticos do jogo"""
    def __init__(self, ai_settings):
        """inicializa os dados estatisticos"""
        self.ai_settings = ai_settings
        self.reset_stats()    
        #inicia a invasão alienigena em um estado inativo
        self.game_active = False



    def reset_stats(self):
        """inicializa dados estatisticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit

