class Object:
    def __init__(self, display, x, y, image):
        self.display = display
        self.x = x
        self.y = y
        self.image = image

    def draw(self, x, y):
        self.display.blit(self.image, (self.x + (self.display.get_width()/2 - 2) - x*10, self.y + (self.display.get_height()/2 - 2) - y*10))