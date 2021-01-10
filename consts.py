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
    FONT = "inkfree"
    # Gold
    GOLD_TEXT_COLOR = (255, 255, 255)
    GOLD_TEXT_SIZE = 36
    GOLD_TEXT_MARGIN_TOP = 50
    # Timer
    TIME_TEXT_SIZE = 32
    TIME_TEXT_POSITION = (150, 720)
    # Icons in colntrol panel
    PANEL_BUILDING_0_POSITION = (40, 130)
    PANEL_BUILDING_1_POSITION = (180, 130)
    PANEL_BUILDING_2_POSITION = (40, 280)
    PANEL_BUILDING_3_POSITION = (180, 280)
    PANEL_BUILDING_4_POSITION = (40, 430)
    ICON_SIZE = 64
    BACK_BUTTON_POSITION = (40, 580)
    FORWARD_BUTTON_POSITION = (180, 580)
    # DESCRIPTION TEXT
    DESCRIPTION_TEXT_SIZE = 22
    DESCRIPTION_TEXT_COLOR = (255, 255, 255)
    TEXT_0_POSITION = (70, 210)
    TEXT_1_POSITION = (212, 210)
    TEXT_2_POSITION = (70, 360)
    TEXT_3_POSITION = (212, 360)
    TEXT_4_POSITION = (70, 510)
    # Game board
    GAME_BOARD_COLOR = (56, 213, 66)
    GAME_BOARD_WIDTH = 900
    GAME_BOARD_HEIGHT = 800
    NUMBER_OF_ROWS = 5
    NUMBER_OF_COLUMNS = 5
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
        cls.BACK = pygame.image.load("assets/back.png")
        cls.FORWARD = pygame.image.load("assets/forward.png")
