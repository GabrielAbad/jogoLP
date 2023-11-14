import pygame
from os import path
from config import Map, PlayerConfig

class Imgs:
    # Estabelece a pasta que contem as figuras e sons.
    img_dir = path.join(path.dirname(__file__), 'img')

    # Carrega todos os assets de uma vez.
    def load_assets(img_dir):
        assets = {}
        assets[PlayerConfig.PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'hero-single.png')).convert_alpha()
        assets[Map.BLOCK] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
        assets[Map.PLATF] = pygame.image.load(path.join(img_dir, 'tile-wood.png')).convert()
        return assets