import pygame
from os import path
from config import Map, PlayerConfig

class Imgs:
    # Estabelece a pasta que contem as figuras.
    img_dir = path.join(path.dirname(__file__), 'img')

    # Carrega todos os assets de uma vez.
    def load_assets(img_dir):
        assets = {}
        assets[PlayerConfig.WATERGIRL_IMG] = pygame.image.load(path.join(img_dir, 'watergirl.png')).convert_alpha()
        assets[PlayerConfig.FIREBOY_IMG] = pygame.image.load(path.join(img_dir, 'fireboy.png')).convert_alpha()
        assets[Map.BLOCK] = pygame.image.load(path.join(img_dir, 'tile-block.png')).convert()
        assets[Map.PLATF] = pygame.image.load(path.join(img_dir, 'tile-wood.png')).convert()
        assets[Map.LAVA] = pygame.image.load(path.join(img_dir, 'lava.png')).convert()
        assets[Map.WATER] = pygame.image.load(path.join(img_dir, 'water.jpg')).convert()
        return assets