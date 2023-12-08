from app.config import ScreenSettings
from app.game import InitialScreen, Game, EndScreen, ModeScreen
import pygame

try:
    screen = pygame.display.set_mode((ScreenSettings.WIDTH, ScreenSettings.HEIGHT))

    tela_inicial = InitialScreen(screen)
    tela_modo = ModeScreen(screen)
    game = Game(screen)
    end = EndScreen(screen)

    phases = [tela_inicial, tela_modo, game, end]

    phase = 0
    while phase < len(phases):
        current_phase = phases[phase]
        current_phase.set_screen()
        current_phase.run()

        if not current_phase.running:
            pygame.quit()
            break

        if not current_phase.running_phase:
            if phase == 2:
                phases[phases[phase].phase_to_go].setresult(phases[phase].result)
            phase = current_phase.phase_to_go

except pygame.error:
    print("O jogo foi fechado.")
except IndexError:
    print("O jogo foi fechado.")
