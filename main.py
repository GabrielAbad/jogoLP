from app.config import ScreenSettings
from app.game import InitialScreen, Game, EndScreen, ModeScreen
import pygame

libraries = [
    "pygame",  
    "numpy",   
    "pandas",  
    "matplotlib"  
]
missing_libraries = []

for lib in libraries:
    try:
        __import__(lib)
    except ImportError:
        print(f"{lib} Não foi instalada.")
        missing_libraries.append(lib)

if missing_libraries:
    print(f"As seguintes biblitecas não estão presentes: {', '.join(missing_libraries)}")


try:
    screen = pygame.display.set_mode((ScreenSettings.WIDTH, ScreenSettings.HEIGHT))

    tela_inicial = InitialScreen(screen)
    game = Game(screen)
    end = EndScreen(screen)

    phases = [tela_inicial, game, end]

    phase = 0
    while phase < len(phases):
        print(f"Current Phase: {phase}")  # Adding this line to print the current phase
        if phase == 0:
            #tela inicial
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
                # Pega se o personagem morreu ou concluiram a fase
                phases[phases[phase].phase_to_go].setresult(phases[phase].result)
                phase = phases[phase].phase_to_go
            
        if phase == 2:
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