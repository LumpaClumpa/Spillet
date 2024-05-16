class Object:
    def __init__(self, screenWidth, screenHeight, display, x, y, image):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.display = display
        self.x = x
        self.y = y
        self.image = image

    def draw(self, x, y):
        self.display.blit(self.image, (self.x + (self.screenWidth/2 - 25) - x, self.y + (self.screenHeight/2 - 25) - y))