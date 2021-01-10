import time

from consts import Consts, Assets


class Player:
    def __init__(self):
        self._buildings = []
        self._gold = 2000
        self.images = Assets()
        self.images.load()
        self._start_time = time.time()
        self._next_gold_time = 10

    class Memento:
        def __init__(self, state):
            self._buildings = state["buildings"]
            self._gold = state["gold"]
            self._time_saved = state["time_saved"]
            self._next_gold_time = state["next_gold_time"]
            self._snapshot_time = time.time()

        def get_state(self):
            return {"buildings": self._buildings,
                    "gold": self._gold,
                    "time_saved": self._time_saved,
                    "next_gold_time": self._next_gold_time}

        def get_snapshot_time(self):
            return self._snapshot_time

    def get_gold(self):
        return self._gold

    def spend_gold(self, costs):
        self._gold -= costs

    def get_buildings_lenght(self):
        return len(self._buildings)

    def add_building(self, building):
        self._buildings.append(building)

    def get_game_time(self):
        return time.time() - self._start_time

    def draw_buildings(self, window):
        for building in self._buildings:
            building.draw_building(window)

    def next_building_position(self):
        row = int((len(self._buildings)) / Consts.NUMBER_OF_ROWS)
        column = len(self._buildings) % Consts.NUMBER_OF_COLUMNS
        position = (row, column)
        return position

    def income_gold(self):
        current_time = time.time()
        if current_time - self._start_time >= self._next_gold_time:
            self._next_gold_time += 10
            for building in self._buildings:
                self._gold += building.get_income()

    def save_snapshop(self):
        save_time = time.time() - self._start_time
        state = {"buildings": self._buildings[:],
                 "gold": self._gold,
                 "time_saved": save_time,
                 "next_gold_time": self._next_gold_time}
        snapshot = self.Memento(state)
        return snapshot

    def restore_snapshot(self, snapshot):
        state = snapshot.get_state()
        self._buildings = state["buildings"]
        self._gold = state["gold"]
        self._next_gold_time = state["next_gold_time"]
        self._start_time = time.time() - state["time_saved"]
