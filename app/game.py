from abc import abstractmethod, ABC
import pygame
from .assets import load_assets, img_dir
from .player import Player
from .config import Map, Colors, ScreenSettings, PlayerConfig, DoorConfig, InitialScreenSettings, EndScreenSettings,ModeScreenSettings
from .tiles import Tiles
from os import path
from math import dist

class Screen(ABC):
    """
    Classe abstrata que representa uma tela de jogo ou uma tela estática.

    Atributes:
    ----------
    screen : pygame.display
        Para começar o pygame sempre precisa de uma interface
    """

    def __init__(self, screen:pygame.display):
        """
        Construtor para inicializar o objeto que herda de Screen.
        Lembrando que essa classe é abstrata, então esse método serve apenas
        para ser herdado pelas 3 classes filhas dela para que possam ser 
        construídas.

        Parameters:
        -----------
        screen : pygame.display
            Para começar o pygame sempre precisa de uma interface
        """
        self.screen = screen

    @abstractmethod
    def set_screen(self):
        """
        Método abstrato para definir o conteúdo da tela.
        Este método deve ser implementado por subclasses concretas.
        """
        ...

    @abstractmethod
    def run(self): 
        """
        Método abstrato para executar a funcionalidade da tela.
        Este método deve ser implementado por subclasses concretas.
        """
        ...


class Game(Screen):
    """
    Representa a tela principal do jogo.

    Esta classe controla a lógica e a execução do jogo.
    """

    def __init__(self, screen):
        """
        Inicializa a tela do jogo.

        Args:
            screen (pygame.Surface): A superfície onde o jogo será renderizado.
        """
        super().__init__(screen)
        self._countwaterwin = 0
        self._countfirewin = 0
    
    def set_screen(self):
        """
        Configura a tela do jogo.

        Esta função inicializa o Pygame, configura a tela, carrega assets e cria os sprites.
        """
        self.__initialize()
        self.__create_sprites()
        self.__play_music()
    
    def __initialize(self):
        """
        Inicializa o Pygame e configurações iniciais do jogo.
        """
        pygame.init()
        pygame.mixer.init()

        # Nome do jogo
        pygame.display.set_caption(ScreenSettings.TITULO)
    
    
        # Variável para o ajuste de velocidade
        self.clock = pygame.time.Clock()

        # Carrega assets
        self.assets = load_assets(img_dir)

        # Cria os grupos de Sprite
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.lava = pygame.sprite.Group()
        self.water = pygame.sprite.Group()

        # Portas da vitória
        self.firedoor = pygame.Rect(80,60 , DoorConfig.DOOR_WIDTH, DoorConfig.DOOR_HEIGHT)
        self.waterdoor = pygame.Rect(120,60 , DoorConfig.DOOR_WIDTH, DoorConfig.DOOR_HEIGHT)

    def __create_sprites(self):
        """
        Cria os sprites do jogo.

        Esta função cria os jogadores, cria os tiles do mapa e os adiciona aos grupos de sprites.
        """
        
        self.fireboy = Player(self.assets[PlayerConfig.FIREBOY_IMG], 13, 0, self.platforms, self.blocks,self.lava,self.water,'fire')
        self.watergirl = Player(self.assets[PlayerConfig.WATERGIRL_IMG], 13, 1, self.platforms, self.blocks,self.lava,self.water ,'water')
        self.players =[self.watergirl,self.fireboy]

        # Cria tiles de acordo com o mapa
        for row in range(len(Map.MAP)):
            for column in range(len(Map.MAP[row])):
                tile_type = Map.MAP[row][column]
                if tile_type != Map.EMPTY:
                    tile = Tiles(self.assets[tile_type], row, column,40)
                    self.all_sprites.add(tile)
                    if tile_type == Map.BLOCK:
                        self.blocks.add(tile)
                    elif tile_type == Map.PLATF:
                        self.platforms.add(tile)
                    elif tile_type == Map.LAVA:
                        self.lava.add(tile)
                    elif tile_type == Map.WATER:
                        self.water.add(tile)

        # Adiciona o jogador no grupo de sprites por último para ser desenhado por cima das plataformas
        self.all_sprites.add(player for player in self.players)
    
    def __play_music(self):
        """
        Toca a música de fundo do jogo.
        """
        self.music_path = path.join(path.dirname(__file__), '..', 'msc','bglmudou.mp3')
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

    @property
    def running(self):
        """
        Propriedade que indica se o jogo está em execução.

        Returns:
            bool: True se o jogo está em execução, False caso contrário.
        """
        return self._running
    
    @property
    def running_phase(self):
        """
        Propriedade que indica se a fase do jogo está em execução.

        Returns:
            bool: True se a fase está em execução, False caso contrário.
        """
        return self._running_phase
    
    @property
    def phase_to_go(self):
        """
        Propriedade que retorna a próxima fase do jogo.

        Returns:
            int: O número da próxima fase.
        """
        return self._phase_to_go

    def run(self):
        """
        Inicia o loop principal do jogo.

        Este método atualiza os eventos, a tela do jogo, verifica as condições de fim de jogo e de vitória.
        """
        self._running_phase = True
        self._running = True
        while self._running and self._running_phase:
            self.__update_events()
            self.__update_screen()
            self.__gameover()
            self.__win()

    def __update_events(self):
        """
        Atualiza os eventos do jogo.

        Este método processa eventos como teclas pressionadas, cliques do mouse, etc.
        """
        # Ajusta a velocidade do jogo.
        self.clock.tick(ScreenSettings.FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                self._running = False
            for player in self.players:
                if player.element == 'water':
                    # Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        # Dependendo da tecla, altera o estado do jogador.
                        if event.key == pygame.K_LEFT:
                            player.walk_to_left()
                        if event.key == pygame.K_RIGHT:
                            player.walk_to_right()
                        if event.key == pygame.K_UP:
                            player.jump()

                    # Verifica se soltou alguma tecla.
                    if event.type == pygame.KEYUP:
                        # Dependendo da tecla, altera o estado do jogador.
                        if event.key == pygame.K_LEFT:
                            player.stop_walk_left()
                        elif event.key == pygame.K_RIGHT:
                            player.stop_walk_right()
                
                elif player.element == 'fire':
                    # Verifica se apertou alguma tecla.
                    if event.type == pygame.KEYDOWN:
                        # Dependendo da tecla, altera o estado do jogador.
                        if event.key == pygame.K_a:
                            player.walk_to_left()
                        if event.key == pygame.K_d:
                            player.walk_to_right()
                        if event.key == pygame.K_w:
                            player.jump()

                    # Verifica se soltou alguma tecla.
                    if event.type == pygame.KEYUP:
                        # Dependendo da tecla, altera o estado do jogador.
                        if event.key == pygame.K_a:
                            player.stop_walk_left()
                        elif event.key == pygame.K_d:
                            player.stop_walk_right()
                    # Verifica se as teclas 'm', 'k' ou 'l' foram pressionadas.
                keys = pygame.key.get_pressed()

                # Aumenta o volume se a tecla 'k' for pressionada.
                if keys[pygame.K_k]:
                    pygame.mixer.music.set_volume(min(1.0, pygame.mixer.music.get_volume() + 0.01))

                # Diminui o volume se a tecla 'l' for pressionada.
                if keys[pygame.K_l]:
                    pygame.mixer.music.set_volume(max(0.0, pygame.mixer.music.get_volume() - 0.01))

        self.all_sprites.update()

    @property
    def result(self):
        """
        Retorna o resultado do jogo.

        Returns:
            str: O resultado do jogo (ganhou ou perdeu).
        """
        return self._result

    def __gameover(self):
        """
        Verifica se o jogo chegou ao fim (game over).
        """
        for player in self.players:
            if not player.life:
                self._phase_to_go = 2
                self._running_phase = player.life
                self._result = 'lost'

    def __win(self):
        """
        Verifica se houve vitória no jogo.
        """
        coord_watergirl = (self.watergirl.rect.x,self.watergirl.rect.y)
        coord_waterdoor = (self.waterdoor.x,self.waterdoor.y)
        coord_fireboy = (self.fireboy.rect.x,self.fireboy.rect.y)
        coord_firedoor = (self.firedoor.x, self.firedoor.y)





        if dist(coord_watergirl,coord_waterdoor)<5:
            self._countwaterwin += 1
        if dist(coord_fireboy, coord_firedoor) < 5:
            self._countfirewin += 1
        if self._countwaterwin or self._countfirewin >= 1:
            self._phase_to_go = 2
            self._running_phase = False
            self._result = 'win'
            self._countwaterwin = 0
            self._countfirewin = 0

    def __update_screen(self):
        """
        Atualiza a tela do jogo.

        Este método desenha todos os sprites na tela, atualiza a tela e realiza a troca de buffers.
        """
        
        # Preenche o fundo de branco
        self.screen.fill(Colors.WHITE)
        
        # Desenha todas as sprites na tela
        self.all_sprites.draw(self.screen)

        # Desenha as portas que tem que chegar
        pygame.draw.rect(self.screen,Colors.BLUE,self.waterdoor)
        pygame.draw.rect(self.screen,Colors.RED,self.firedoor)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()


class InitialScreen(Screen):

    def set_screen(self):
        self.__initialize()
        self.__play_music()

    def __initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(ScreenSettings.TITULO)

    def __play_music(self):
        self.music_path = path.join(path.dirname(__file__), '..','msc','caillou_theme_song.mp3')
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)
    
    @property
    def running(self):
        return self._running
    
    @property
    def running_phase(self):
        return self._running_phase
    
    def run(self):
        self._running = True
        self._running_phase = True
        while self.running and self.running_phase:
            self.__update_events()
            self.__update_screen()
    

    def __update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._running_phase = False
    
    def __background(self):
        # Carrega assets
        self.assets = load_assets(img_dir)
        self.background = self.assets[InitialScreenSettings.BACKGROUND_IMG]
        self.screen.blit(self.background, (0,0))
    
    def __update_screen(self):
        self.__background()
        pygame.display.flip()


class ModeScreen(Screen):
    """
    Representa a tela de seleção de modo do jogo.

    Nesta tela, o jogador pode escolher entre diferentes modos de jogo.
    """

    def set_screen(self):
        """
        Configura a tela do modo de jogo.

        Esta função inicializa o Pygame, configura a tela e inicia a música de fundo.
        """
        self.__initialize()
        self.__play_music()

    def __initialize(self):
        """
        Inicializa o Pygame e configurações iniciais do modo de jogo.
        """
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(ScreenSettings.TITULO)

    def __play_music(self):
        """
        Toca a música de fundo do modo de jogo.
        """
        self.music_path = path.join(path.dirname(__file__), '..','msc','caillou_theme_song.mp3')
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)
    
    @property
    def running(self):
        """
        Propriedade que indica se o jogo está em execução.

        Returns:
            bool: True se o jogo está em execução, False caso contrário.
        """
        return self._running
    
    @property
    def running_phase(self):
        """
        Propriedade que indica se a fase do jogo está em execução.

        Returns:
            bool: True se a fase está em execução, False caso contrário.
        """
        return self._running_phase
    
    def run(self):
        """
        Inicia o loop principal do modo de jogo.

        Este método atualiza os eventos e a tela do modo de jogo.
        """
        self._running = True
        self._running_phase = True
        while self.running and self.running_phase:
            self.__update_events()
            self.__update_screen()
    

    def __update_events(self):
        """
        Atualiza os eventos do modo de jogo.

        Este método processa eventos como teclas pressionadas para selecionar o modo de jogo.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self._running_phase = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    self._running_phase = False
    
    def __background(self):
        """
        Define o background da tela do modo de jogo.
        """
        # Carrega assets
        self.assets = load_assets(img_dir)
        self.background = self.assets[ModeScreenSettings.BACKGROUND_IMG]
        self.screen.blit(self.background, (0,0))
    
    def __update_screen(self):
        """
        Atualiza a tela do modo de jogo.

        Este método desenha o background na tela do modo de jogo.
        """
        self.__background()
        pygame.display.flip()

class EndScreen(Screen):
    """
    Representa a tela de fim de jogo.

    Nesta tela, é exibido o resultado final do jogo (vitória ou derrota).
    """
    
    def __init__(self, screen):
        """
        Inicializa a tela de fim de jogo.

        Args:
            screen (pygame.Surface): A superfície onde a tela de fim de jogo será renderizada.
        """
        super().__init__(screen)
        self._result = ''

    def set_screen(self):
        """
        Configura a tela de fim de jogo.

        Esta função inicializa o Pygame, configura a tela e interrompe a música de fundo.
        """
        self.__initialize()
        self.__play_music()

    def __initialize(self):
        """
        Inicializa o Pygame e configurações iniciais da tela de fim de jogo.
        """
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(ScreenSettings.TITULO)
    
    def __play_music(self):
        """
        Interrompe a reprodução da música de fundo na tela de fim de jogo.
        """
        pygame.mixer.music.stop()

    @property
    def running(self):
        """
        Propriedade que indica se o jogo está em execução.

        Returns:
            bool: True se o jogo está em execução, False caso contrário.
        """
        return self._running
    
    @property
    def running_phase(self):
        """
        Propriedade que indica se a fase do jogo está em execução.

        Returns:
            bool: True se a fase está em execução, False caso contrário.
        """
        return self._running_phase

    def run(self):
        """
        Inicia o loop principal da tela de fim de jogo.

        Este método atualiza os eventos e a tela da tela de fim de jogo.
        """
        self._running = True
        self._running_phase = True
        while self.running and self.running_phase:
            self.__update_events()
            self.__update_screen()
    
    def __background(self):
        """
        Define o background da tela de fim de jogo baseado no resultado (vitória ou derrota).
        """
        self.assets = load_assets(img_dir)
        if self._result == 'lost':
            self.background = self.assets[EndScreenSettings.GAMEOVER_IMG]
            self.screen.blit(self.background, (0,0))
        elif self._result =='win':
            self.background = self.assets[EndScreenSettings.WIN_IMG]
            self.screen.blit(self.background, (0,0))
   
    def __update_screen(self):
        """
        Atualiza a tela da tela de fim de jogo.

        Este método desenha o background na tela de fim de jogo.
        """
        self.__background()
        pygame.display.flip()

    def setresult(self, result):
        """
        Define o resultado do jogo.

        Args:
            result (str): Resultado do jogo ('win' para vitória ou 'lost' para derrota).
        """
        self._result = result

    @property
    def phase_to_go(self):
        """
        Retorna a fase para a qual o jogo deve ir após a tela de fim de jogo.

        Returns:
            int: Número da fase seguinte.
        """
        return self._phase_to_go
    
    def __update_events(self):
        """
        Atualiza os eventos da tela de fim de jogo.

        Este método processa eventos como teclas pressionadas para escolher a próxima fase ou sair do jogo.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if self._result == 'lost':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self._phase_to_go = 1
                        self._running_phase = False
                    if event.key == pygame.K_m:
                        self._phase_to_go = 0
                        self._running_phase = False
            elif self._result == 'win':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self._phase_to_go = 0
                        self._running_phase = False