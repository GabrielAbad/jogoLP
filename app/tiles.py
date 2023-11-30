import pygame

# Classe que representa os blocos do cenário
class Tiles(pygame.sprite.Sprite):

    TILE_SIZE = 40
    
    # Construtor da classe.
    def __init__(self, tile_img, row, column,tile_size):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Ajusta o tamanho da imagem que representa o tile de acordo com o tamanho do asset
        tile_img = pygame.transform.scale(tile_img, (tile_size, tile_size))

        # Define a imagem do tile.
        self.image = tile_img
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile 
        self.rect.x = self.TILE_SIZE * column
        self.rect.y = self.TILE_SIZE * row