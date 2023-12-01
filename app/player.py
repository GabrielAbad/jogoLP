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

    Metods:
    -------
    __init__(self, player_img, row, column, platforms, blocks, lava, water, element)
        Construtor da classe.

    update(self)
        Atualiza o estado do jogador, chama todos os métodos privados da classe.

    jump(self)
        Função para fazer o jogador pular.

    walk_to_left(self)
        Move o jogador para a esquerda.

    walk_to_right(self)
        Move o jogador para a direita.

    stop_walk_left(self)
        Para o movimento do jogador para a esquerda.

    stop_walk_right(self)
        Para o movimento do jogador para a direita.

    __death(self)
        Verifica se o jogador morreu.

    __update_movement_y(self)
        Atualiza o movimento vertical do jogador.

    __check_block_collision(self)
        Verifica colisões com blocos.

    __check_platform_collision(self)
        Verifica colisões com plataformas.

    __update_movement_x(self)
        Atualiza o movimento horizontal do jogador.

    __check_horizontal_collision(self)
        Verifica colisões horizontais.

    __check_lava_collision(self)
        Verifica colisões com lava.

    __check_water_collision(self)
        Verifica colisões com água.
    """
    # Construtor da classe.
    def __init__(self, player_img, row, column, platforms, 
                 blocks, lava, water, element):

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

        # Define altura no mapa
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
        return self._element

    def update(self):
        self.__update_movement_y()
        self.__check_block_collision()
        self.__check_platform_collision()
        self.__check_lava_collision()
        self.__update_movement_x()
        self.__check_horizontal_collision()
        self.__death()
        self.__check_water_collision()

    def __update_movement_y(self):
        self.speedy += Map.GRAVITY
        
        if self.speedy > 0:
            self.state = PlayerConfig.FALLING
        
        self.rect.y += self.speedy

        if self.state != PlayerConfig.FALLING:
            self.highest_y = self.rect.bottom
        
    def __check_block_collision(self):   
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
        if self.speedy > 0: 
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            
            for platform in collisions:
               
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.highest_y = self.rect.bottom
                    self.speedy = 0
                    self.state = PlayerConfig.STILL

    def __update_movement_x(self):
        self.rect.x += self.speedx

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= ScreenSettings.WIDTH:
            self.rect.right = ScreenSettings.WIDTH - 1 

    def __check_horizontal_collision(self):
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)        
        
        for collision in collisions:            
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
    
    def __check_lava_collision(self):
        collisions = pygame.sprite.spritecollide(self, self.lava, False)
        
        for lava in collisions:
            if self._element == 'water':
                if self.highest_y <= lava.rect.top:
                    self.health = 0                       
    
    def __check_water_collision(self):
        collisions = pygame.sprite.spritecollide(self, self.water, False)
        
        for water in collisions:
            if self._element == 'fire':
                if self.highest_y <= water.rect.top:
                    self.health = 0

    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == PlayerConfig.STILL:
            self.speedy -= PlayerConfig.JUMP_SIZE
            self.state = PlayerConfig.JUMPING

    def walk_to_left(self):
        self.speedx -= PlayerConfig.SPEED_X

    def walk_to_right(self):
        self.speedx += PlayerConfig.SPEED_X
    
    def stop_walk_left(self):
        self.speedx += PlayerConfig.SPEED_X
    
    def stop_walk_right(self):
        self.speedx -= PlayerConfig.SPEED_X

    def __death(self):
        if self.rect.bottom >= 659:
            self.life = False
        if self.health == 0:
            self.life = False