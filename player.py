import pygame
from config import Map, ScreenSettings, PlayerConfig,TilesConfig

class Player(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img, row, column, platforms, blocks, lava, element):

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
        self.__check_block_colision()
        self.__check_platform_colision()
        self.__check_lava_colision()
        self.__update_movement_x()
        self.__check_horizontal_colision()
        self.__death()

    def __update_movement_y(self):
        self.speedy += Map.GRAVITY
        
        if self.speedy > 0:
            self.state = PlayerConfig.FALLING
        
        self.rect.y += self.speedy

        if self.state != PlayerConfig.FALLING:
            self.highest_y = self.rect.bottom
        
    def __check_block_colision(self):   
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

    def __check_platform_colision(self):
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

    def __check_horizontal_colision(self):
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)        
        
        for collision in collisions:            
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
    
    def __check_lava_colision(self):
        collisions = pygame.sprite.spritecollide(self, self.lava, False)
        
        if self._element == 'water':
            for lava in collisions:
                if self.highest_y <= lava.rect.top:
                    self.health = 0
        if self._element == 'fire':
            for lava in collisions:
                if self.rect.bottom <= lava.rect.top:
                    self.rect.bottom = lava.rect.bottom

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