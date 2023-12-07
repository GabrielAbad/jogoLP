'''
Módulo responsável pelas assets do jogo.
'''

import pygame
from os import path
from .config import Map, PlayerConfig, InitialScreenSettings, EndScreenSettings, ModeScreenSettings

    
# Estabelece a pasta que contem as figuras.
img_dir = path.join('..', 'img')

# Carrega todos os assets de uma vez.
def load_assets(img_dir : str) -> dict:
    '''
    Função que carrega e guarda as imagens dos blocos e personagens do jogo.

    Parameters
    ----------
    img_dir : str
        O caminho pro diretório em que estão as imagens.

    Returns
    -------
    assets : dict
        Um dict que as chaves são nomes significativos para os blocos e personagens, 
        e os valores são as imagens carregadas dos blocos e personagens.

    '''
    assets = {}
    assets[PlayerConfig.WATERGIRL_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'watergirlpenut.png')).convert_alpha()
    assets[PlayerConfig.FIREBOY_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'fireboypenut.png')).convert_alpha()
    assets[Map.BLOCK] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'tile-block.png')).convert()
    assets[Map.PLATF] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'tile-wood.png')).convert()
    assets[Map.LAVA] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'lava.png')).convert()
    assets[Map.WATER] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'water.jpg')).convert()
    assets[InitialScreenSettings.BACKGROUND_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'SUPER.jpg')).convert()
    assets[EndScreenSettings.WIN_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'youwin.jpg')).convert()
    assets[EndScreenSettings.GAMEOVER_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'gameover.jpg')).convert()
    assets[ModeScreenSettings.BACKGROUND_IMG] = pygame.image.load(path.join(path.dirname(__file__),img_dir, 'mode.jpg')).convert()

    return assets
