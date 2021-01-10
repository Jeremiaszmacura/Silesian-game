import pygame

from consts import Consts, Assets


class GameBoard:
    def __init__(self):
        self.images = Assets()

    @staticmethod
    def draw(window):
        pygame.draw.rect(window, Consts.GAME_BOARD_COLOR, (Consts.CONTROL_PANEL_WIDTH, 0,
                                                           Consts.GAME_BOARD_WIDTH,
                                                           Consts.GAME_BOARD_HEIGHT))
