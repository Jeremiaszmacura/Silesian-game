from building import Building
from consts import Assets


class Sawmill(Building):
    def __init__(self, position):
        super().__init__(position)
        self.images = Assets()
        self.income = 500

    def draw_building(self, window):
        window.blit(self.images.SAWMILL, self.get_pixel_position())
