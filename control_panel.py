import time

import pygame

from consts import Consts, Assets


class ControlPanel:
    def __init__(self):
        self.panel_color = Consts.CONTROL_PANEL_COLOR
        self.panel_width = Consts.CONTROL_PANEL_WIDTH
        self.panel_height = Consts.CONTROL_PANEL_HEIGHT
        self.panel_x = 0
        self.panel_y = 0
        self.images = Assets()
        self.time = time.time()

    def draw(self, window, gold):
        self.images.load()
        pygame.display.set_icon(self.images.TREASURE)
        self.draw_panel(window)
        self.draw_amount_of_gold(window, gold)
        self.draw_buttons(window)
        self.draw_description(window)
        self.show_time(window)

    def draw_panel(self, window):
        pygame.draw.rect(window, self.panel_color, (self.panel_x, self.panel_y,
                                                    self.panel_width,
                                                    self.panel_height))

    @staticmethod
    def draw_amount_of_gold(window, gold):
        font = pygame.font.SysFont(Consts.FONT, Consts.GOLD_TEXT_SIZE)
        label = font.render("Kotloki: {}".format(gold), True, Consts.GOLD_TEXT_COLOR)
        text_rect = label.get_rect(center=(Consts.CONTROL_PANEL_WIDTH / 2, 50))
        window.blit(label, text_rect)

    def draw_buttons(self, window):
        window.blit(self.images.WOODCUTTERS, Consts.BUILDING_0_POSITION)
        window.blit(self.images.QUARRY, Consts.BUILDING_1_POSITION)
        window.blit(self.images.SAWMILL, Consts.BUILDING_2_POSITION)
        window.blit(self.images.GOLD_MINE, Consts.BUILDING_3_POSITION)
        window.blit(self.images.GOLD_MINT, Consts.BUILDING_4_POSITION)

    def show_time(self, window):
        current_time = time.time()
        time_font = pygame.font.SysFont('inkfree', Consts.TIME_TEXT_SIZE)
        time_text = time_font.render('Zygor: {}'.format(int(current_time-self.time)), True, Consts.DESCRIPTION_TEXT_COLOR)
        time_text_rect = time_text.get_rect()
        time_text_rect.center = Consts.TIME_TEXT_POSITION
        window.blit(time_text, time_text_rect)

    @staticmethod
    def draw_description(window):
        description_font = pygame.font.SysFont('inkfree', Consts.DESCRIPTION_TEXT_SIZE)

        text_0 = description_font.render('Drwal', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_0_rect = text_0.get_rect()
        text_0_rect.center = Consts.TEXT_0_POSITION
        window.blit(text_0, text_0_rect)

        text_1 = description_font.render('Kamieniorz', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_1_rect = text_1.get_rect()
        text_1_rect.center = Consts.TEXT_1_POSITION
        window.blit(text_1, text_1_rect)

        text_2 = description_font.render('Pilorz', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_2_rect = text_2.get_rect()
        text_2_rect.center = Consts.TEXT_2_POSITION
        window.blit(text_2, text_2_rect)

        text_3 = description_font.render('Gruba Gelda', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_3_rect = text_3.get_rect()
        text_3_rect.center = Consts.TEXT_3_POSITION
        window.blit(text_3, text_3_rect)

        text_4 = description_font.render('Mennica', True, Consts.DESCRIPTION_TEXT_COLOR)
        text_4_rect = text_4.get_rect()
        text_4_rect.center = Consts.TEXT_4_POSITION
        window.blit(text_4, text_4_rect)
