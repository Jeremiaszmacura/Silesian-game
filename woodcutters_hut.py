from building import Building
from consts import Assets


class WoodcuttersHut(Building):
    def __init__(self, position):
        super().__init__(position)
        self.images = Assets()
        self.income = 300

    def draw_building(self, window):
        window.blit(self.images.WOODCUTTERS, self.get_pixel_position())
