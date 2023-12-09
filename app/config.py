"""
Módulo responsável pelas configurações básicas do jogo e estruturas auxiliares 
para a construção de outras funcionalidades do programa.
"""


class Colors:
    """
    Classe que armazena a representação RGB das cores em variáveis significativas.

    Constants:
    ----------
    WHITE : tuple
        Representação RGB da cor branca. Valor: (255, 255, 255).

    BLACK : tuple
        Representação RGB da cor preta. Valor: (0, 0, 0).

    RED : tuple
        Representação RGB da cor vermelha. Valor: (255, 0, 0).

    GREEN : tuple
        Representação RGB da cor verde. Valor: (0, 255, 0).

    BLUE : tuple
        Representação RGB da cor azul. Valor: (0, 0, 255).

    YELLOW : tuple
        Representação RGB da cor amarela. Valor: (255, 255, 0).

    BROWN : tuple
        Representação RGB da cor marrom. Valor: (139, 69, 19).

    Example:
    --------
    Acesso às constantes:
        >>> print(Colors.WHITE)    # Saída: (255, 255, 255)
        >>> print(Colors.BLACK)    # Saída: (0, 0, 0)
        >>> print(Colors.RED)      # Saída: (255, 0, 0)
        >>> print(Colors.GREEN)    # Saída: (0, 255, 0)
        >>> print(Colors.BLUE)     # Saída: (0, 0, 255)
        >>> print(Colors.YELLOW)   # Saída: (255, 255, 0)
        >>> print(Colors.BROWN)    # Saída: (139, 69, 19)
    """
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    BROWN = (139,69,19)


class ScreenSettings:
    """
    Classe que armazena as configurações da tela do pygame.

    Constants:
    ----------
    TITULO : str
        Título que aparece na parte superior da tela.

    WIDTH : int
        Largura da tela em pixels.

    HEIGHT : int
        Altura da tela em pixels.

    FPS : int
        Número de frames por segundo.

    Example:
    --------
    Acesso às constantes (saída pode ser alterada dependendo da config desejada):
    
        >>> print(ScreenSettings.TITULO)   # Saída: 'Caillou'
        >>> print(ScreenSettings.WIDTH)    # Saída: 480
        >>> print(ScreenSettings.HEIGHT)   # Saída: 600
        >>> print(ScreenSettings.FPS)      # Saída: 60
    """
    TITULO = 'Caillou' # Titulo que aprece na parte de cima da tela
    WIDTH = 800 # Largura da tela
    HEIGHT = 800 # Altura da tela
    FPS = 60 # Frames por segundo


class InitialScreenSettings:
    """
    Classe responsável por armazenar as configurações da tela inicial do jogo.

    Constants:
    ----------
    BACKGROUND_IMG : str
        Chave do dicionário de assets que representa a imagem de fundo da tela inicial.

    Example:
    --------
    Acesso à constante:
        >>> print(InitialScreenSettings.BACKGROUND_IMG)   # Saída: 'initial_screen_background'
    """
    #Chave do dicionario de assets
    BACKGROUND_IMG = 'initial_screen_bakground'


class EndScreenSettings:
    """
    Classe responsável por armazenar as configurações da tela de fim de jogo.

    Constants:
    -----------
    WIN_IMG : str
        Chave do dicionário de assets que representa a imagem de vitória na tela final.

    GAMEOVER_IMG : str
        Chave do dicionário de assets que representa a imagem de derrota/game over na tela final.
        
    Example:
    --------
    Acesso às constantes:
        >>> print(EndScreenSettings.WIN_IMG)        # Saída: 'win_img'
        >>> print(EndScreenSettings.GAMEOVER_IMG)   # Saída: 'gameover_img'
    """
    
    # Chaves do dicionario de assets
    WIN_IMG ='win_img' 
    GAMEOVER_IMG = 'gameover_img' 

class ModeScreenSettings:
    """
    Classe responsável por armazenar as configurações da tela de modo de jogo.

    Constants:
    -----------
    BACKGROUND_IMG : str
        Chave do dicionário de assets que representa a imagem de fundo do modo de jogo.
    
    Example:
    --------
    Acesso à constante:
        >>> print(ModeScreenSettings.BACKGROUND_IMG)   # Saída: 'mode_img'
    """
    BACKGROUND_IMG = 'mode_img'

    # Chaves do dicionario de assets

class Map:
    """
    Classe responsável pela estrutura do mapa e configuração da gravidade do jogo.

    Constants:
    ----------
    BLOCK : int
        Representa um bloco no mapa e a chave no dicionário de assets. Valor numérico: 0.

    PLATF : int
        Representa uma plataforma no mapa e a chave no dicionário de assets. Valor numérico: 1.

    LAVA : int
        Representa a lava no mapa e a chave no dicionário de assets. Valor numérico: 2.

    WATER : int
        Representa a água no mapa e a chave no dicionário de assets. Valor numérico: 3.

    EMPTY : int
        Representa uma posição vazia no mapa e a chave no dicionário de assets. Valor numérico: -1.

    GRAVITY : int
        Aceleração da gravidade no jogo. Valor numérico: 5.

    MAP : list
        Matriz que representa a estrutura do mapa. Cada número na matriz representa um tipo de tile.
        Valores possíveis: BLOCK, PLATF, LAVA, WATER, EMPTY.

    Example:
    --------
    Acesso às constantes:
        
        >>> print(Map.BLOCK)   # Saída: 0
        >>> print(Map.PLATF)   # Saída: 1
        >>> print(Map.LAVA)    # Saída: 2
        >>> print(Map.WATER)   # Saída: 3
        >>> print(Map.EMPTY)   # Saída: -1
        >>> print(Map.GRAVITY) # Saída: 5

    Acesso à matriz do mapa:
        
        >>> print(Map.MAP)
    
    """
    
    # Define os tipos de tiles, os números destinados a eles não tem signifcado algum
    BLOCK = 0
    PLATF = 1
    LAVA = 2
    WATER = 3
    EMPTY = -1

    # Define a aceleração da gravidade
    GRAVITY = 5 
    
    # Define o mapa com os tipos de tiles, se empty é porque não tem tile
    MAP= [
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, WATER, WATER, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, BLOCK, BLOCK, WATER, WATER, BLOCK, LAVA, LAVA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
        [BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, PLATF, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY],
        [EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, LAVA, LAVA, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, PLATF, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, LAVA, LAVA, BLOCK, WATER, WATER, BLOCK, BLOCK],
        [BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK]
    ]


class TilesConfig:
    """
    Classe responsável por armazenar as configurações dos blocos no mapa.

    Contants:
    ---------
    TILE_SIZE : int
        Define o tamanho de um bloco no mapa.

    Example:
    --------
    Acesso a constante (saída pode ser alterada dependendo da config desejada):
    
            >>> print(TilesConfig.TILE_SIZE)   # Saída: 40
    """

    TILE_SIZE = 40


class PlayerConfig:
    """
    Classe responsável por armazenar as configurações do jogador.

    Constants:
    ----------
    SPEED_X : int
        Velocidade em que o boneco se move horizontalmente. Valor padrão: 5.

    PLAYER_WIDTH : int
        Largura do boneco. Valor padrão: igual a TILE_SIZE da classe TilesConfig.

    PLAYER_HEIGHT : int
        Altura do boneco. Valor padrão: 1.5 vezes TILE_SIZE da classe TilesConfig.

    JUMP_SIZE : int
        Define a velocidade inicial no pulo. Valor padrão: TILE_SIZE da classe TilesConfig.

    WATERGIRL_IMG : str
        Chave do dicionário de assets que representa a imagem da personagem Watergirl.

    FIREBOY_IMG : str
        Chave do dicionário de assets que representa a imagem da personagem Fireboy.

    STILL : str
        Estado do jogador quando está parado.

    JUMPING : str
        Estado do jogador durante o pulo.

    FALLING : str
        Estado do jogador durante a queda.

    Example:
    --------
    Acesso às constantes (algumas saídas podem ser alteradas dependendo da config desejada):
        
        >>> print(PlayerConfig.SPEED_X)       # Saída: 5
        >>> print(PlayerConfig.PLAYER_WIDTH)   # Saída: 40
        >>> print(PlayerConfig.PLAYER_HEIGHT)  # Saída: 60
        >>> print(PlayerConfig.JUMP_SIZE)      # Saída: 40
        >>> print(PlayerConfig.WATERGIRL_IMG)  # Saída: 'watergirl_img'
        >>> print(PlayerConfig.FIREBOY_IMG)    # Saída: 'fireboy_img'
        >>> print(PlayerConfig.STILL)           # Saída: 'still'
        >>> print(PlayerConfig.JUMPING)         # Saída: 'jumping'
        >>> print(PlayerConfig.FALLING)         # Saída: 'falling'
    """

    SPEED_X = 5

    PLAYER_WIDTH = TilesConfig.TILE_SIZE
    PLAYER_HEIGHT = int(TilesConfig.TILE_SIZE * 1.5)

    JUMP_SIZE = TilesConfig.TILE_SIZE

    WATERGIRL_IMG = 'watergirl_img'
    FIREBOY_IMG = 'fireboy_img'

    STILL = 'still'
    JUMPING = 'jumping'
    FALLING = 'falling'


class DoorConfig:
    """
    Classe responsável por armazenar as configurações das portas no jogo.

    Constants:
    ----------
    DOOR_HEIGHT : int
        Altura das portas no jogo.

    DOOR_WIDTH : int
        Largura das portas no jogo.

    Example:
    --------
    Acesso às constantes:
        >>> print(DoorConfig.DOOR_HEIGHT)   # Exibe a altura das portas (Saída: 60)
        >>> print(DoorConfig.DOOR_WIDTH)    # Exibe a largura das portas (Saída: 40)
    """

    DOOR_HEIGHT = 60
    DOOR_WIDTH = 40