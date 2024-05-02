from Object import Object

class Player(Object):
    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, (0, 128, 255), 50, 50)