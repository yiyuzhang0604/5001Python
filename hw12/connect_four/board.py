from disk import Disk

DISK_X = 0
DISK_Y = 0
DISK_COL = 12


class Board:
    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.grid = [[None] * self.col_num for _ in range(self.row_num)]
        self.disk = Disk(DISK_X, DISK_Y, DISK_COL)

    def draw_me(self):
        """ sets processing values"""
        LENGTH = 100
        STROKE_W = 13
        FILL = 500
        STROKE_C = (0, 0, 255)

        for i in range(self.col_num):
            for j in range(self.row_num):
                x = i * LENGTH
                y = j * LENGTH
                fill(FILL)
                strokeWeight(STROKE_W)
                stroke(*STROKE_C)
                rect(x, y, LENGTH, LENGTH)
