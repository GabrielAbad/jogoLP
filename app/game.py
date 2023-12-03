from abc import abstractmethod, ABC
import pygame
from .assets import load_assets, img_dir
from .player import Player
from .config import Map, Colors, ScreenSettings, PlayerConfig, DoorConfig, InitialScreenSettings, EndScreenSettings
from .tiles import Tiles
from os import path


class Screen(ABC):
    def __init__(self, screen):
        self.screen = screen

    @abstractmethod
    def set_screen(self): ...

    @abstractmethod
    def run(self): ...


class Game(Screen):

    def __init__(self, screen):
        super().__init__(screen)
        self._countwaterwin = 0
        self._countfirewin = 0
    
    def set_screen(self):
        self.__initialize()
        self.__create_sprites()
        self.__play_music()
    
    def __initialize(self):
        # Inicialização do Pygame.
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
        self.music_path = path.join(path.dirname(__file__), '..', 'msc','bglmudou.mp3')
        pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)

    @property
    def running(self):
        return self._running
    
    @property
    def running_phase(self):
        return self._running_phase
    
    @property
    def phase_to_go(self):
        return self._phase_to_go

    def run(self):
        self._running_phase = True
        self._running = True
        while self._running and self._running_phase:
            self.__update_events()
            self.__update_screen()
            self.__gameover()
            self.__win()

    def __update_events(self):
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

        self.all_sprites.update()

    @property
    def result(self):
        return self._result

    def __gameover(self):
        for player in self.players:
            if not player.life:
                self._phase_to_go = 2
                self._running_phase = player.life
                self._result = 'lost'

    def __win(self):
        if self.watergirl.rect.left == self.waterdoor.left and self.watergirl.highest_y == self.waterdoor.bottom:
            self._countwaterwin += 1
        if self.fireboy.rect.left == self.firedoor.left and self.fireboy.highest_y == self.firedoor.bottom:
            self._countfirewin += 1
        if self._countwaterwin and self._countfirewin >= 1:
            self._phase_to_go = 2
            self._running_phase = False
            self._result = 'win'
            self._countwaterwin = 0
            self._countfirewin = 0

    def __update_screen(self):
        
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


class EndScreen(Screen):
    
    def __init__(self, screen):
        super().__init__(screen)
        self._result = ''

    def set_screen(self):
        self.__initialize()
        self.__play_music()

    def __initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(ScreenSettings.TITULO)
    
    def __play_music(self):
        pygame.mixer.music.stop()

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
    #TODO
    def __background(self):
        self.assets = load_assets(img_dir)
        if self._result == 'lost':
            self.background = self.assets[EndScreenSettings.GAMEOVER_IMG]
            self.screen.blit(self.background, (0,0))
        elif self._result =='win':
            self.background = self.assets[EndScreenSettings.WIN_IMG]
            self.screen.blit(self.background, (0,0))
   
    def __update_screen(self):
        self.__background()
        pygame.display.flip()

    def setresult(self, result):
        self._result = result

    @property
    def phase_to_go(self):
        return self._phase_to_go
    
    def __update_events(self):
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