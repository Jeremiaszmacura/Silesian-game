import time

import pygame

from control_panel import ControlPanel
from consts import Consts
from game_board import GameBoard
from player import Player
from sawmill import Sawmill
from gold_mint import GoldMint
from gold_mine import GoldMine
from quarry import Quarry
from woodcutters_hut import WoodcuttersHut


class Game:
    def __init__(self):
        self.running = False
        self.screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()  # frame clock
        self.control_panel = ControlPanel()
        self.game_board = GameBoard()
        self.player = Player()
        self.clock = pygame.time.Clock()
        self.start_time = time.time()

    def start_game(self):
        pygame.display.set_caption("Śląska gierka")
        self.running = True
        self.game_loop()

    def game_loop(self):
        while self.running:
            self.clock.tick(Consts.FPS)
            self.key_control()
            self.draw()
            self.player.income_gold()
            pygame.display.update()

    def draw(self):
        self.control_panel.draw(self.screen, self.player.gold)
        self.game_board.draw(self.screen)
        self.player.draw_buildings(self.screen)

    def build(self, building_type):
        if building_type == 0:
            if self.player.gold >= Consts.WOODCUTTERS_HUT_COST:
                self.player.buildings.append(WoodcuttersHut(self.player.next_building_position()))
                self.player.gold -= Consts.WOODCUTTERS_HUT_COST
            else:
                print("Ni mosz tyla piniondza!")
        elif building_type == 1:
            if self.player.gold >= Consts.QUARRY_COST:
                self.player.buildings.append(Quarry(self.player.next_building_position()))
                self.player.gold -= Consts.QUARRY_COST
            else:
                print("Ni mosz tyla piniondza!")
        elif building_type == 2:
            if self.player.gold >= Consts.SAWMILL_COST:
                self.player.buildings.append(Sawmill(self.player.next_building_position()))
                self.player.gold -= Consts.SAWMILL_COST
            else:
                print("Ni mosz tyla piniondza!")
        elif building_type == 3:
            if self.player.gold >= Consts.GOLD_MINE_COST:
                self.player.buildings.append(GoldMine(self.player.next_building_position()))
                self.player.gold -= Consts.GOLD_MINE_COST
            else:
                print("Ni mosz tyla piniondza!")
        elif building_type == 4:
            if self.player.gold >= Consts.GOLD_MINT_COST:
                self.player.buildings.append(GoldMint(self.player.next_building_position()))
                self.player.gold -= Consts.GOLD_MINT_COST
            else:
                print("Ni mosz tyla piniondza!")

    def key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                building_type = self.is_onclick(event.pos)
                if building_type in [0, 1, 2, 3, 4] and len(self.player.buildings) >= Consts.NUMBER_OF_ROWS * Consts.NUMBER_OF_COLUMNS:
                    print("Wincyj ni poradzisz chopie!!!")
                    pass
                else:
                    self.build(building_type)

    @staticmethod
    def is_onclick(mouse_position):
        if (Consts.BUILDING_0_POSITION[0] < mouse_position[0] <
                Consts.BUILDING_0_POSITION[0] + Consts.BUILDING_ICON_SIZE and
                Consts.BUILDING_0_POSITION[1] < mouse_position[1] < Consts.BUILDING_0_POSITION[
                    1] + Consts.BUILDING_ICON_SIZE):
            return 0
        elif (Consts.BUILDING_1_POSITION[0] < mouse_position[0] <
              Consts.BUILDING_1_POSITION[0] + Consts.BUILDING_ICON_SIZE and
              Consts.BUILDING_1_POSITION[1] < mouse_position[1] < Consts.BUILDING_1_POSITION[
                  1] + Consts.BUILDING_ICON_SIZE):
            return 1
        elif (Consts.BUILDING_2_POSITION[0] < mouse_position[0] <
              Consts.BUILDING_2_POSITION[0] + Consts.BUILDING_ICON_SIZE and
              Consts.BUILDING_2_POSITION[1] < mouse_position[1] < Consts.BUILDING_2_POSITION[
                  1] + Consts.BUILDING_ICON_SIZE):
            return 2
        elif (Consts.BUILDING_3_POSITION[0] < mouse_position[0] <
              Consts.BUILDING_3_POSITION[0] + Consts.BUILDING_ICON_SIZE and
              Consts.BUILDING_3_POSITION[1] < mouse_position[1] < Consts.BUILDING_3_POSITION[
                  1] + Consts.BUILDING_ICON_SIZE):
            return 3
        elif (Consts.BUILDING_4_POSITION[0] < mouse_position[0] <
              Consts.BUILDING_4_POSITION[0] + Consts.BUILDING_ICON_SIZE and
              Consts.BUILDING_4_POSITION[1] < mouse_position[1] < Consts.BUILDING_4_POSITION[
                  1] + Consts.BUILDING_ICON_SIZE):
            return 4
        else:
            return 5


def main():
    pygame.init()
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
