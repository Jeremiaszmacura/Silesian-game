class Caretaker:
    def __init__(self, player):
        self.__history = []
        self.player = player
        self.__iterator = 0
        self.store_snapshot()

    def store_snapshot(self):
        del self.__history[self.__iterator:]
        self.__iterator += 1
        self.__history.append(self.player.save_snapshop())

    def undo(self):
        if len(self.__history):
            self.player.restore_snapshot(self.__history[self.__iterator - 1])
            self.__iterator -= 1
        else:
            print("No more saves back!")

    def redo(self):
        if len(self.__history) >= self.__iterator + 2:
            self.player.restore_snapshot(self.__history[self.__iterator + 1])
            self.__iterator += 1
        else:
            print("No more saves forward!")
