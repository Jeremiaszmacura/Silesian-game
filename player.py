import time

from consts import Consts, Assets


class Player:
    def __init__(self):
        self.buildings = []
        self.gold = 2000
        self.images = Assets()
        self.images.load()
        self.save_time = time.time()

    def draw_buildings(self, window):
        for building in self.buildings:
            building.draw_building(window)

    def next_building_position(self):
        row = int((len(self.buildings)) / Consts.NUMBER_OF_ROWS)
        column = len(self.buildings) % Consts.NUMBER_OF_COLUMNS
        position = (row, column)
        return position

    def income_gold(self):
        current_time = time.time()
        if current_time - self.save_time >= 10:
            self.save_time += 10
            for building in self.buildings:
                self.gold += building.income
