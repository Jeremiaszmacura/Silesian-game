import time

from consts import Consts, Assets


class Player:
    def __init__(self):
        self.__buildings = []
        self.__gold = 2000
        self.images = Assets()
        self.images.load()
        self.__start_time = time.time()
        self.__next_gold_time = 10

    class Memento:
        def __init__(self, state):
            self.__buildings = state["buildings"]
            self.__gold = state["gold"]
            self.__time_saved = state["time_saved"]
            self.__next_gold_time = state["next_gold_time"]
            self.__snapshot_time = time.time()

        def get_state(self):
            return {"buildings": self.__buildings,
                    "gold": self.__gold,
                    "time_saved": self.__time_saved,
                    "next_gold_time": self.__next_gold_time}

        def get_snapshot_time(self):
            return self.__snapshot_time

    def get_gold(self):
        return self.__gold

    def spend_gold(self, costs):
        self.__gold -= costs

    def get_buildings_length(self):
        return len(self.__buildings)

    def add_building(self, building):
        self.__buildings.append(building)

    def get_game_time(self):
        return time.time() - self.__start_time

    def draw_buildings(self, window):
        for building in self.__buildings:
            building.draw_building(window)

    def next_building_position(self):
        row = int((len(self.__buildings)) / Consts.NUMBER_OF_ROWS)
        column = len(self.__buildings) % Consts.NUMBER_OF_COLUMNS
        position = (row, column)
        return position

    def income_gold(self):
        current_time = time.time()
        if current_time - self.__start_time >= self.__next_gold_time:
            self.__next_gold_time += 10
            for building in self.__buildings:
                self.__gold += building.get_income()

    def save_snapshop(self):
        save_time = time.time() - self.__start_time
        state = {"buildings": self.__buildings[:],
                 "gold": self.__gold,
                 "time_saved": save_time,
                 "next_gold_time": self.__next_gold_time}
        snapshot = self.Memento(state)
        return snapshot

    def restore_snapshot(self, snapshot):
        state = snapshot.get_state()
        self.__buildings = state["buildings"]
        self.__gold = state["gold"]
        self.__next_gold_time = state["next_gold_time"]
        self.__start_time = time.time() - state["time_saved"]
