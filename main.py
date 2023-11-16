from config import ScreenSettings
from game import InitialScreen, Game, GameOverScreen
import pygame

try:
    screen = pygame.display.set_mode((ScreenSettings.WIDTH, ScreenSettings.HEIGHT))

    tela_inicial = InitialScreen(screen)
    game = Game(screen)
    gameover = GameOverScreen(screen)

    phases = [tela_inicial, game, gameover]

    phase = 0
    while phase <= len(phases):
        if phase == 0:
            phases[phase].set_screen()
            phases[phase].run()
            if not phases[phase].running:
                pygame.quit()
            if not phases[phase].running_phase:
                phase += 1

        if phase == 1:
            phases[phase].set_screen()
            phases[phase].run()
            if not phases[phase].running:
                phase += 3
            if not phases[phase].running_phase:
                phase = 2
            
        if phase == 2:
            phases[phase].set_screen()
            phases[phase].run()
            if not phases[phase].running_phase:
                phase = phases[phase].phase_to_go
            if not phases[phase].running:
                phase += 3

except pygame.error:
    print("O jogo foi fechado.")