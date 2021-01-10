from building import Building
from consts import Assets


class GoldMine(Building):
    def __init__(self, position):
        super().__init__(position)
        self.images = Assets()
        self._income = 100

    def draw_building(self, window):
        window.blit(self.images.GOLD_MINE, self.get_pixel_position())
