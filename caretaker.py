

class Caretaker:
    def __init__(self, player):
        self._history = []
        self.player = player
        self._iterator = 0
        self.store_snapshot()

    def store_snapshot(self):
        del self._history[self._iterator:]
        self._iterator += 1
        self._history.append(self.player.save_snapshop())

    def undo(self):
        if len(self._history):
            self.player.restore_snapshot(self._history[self._iterator - 1])
            self._iterator -= 1
        else:
            print("Ni mo zapisów")

    def redo(self):
        if len(self._history) >= self._iterator + 2:
            self.player.restore_snapshot(self._history[self._iterator + 1])
            self._iterator += 1
        else:
            print("Ni do sie wincyj wczytoć!")
