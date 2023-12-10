import pygame
from .config import TilesConfig


class Tiles(pygame.sprite.Sprite):
    """
    Classe que representa os blocos do cenário.

    Atributes:
    ----------
    image : pygame.Surface
        Imagem que representa o tile.
    rect : pygame.Rect
        Retângulo de colisão do tile no cenário.
    """
    def __init__(self, tile_img:pygame.Surface, row:int, column:int, tile_size:int):
        """
        Inicializa um objeto Tiles.

        Parameters:
        - tile_img (pygame.Surface): Imagem que representa o tile.
        - row (int): Índice da linha onde o tile será posicionado.
        - column (int): Índice da coluna onde o tile será posicionado.
        - tile_size (int): Tamanho do tile em pixels.
        """
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do tile.
        self.image = pygame.transform.scale(tile_img, (tile_size, tile_size))
        
        # Detalhes sobre o tile para tratar colisão.
        self.rect = self.image.get_rect()

        # Posiciona o tile.
        self.rect.x = TilesConfig.TILE_SIZE * column
        self.rect.y = TilesConfig.TILE_SIZE * row

    def check_collision(self, other_sprite):
        """
        Verifica se este tile colidiu com outro sprite.

        Parameters:
        - other_sprite (pygame.sprite.Sprite): O sprite a ser verificado quanto à colisão.

        Returns:
        - bool: True se houver colisão e False se não houver colisão.
        """
        return self.rect.colliderect(other_sprite.rect)