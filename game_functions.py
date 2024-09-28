import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """responde a eventos de pressionamentos de tecla e mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()       
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)    
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """inicia um novo jogo ao clicar play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #ocula o cursor do mouse
        pygame.mouse.set_visible(False)

        #reinicia dados estatisticos do jogo
        stats.reset_stats()
        stats.game_active = True

        #limpa os alienigenas
        aliens.empty()
        bullets.empty()
        ai_settings.initialize_dynamic_settings()

        #cria uma nova frota e cntraliza a nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """responde a keydown events ao pressionar uma tecla"""

    if event.key == pygame.K_RIGHT:
        #move a nave pra direita
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        #move a nave pra esquerda
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        #move a nave para cima
        ship.moving_top = True
    elif event.key == pygame.K_DOWN:
        #move a nave para baixo
        ship.moving_bottom = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """dispara um projetil se o limite ainda não foi alcaçado"""
    
    #cria um novo projetil e o adiciona no grupo de projeteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)   
    
def check_keyup_events(event, ship):
    """responde a keyup event ao soltar uma tecla"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_top = False
    elif event.key == pygame.K_DOWN:
        ship.moving_bottom = False               

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    """Atualiza as imagens da tela e alterna para a mais nova"""
    
    #Redesenha a tela a cada passagem pelo laço 
    screen.fill(ai_settings.bg_color)

    #Redesenha todos os projétesis atrás da espaçonave e dos alienigenas
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)

    #desenha o botão play se o jogo estiver inativo
    if not stats.game_active:
        play_button.draw_button()


    #deixa a tela mais recente visível
    pygame.display.flip()



def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a poseção dos projeteis e se livra dos antigos"""
    #atualiza a poseção dos projeteis
    bullets.update()

    #livra-se dos projeteis que desapareceram
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets):
    """Responde colisoes entre projeteis e alienigenas"""
    #remove qualquer projetil e alienigena atingido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        #destroi os projeteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    """Determina o numero de alienigenas que cabem em uma linha"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #cria um alienigena e posiciona na linha
    alien = Alien(ai_settings, screen)
    alien.width = alien.rect.width
    alien.x = alien.width + 2 * alien.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)



def create_fleet(ai_settings, screen, ship, aliens):
    """cria uma frota de aliens"""

    #cria um alienigena e calcula o nº de alienigenas em uma linha
    #o espaçamento entre eles é igual a largura de um alienigena
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #cria frota de alienigenas
    for row_number in range(number_rows):

        #cria a primeira linha de alienginas
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """determina o numero de linhas de alienigenas que cabem na tela"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def check_fleet_edges(ai_settings, aliens):
    """Responde se um alienigena atingir a borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """faz toda a frota descer e mudar de direção"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Verifica se a frota esta em uma das frotas
    e então atualiza a posição de todos os alienigenas"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #verifica se algum alien atingiu a borda inferior
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    #verifica se houve colisão entre alienigenas e o jogador
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """verifica se um alienigena alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #reinicia o jogo e diminui uma das naves restantes
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responde ao fato da nave ser atingida"""
    #Diminui as naves restantes
    
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #limpa os alienigenas e projeteis
        aliens.empty()
        bullets.empty()

        #cria uma nova frota e centraliza a nave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

         #faz uma pausa
        sleep(0.1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

    





    