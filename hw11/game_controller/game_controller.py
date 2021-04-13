from board import Board
from disk import Disk

pressed = False
coordinates = []
player1 = True
d = None
col = None
over = False


class GameController:
    def __init__(self, ROW_NUM, COL_NUM):
        self.ROW_NUM = ROW_NUM
        self.COL_NUM = COL_NUM
        self.board = Board(self.ROW_NUM, self.COL_NUM)
        self.current_width = [150, 150]
        self.COUNT = 4

    def update(self):
        """update the game every frame"""
        global pressed
        global coordinates
        global player1
        global d
        global col
        global over
        ZONE = 100

        self.board.draw_me()
        if (not over):
            # if game is not over
            if player1:
                col = 0
            else:
                col = 203
            if(mousePressed):
                if (mouseY < ZONE):
                    # only when mouseY is in this zone, show the disk
                    pressed = True
                    d = self.handle_mouse_press(mouseX, mouseY, col)
            elif (pressed):
                if(mouseY < ZONE):
                    if (d is not None):
                        self.handle_mouse_release(d)
                        if len(coordinates) % 2 == 0:
                            player1 = True
                        else:
                            player1 = False
                pressed = False
                # when mouseY is out of zone, need to reset pressed
        # display the disk after dropping is finished
        for i in range(len(coordinates)):
            co = coordinates[i]
            self.stay(co)
        self.check_over()
        self.board.draw_me()

    def check_over(self):
        """ check if the game is over"""
        if (len(coordinates) == self.COUNT):
            FILL = (200, 3, 0)
            SIZE = 28
            X = 29
            Y = -20
            fill(*FILL)
            over = True
            textSize(SIZE)
            text("Game Over", X, Y)
            print("Game Over")

    def convert(self, pressed_x):
        """ from x posistion, tell which column the disk is located"""
        ZONE1 = 50
        ZONE2 = 150
        if pressed_x == ZONE1:
            return 0
        elif pressed_x == ZONE2:
            return 1

    def handle_mouse_press(self, mouseX, mouseY, col):
        """ handle disk dropping animation"""
        ZONE = 100
        X1 = 50
        X2 = 150
        Y = -45
        if(mouseX <= ZONE):
            # initiate a disk object
            d = Disk(X1, Y, col)
        else:
            d = Disk(X2, Y, col)

        limit = self.current_width[self.convert(d.x)]
        if (limit > 0):
            d.draw_me(col, d.x, d.y)
        return d

    def handle_mouse_release(self, d):
        Y = 45
        d.y = Y
        ACC = 0.7
        UPDATE = 100
        limit = self.current_width[self.convert(d.x)]
        if (limit > 0):
            while (d.y < limit):
                d.y = d.y + ACC
                d.draw_me(col, d.x, d.y)
            coordinates.append(d)
            self.current_width[self.convert(d.x)] -= UPDATE

    def stay(self, disk):
        disk.display(disk)
