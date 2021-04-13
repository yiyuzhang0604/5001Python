class Disk:
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col
        self.RADIUS = 95

    def draw_me(self, col, pressed_x, y):
        """draw the disk"""
        FILL1 = 255
        FILL2 = 0
        fill(FILL1, col, FILL2)
        noStroke()
        ellipse(pressed_x, y, self.RADIUS, self.RADIUS)

    def display(self, disk):
        """ display the disk after dropping is finished"""
        FILL1 = 255
        FILL2 = 0
        fill(FILL1, disk.col, FILL2)
        noStroke()
        ellipse(disk.x, disk.y, self.RADIUS, self.RADIUS)
