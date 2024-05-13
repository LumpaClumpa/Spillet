from Object import Object

class Player(Object):
    def __init__(self, screen):
        super().__init__(screen, 0, 0, (0, 128, 255), 50, 50)