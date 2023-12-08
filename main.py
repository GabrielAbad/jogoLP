from app.config import ScreenSettings
from app.game import InitialScreen, Game, EndScreen, ModeScreen
import pygame

try:
    screen = pygame.display.set_mode((ScreenSettings.WIDTH, ScreenSettings.HEIGHT))

    tela_inicial = InitialScreen(screen)
    tela_modo = ModeScreen(screen)
    game = Game(screen)
    end = EndScreen(screen)

    phases = [tela_inicial,tela_modo, game, end]

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
                pygame.quit()
            if not phases[phase].running_phase:
                phase += 1
        if phase == 2:
            phases[phase].set_screen()
            phases[phase].run()
            if not phases[phase].running:
                phase += 1
            if not phases[phase].running_phase:
                phases[phases[phase].phase_to_go].setresult(phases[phase].result)
                phase = phases[phase].phase_to_go
            
        if phase == 3:
            phases[phase].set_screen()
            phases[phase].run()
            if not phases[phase].running_phase:
                phase = phases[phase].phase_to_go
            if not phases[phase].running:
                phase += 3


except pygame.error:
    print("O jogo foi fechado.")
except IndexError:
    print("O jogo foi fechado.")