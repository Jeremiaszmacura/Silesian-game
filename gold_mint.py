from building import Building
from consts import Assets


class GoldMint(Building):
    def __init__(self, position):
        super().__init__(position)
        self.images = Assets()
        self._income = 3000

    def draw_building(self, window):
        window.blit(self.images.GOLD_MINT, self.get_pixel_position())
