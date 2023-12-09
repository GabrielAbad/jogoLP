'''
Módulo responsável pelo gerenciamento dos recursos visuais do jogo.
'''


import pygame
from os import path
from .config import Map, PlayerConfig, InitialScreenSettings, EndScreenSettings, ModeScreenSettings

    
# Define o diretório que contém as imagens.
img_dir = path.join('..', 'img')


def load_assets(img_dir: str) -> dict:
    '''
    Carrega e armazena as imagens dos blocos e personagens do jogo.

    Parameters
    ----------
    img_dir : str
        O caminho para o diretório que contém as imagens.

    Returns
    -------
    assets : dict
        Um dicionário onde as chaves representam nomes significativos para blocos e personagens, 
        e os valores são as imagens carregadas dos blocos e personagens.
    '''
    assets = {}
    assets[PlayerConfig.WATERGIRL_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'watergirlpenut.png')).convert_alpha()
    assets[PlayerConfig.FIREBOY_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'fireboypenut_resized.png')).convert_alpha()
    assets[Map.BLOCK] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'dirtblock.png')).convert()
    assets[Map.PLATF] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'tile-wood.png')).convert()
    assets[Map.LAVA] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'lavablock.png')).convert()
    assets[Map.WATER] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'waterblock.png')).convert()
    assets[InitialScreenSettings.BACKGROUND_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'startscream_resized.jpg')).convert()
    assets[EndScreenSettings.WIN_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'youwin_resized.jpg')).convert()
    assets[EndScreenSettings.GAMEOVER_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'gameover_resized.jpg')).convert()
    assets[ModeScreenSettings.BACKGROUND_IMG] = pygame.image.load(path.join(path.dirname(__file__), img_dir, 'mode_resized.jpg')).convert()

    return assets