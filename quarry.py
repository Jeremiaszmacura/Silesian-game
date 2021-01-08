from building import Building
from consts import Assets


class Quarry(Building):
    def __init__(self, position):
        super().__init__(position)
        self.images = Assets()
        self.income = 200

    def draw_building(self, window):
        window.blit(self.images.QUARRY, self.get_pixel_position())
