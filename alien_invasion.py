import pygame
import game_functions as gf
from settings import Setting
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from gamestats import GameStats
from button import Button


def run_game():
    #Inicia o jogo e cria um objeto na tela
    pygame.init()
    ai_settings = Setting()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #cria botão play
    play_button = Button(ai_settings, screen, "Play")

    #cria uma instancia para armazenar dados estatisticos
    stats = GameStats(ai_settings)

    #cria uma nave
    ship = Ship(ai_settings, screen)

    #cria um alienigena
    alien = Alien(ai_settings, screen)

    #cria grupo onde será armazenado os projéteis
    bullets = Group()

    #cria uma nave, um grupo de projéteis e um grupo de alienigenas
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #cria uma frota de alienigenas
    gf.create_fleet(ai_settings, screen, ship, aliens)

    

    #inicia laço principal do jogo
    while True:

        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)
        

run_game()



                