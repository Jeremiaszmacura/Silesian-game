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
from caretaker import Caretaker


class Game:
    def __init__(self):
        self.__running = False
        self.screen = pygame.display.set_mode((Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
        self.__clock = pygame.time.Clock()  # frame clock
        self.__game_board = GameBoard()
        self.player = Player()
        self.control_panel = ControlPanel(self.player)
        self.caretaker = Caretaker(self.player)

    def start_game(self):
        pygame.display.set_caption("Silesian Game")
        self.__running = True
        self.__game_loop()

    def __game_loop(self):
        while self.__running:
            self.__clock.tick(Consts.FPS)
            self.__key_control()
            self.__draw()
            self.player.income_gold()
            pygame.display.update()

    def __draw(self):
        self.control_panel.draw(self.screen, self.player.get_gold())
        self.__game_board.draw(self.screen)
        self.player.draw_buildings(self.screen)

    def __build(self, building_type):
        if building_type == 0:
            if self.player.get_gold() >= Consts.WOODCUTTERS_HUT_COST:
                self.caretaker.store_snapshot()
                self.player.add_building(WoodcuttersHut(self.player.next_building_position()))
                self.player.spend_gold(Consts.WOODCUTTERS_HUT_COST)
            else:
                print("Dont have enough gold!")
        elif building_type == 1:
            if self.player.get_gold() >= Consts.QUARRY_COST:
                self.caretaker.store_snapshot()
                self.player.add_building(Quarry(self.player.next_building_position()))
                self.player.spend_gold(Consts.QUARRY_COST)
            else:
                print("Dont have enough gold!")
        elif building_type == 2:
            if self.player.get_gold() >= Consts.SAWMILL_COST:
                self.caretaker.store_snapshot()
                self.player.add_building(Sawmill(self.player.next_building_position()))
                self.player.spend_gold(Consts.SAWMILL_COST)
            else:
                print("Dont have enough gold!")
        elif building_type == 3:
            if self.player.get_gold() >= Consts.GOLD_MINE_COST:
                self.caretaker.store_snapshot()
                self.player.add_building(GoldMine(self.player.next_building_position()))
                self.player.spend_gold(Consts.GOLD_MINE_COST)
            else:
                print("Dont have enough gold!")
        elif building_type == 4:
            if self.player.get_gold() >= Consts.GOLD_MINT_COST:
                self.caretaker.store_snapshot()
                self.player.add_building(GoldMint(self.player.next_building_position()))
                self.player.spend_gold(Consts.GOLD_MINT_COST)
            else:
                print("Dont have enough gold!")

    def __key_control(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                building_type = self.__is_onclick(event.pos)
                if building_type in [0, 1, 2, 3, 4]:
                    if self.player.get_buildings_length() >= Consts.NUMBER_OF_ROWS * Consts.NUMBER_OF_COLUMNS:
                        print("Cant build more!")
                        continue
                    self.__build(building_type)
                elif building_type == 5:
                    self.caretaker.undo()
                elif building_type == 6:
                    self.caretaker.redo()

    @staticmethod
    def __is_onclick(mouse_position):
        if (Consts.PANEL_BUILDING_0_POSITION[0] < mouse_position[0] <
                Consts.PANEL_BUILDING_0_POSITION[0] + Consts.ICON_SIZE and
                Consts.PANEL_BUILDING_0_POSITION[1] < mouse_position[1] < Consts.PANEL_BUILDING_0_POSITION
                [1] + Consts.ICON_SIZE):
            return 0
        elif (Consts.PANEL_BUILDING_1_POSITION[0] < mouse_position[0] <
              Consts.PANEL_BUILDING_1_POSITION[0] + Consts.ICON_SIZE and
              Consts.PANEL_BUILDING_1_POSITION[1] < mouse_position[1] < Consts.PANEL_BUILDING_1_POSITION
              [1] + Consts.ICON_SIZE):
            return 1
        elif (Consts.PANEL_BUILDING_2_POSITION[0] < mouse_position[0] <
              Consts.PANEL_BUILDING_2_POSITION[0] + Consts.ICON_SIZE and
              Consts.PANEL_BUILDING_2_POSITION[1] < mouse_position[1] < Consts.PANEL_BUILDING_2_POSITION
              [1] + Consts.ICON_SIZE):
            return 2
        elif (Consts.PANEL_BUILDING_3_POSITION[0] < mouse_position[0] <
              Consts.PANEL_BUILDING_3_POSITION[0] + Consts.ICON_SIZE and
              Consts.PANEL_BUILDING_3_POSITION[1] < mouse_position[1] < Consts.PANEL_BUILDING_3_POSITION
              [1] + Consts.ICON_SIZE):
            return 3
        elif (Consts.PANEL_BUILDING_4_POSITION[0] < mouse_position[0] <
              Consts.PANEL_BUILDING_4_POSITION[0] + Consts.ICON_SIZE and
              Consts.PANEL_BUILDING_4_POSITION[1] < mouse_position[1] < Consts.PANEL_BUILDING_4_POSITION
              [1] + Consts.ICON_SIZE):
            return 4
        elif (Consts.BACK_BUTTON_POSITION[0] < mouse_position[0] <
              Consts.BACK_BUTTON_POSITION[0] + Consts.ICON_SIZE and
              Consts.BACK_BUTTON_POSITION[1] < mouse_position[1] < Consts.BACK_BUTTON_POSITION
              [1] + Consts.ICON_SIZE):
            return 5
        elif (Consts.FORWARD_BUTTON_POSITION[0] < mouse_position[0] <
              Consts.FORWARD_BUTTON_POSITION[0] + Consts.ICON_SIZE and
              Consts.FORWARD_BUTTON_POSITION[1] < mouse_position[1] < Consts.FORWARD_BUTTON_POSITION
              [1] + Consts.ICON_SIZE):
            return 6
        else:
            return 7


def main():
    pygame.init()
    game = Game()
    game.start_game()


if __name__ == "__main__":
    main()
