import pygame

from consts import Consts, Assets


class ControlPanel:
    def __init__(self, player):
        self.player = player
        self.images = Assets()
        self.__panel_x = 0
        self.__panel_y = 0

    def draw(self, window, gold):
        self.images.load()
        pygame.display.set_icon(self.images.TREASURE)
        self.__draw_panel(window)
        self.__draw_amount_of_gold(window, gold)
        self.__draw_buttons(window)
        self.__draw_description(window)
        self.__show_time(window)

    def __draw_panel(self, window):
        pygame.draw.rect(window, Consts.CONTROL_PANEL_COLOR, (self.__panel_x, self.__panel_y,
                                                              Consts.CONTROL_PANEL_WIDTH,
                                                              Consts.CONTROL_PANEL_HEIGHT))
        window.blit(self.images.CONTROL_PANEL_BACKGROUND, (0, 0))

    @staticmethod
    def __draw_amount_of_gold(window, gold):
        font = pygame.font.SysFont(Consts.FONT, Consts.GOLD_TEXT_SIZE)
        label = font.render("Gold: {}".format(gold), True, Consts.GOLD_TEXT_COLOR)
        text_rect = label.get_rect(center=(Consts.CONTROL_PANEL_WIDTH / 2, Consts.GOLD_TEXT_MARGIN_TOP))
        window.blit(label, text_rect)

    def __draw_buttons(self, window):
        window.blit(self.images.WOODCUTTERS, Consts.PANEL_BUILDING_0_POSITION)
        window.blit(self.images.QUARRY, Consts.PANEL_BUILDING_1_POSITION)
        window.blit(self.images.SAWMILL, Consts.PANEL_BUILDING_2_POSITION)
        window.blit(self.images.GOLD_MINE, Consts.PANEL_BUILDING_3_POSITION)
        window.blit(self.images.GOLD_MINT, Consts.PANEL_BUILDING_4_POSITION)
        window.blit(self.images.BACK, Consts.BACK_BUTTON_POSITION)
        window.blit(self.images.FORWARD, Consts.FORWARD_BUTTON_POSITION)

    def __show_time(self, window):
        time_font = pygame.font.SysFont('inkfree', Consts.TIME_TEXT_SIZE)
        time_text = time_font.render('Timer: {}'.format(int(self.player.get_game_time())), True,
                                     Consts.DESCRIPTION_TEXT_COLOR)
        time_text_rect = time_text.get_rect()
        time_text_rect.center = Consts.TIME_TEXT_POSITION
        window.blit(time_text, time_text_rect)

    @staticmethod
    def __draw_description(window):
        description_font = pygame.font.SysFont(Consts.FONT, Consts.DESCRIPTION_TEXT_SIZE)

        text_0 = description_font.render('Wood cutter', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_0_rect = text_0.get_rect()
        text_0_rect.center = Consts.TEXT_0_POSITION
        window.blit(text_0, text_0_rect)

        text_1 = description_font.render('Quarry', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_1_rect = text_1.get_rect()
        text_1_rect.center = Consts.TEXT_1_POSITION
        window.blit(text_1, text_1_rect)

        text_2 = description_font.render('Sawmill', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_2_rect = text_2.get_rect()
        text_2_rect.center = Consts.TEXT_2_POSITION
        window.blit(text_2, text_2_rect)

        text_3 = description_font.render('Gold Mine', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_3_rect = text_3.get_rect()
        text_3_rect.center = Consts.TEXT_3_POSITION
        window.blit(text_3, text_3_rect)

        text_4 = description_font.render('Gold Mint', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_4_rect = text_4.get_rect()
        text_4_rect.center = Consts.TEXT_4_POSITION
        window.blit(text_4, text_4_rect)
