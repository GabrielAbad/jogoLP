class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BROWN = (139,69,19)


class ScreenSettings:
    TITULO = 'Nome do Jogo' # Titulo que aprece na parte de cima da tela
    WIDTH = 480 # Largura da tela
    HEIGHT = 600 # Altura da tela
    FPS = 60 # Frames por segundo


class Map:
    # Define os tipos de tiles
    BLOCK = 0
    PLATF = 1
    LAVA = 2
    EMPTY = -1

    # Define a aceleração da gravidade
    GRAVITY = 5
    
    # Define o mapa com os tipos de tiles, se empty é porque não tem tile
    MAP = [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, PLATF, PLATF, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY, EMPTY],
        [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
        [EMPTY, EMPTY, BLOCK, BLOCK, LAVA, LAVA, LAVA, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
        [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
        [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
    ]


class TilesConfig:
    #Define o tamanho de um bloco no mapa
    TILE_SIZE = 40


class PlayerConfig:
    
    # Velocidade em que o boneco anda
    SPEED_X = 5
    
    # Dimensões do boneco
    PLAYER_WIDTH = TilesConfig.TILE_SIZE
    PLAYER_HEIGHT = int(TilesConfig.TILE_SIZE * 1.5)

    # Define a velocidade inicial no pulo
    JUMP_SIZE = TilesConfig.TILE_SIZE

    PLAYER_IMG = 'player_img'

    # Define estados possíveis do jogador
    STILL = 'still'
    JUMPING = 'jumping'
    FALLING = 'falling'


class DoorConfig:
    DOOR_HEIGHT = 60
    DOOR_WIDTH = 40