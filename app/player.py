import pygame
from .config import Map, ScreenSettings, PlayerConfig,TilesConfig

class Player(pygame.sprite.Sprite):
    """
    Classe que representa o jogador no jogo.

    Atributes:
    ----------
    player_img : pygame.Surface
        Imagem representando o jogador.

    row : int
        Linha inicial do jogador no mapa.

    column : int
        Coluna inicial do jogador no mapa.

    platforms : pygame.sprite.Group
        Grupo de plataformas no jogo.

    blocks : pygame.sprite.Group
        Grupo de blocos no jogo.

    lava : pygame.sprite.Group
        Grupo de lava no jogo.

    water : pygame.sprite.Group
        Grupo de água no jogo.

    element : str
        Tipo do jogador, 'water' ou 'fire'.

    state : str
        Estado atual do jogador, inicializado como 'still'.

    rect : pygame.Rect
        Retângulo que representa a posição e tamanho do jogador.

    speedx : int
        Velocidade horizontal do jogador.

    speedy : int
        Velocidade vertical do jogador.

    highest_y : int
        Altura máxima alcançada pelo jogador antes de começar a cair.

    life : bool
        Indica se o jogador está vivo.

    health : int
        Vida do jogador.
    """
    def __init__(self, player_img : pygame.Surface, row:  int, column : int, 
                 platforms : pygame.sprite.Group, blocks : pygame.sprite.Group, 
                 lava : pygame.sprite.Group, water : pygame.sprite.Group, element : str):
        """
        Inicializa a classe Player.

        Parameters
        ----------
        player_img : pygame.Surface
            Uma superfície Pygame representando a imagem do jogador.
        row : int
            A linha inicial do jogador.
        column : int
            A coluna inicial do jogador.
        platforms : pygame.sprite.Group
            Grupo de sprites representando plataformas no jogo.
        blocks : pygame.sprite.Group
            Grupo de sprites representando blocos no jogo.
        lava : pygame.sprite.Group
            Grupo de sprites representando lava no jogo.
        water : pygame.sprite.Group
            Grupo de sprites representando água no jogo.
        element : str
            Uma string indicando o tipo de jogador (por exemplo, 'água' ou 'fogo').
        """
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = PlayerConfig.STILL

        # Ajusta o tamanho da imagem que representa o boneco
        player_img = pygame.transform.scale(player_img, (PlayerConfig.PLAYER_WIDTH, PlayerConfig.PLAYER_HEIGHT))

        # Define a imagem do sprite.
        self.image = player_img
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda os grupos de sprites para tratar as colisões
        self.platforms = platforms
        self.blocks = blocks
        self.lava = lava
        self.water = water

        # Posiciona o personagem
        self.rect.x = column * TilesConfig.TILE_SIZE
        self.rect.bottom = row * TilesConfig.TILE_SIZE

        # Inicializa velocidades
        self.speedx = 0
        self.speedy = 0

        # Essa variável sempre conterá a maior altura alcançada pelo jogador
        # antes de começar a cair
        self.highest_y = self.rect.bottom

        #Define se o personagem esta vivo
        self.life = True
        
        # Vida do personagem
        self.health = 5

        # Define o tipo de player, se é agua ou fogo
        self._element = element

    @property
    def element(self):
        # Retorna o tipo de elemento ('water' ou 'fire').
        return self._element

    def update(self):
        # Atualiza movimento, colisões e estado.
        self.__update_movement_y()
        self.__check_block_collision()
        self.__check_platform_collision()
        self.__check_lava_collision()
        self.__update_movement_x()
        self.__check_screen_limit()
        self.__check_horizontal_collision()
        self.__death()
        self.__check_water_collision()

    def __update_movement_y(self):
        """
        Atualiza o movimento vertical levando em consideração a gravidade
        e o estado do jogador (se está caindo ou não).
        """
        # Atualiza a velocidade vertical do jogador adicionando a constante
        # de gravidade definida em Map.GRAVITY.
        self.speedy += Map.GRAVITY

        # Verifica se a velocidade vertical (speedy) é maior que zero, 
        # indicando que o jogador está se movendo para baixo.
        if self.speedy > 0:
            # Se a velocidade vertical é positiva, atualiza o estado do 
            # jogador para "FALLING" (cair).
            self.state = PlayerConfig.FALLING

        # Atualiza a posição vertical do jogador com base na sua velocidade vertical.
        self.rect.y += self.speedy

        # Verifica se o estado do jogador não é "FALLING", o que significa
        # que o jogador não está atualmente caindo.
        if self.state != PlayerConfig.FALLING:
            # Nesse caso, atualiza a variável 'highest_y' para conter a 
            # posição mais alta alcançada pelo jogador antes de começar a cair.
            self.highest_y = self.rect.bottom

    def __check_block_collision(self):
        """
        Verifica e trata colisões verticais com blocos. Os blocos
        não podem ser atravessados.
        """
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        
        for collision in collisions:
            
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = PlayerConfig.STILL
            
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom  
                self.speedy = 0
                self.state = PlayerConfig.STILL

    def __check_platform_collision(self):
        """
        Verifica e trata colisões com plataformas, as plataformas só podem
        ser atravessadas por baixo.
        """
        if self.speedy > 0: 
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            
            for platform in collisions:
            
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.highest_y = self.rect.bottom
                    self.speedy = 0
                    self.state = PlayerConfig.STILL

    def __update_movement_x(self):
        """ 
        Atualiza o movimento horizontal usando as coordenadas do rect do sprite.
        """
        self.rect.x += self.speedx

    def __check_screen_limit(self):
        """
        Impede que o player passe do limite lateral da tela.
        """
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= ScreenSettings.WIDTH:
            self.rect.right = ScreenSettings.WIDTH - 1 

    def __check_horizontal_collision(self):
        """
        Verifica e trata colisões horizontais com blocos.
        """
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)        
        
        for collision in collisions:            
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    def __check_lava_collision(self):
        """
        Verifica e trata colisões com elementos de lava. A watergirl morre ao
        encostar na lava e o fireboy pode nadar na lava.
        """
        collisions = pygame.sprite.spritecollide(self, self.lava, False)
        
        for lava in collisions:
            if self._element == 'water' and self.highest_y <= lava.rect.top:
                self.health = 0

    def __check_water_collision(self):
        """
        Verifica e trata colisões com elementos de água. A watergirl pode 
        nadar na água e o fireboy morre ao encostar na água.
        """
        collisions = pygame.sprite.spritecollide(self, self.water, False)
        
        for water in collisions:
            if self._element == 'fire' and self.highest_y <= water.rect.top:
                self.health = 0

    def jump(self):
        """
        Pula se não estiver pulando ou caindo.
        """
        if self.state == PlayerConfig.STILL:
            self.speedy -= PlayerConfig.JUMP_SIZE
            self.state = PlayerConfig.JUMPING

    def walk_to_left(self):
        """
        Move para a esquerda o personagem utilizando a posicao do rect dele
        e a configuração de speed pre definida. A speedx diz o quanto o
        personagem move horizontalmente.
        """
        self.speedx -= PlayerConfig.SPEED_X

    def walk_to_right(self):
        """
        Move para a direita o personagem utilizando a posicao do rect dele
        e a configuração de speed pré definida. A speedx diz o quanto o
        personagem move horizontalmente.
        """
        self.speedx += PlayerConfig.SPEED_X

    def stop_walk_left(self):
        """
        Faz o boneco parar de andar caso estivesse andando para esquerda.
        """
        self.speedx += PlayerConfig.SPEED_X

    def stop_walk_right(self):
        """
        Faz o boneco parar de andar caso estivesse andando para direita.
        """
        self.speedx -= PlayerConfig.SPEED_X

    def __death(self):
        """
        Trata as possibilidades de morte, caso o personagem caia no buraoco
        do mapa, ou caia na água se for o fireboy, ou caia no fogo se for a
        watergirl.
        """
        if self.rect.bottom >= 659 or self.health == 0:
            self.life = False