import pygame

from consts import Consts, Assets


class GameBoard:
    def __init__(self):
        self.images = Assets()

    def draw(self, window):
        pygame.draw.rect(window, Consts.GAME_BOARD_COLOR, (Consts.CONTROL_PANEL_WIDTH, 0,
                                                           Consts.GAME_BOARD_WIDTH,
                                                           Consts.GAME_BOARD_HEIGHT))
