import pygame


class Consts:

    # Game
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800
    FPS = 20
    # Control Panel
    CONTROL_PANEL_WIDTH = 300
    CONTROL_PANEL_HEIGHT = 800
    CONTROL_PANEL_COLOR = (158, 117, 55)
    GOLD_TEXT_COLOR = (255, 255, 255)
    FONT = "inkfree"
    GOLD_TEXT_SIZE = 36
    DESCRIPTION_TEXT_SIZE = 22
    TIME_TEXT_SIZE = 32
    DESCRIPTION_TEXT_COLOR = (255, 255, 255)
    TIME_TEXT_POSITION = (150, 700)
    # Buildings
    BUILDING_0_POSITION = (40, 150)
    TEXT_0_POSITION = (70, 230)
    BUILDING_1_POSITION = (180, 150)
    TEXT_1_POSITION = (212, 230)
    BUILDING_2_POSITION = (40, 300)
    TEXT_2_POSITION = (70, 380)
    BUILDING_3_POSITION = (180, 300)
    TEXT_3_POSITION = (212, 380)
    BUILDING_4_POSITION = (40, 450)
    TEXT_4_POSITION = (70, 530)
    BUILDING_ICON_SIZE = 64
    NUMBER_OF_ROWS = 5
    NUMBER_OF_COLUMNS = 5
    # Game board
    GAME_BOARD_COLOR = (56, 213, 66)
    GAME_BOARD_WIDTH = 900
    GAME_BOARD_HEIGHT = 800
    GRID = [[(400, 50), (500, 50), (600, 50), (700, 50), (800, 50)],
            [(400, 150), (500, 150), (600, 150), (700, 150), (800, 150)],
            [(400, 250), (500, 250), (600, 250), (700, 250), (800, 250)],
            [(400, 350), (500, 350), (600, 350), (700, 350), (800, 350)],
            [(400, 450), (500, 450), (600, 450), (700, 450), (800, 450)]]
    # Building costs
    GOLD_MINE_COST = 5000
    GOLD_MINT_COST = 10000
    QUARRY_COST = 500
    SAWMILL_COST = 3000
    WOODCUTTERS_HUT_COST = 1500


class Assets:
    """It stores graphic resources."""
    # pylint: disable=too-few-public-methods

    @classmethod
    def load(cls):
        cls.GAME_BACKGROUND = pygame.image.load("assets/game_background.png")
        cls.CONTROL_PANEL_BACKGROUND = pygame.image.load("assets/wood_background.png")
        cls.GOLD_MINE = pygame.image.load("assets/gold_mine.png")
        cls.GOLD_MINT = pygame.image.load("assets/gold_mint.png")
        cls.QUARRY = pygame.image.load("assets/quary.png")
        cls.SAWMILL = pygame.image.load("assets/sawmill.png")
        cls.TREASURE = pygame.image.load("assets/treasure.png")
        cls.WOODCUTTERS = pygame.image.load("assets/woodcutters.png")
