import abc

from consts import Consts


class Building:
    def __init__(self, position):
        self.__position = position
        self._income = 0

    def get_position(self):
        return self.__position

    def get_income(self):
        return self._income

    def get_pixel_position(self):
        start_point_x = 350
        start_point_y = 50
        step_x = Consts.GAME_BOARD_WIDTH/Consts.NUMBER_OF_ROWS
        step_y = Consts.GAME_BOARD_HEIGHT/Consts.NUMBER_OF_COLUMNS
        pixel_position = (self.__position[0] * step_x + start_point_x, self.__position[1] * step_y + start_point_y)
        return pixel_position

    @abc.abstractmethod
    def draw_building(self, window):
        pass
