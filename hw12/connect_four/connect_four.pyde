from game_controller import GameController
from board import Board


SPACE = {'w': 720, 'h':740 }
ROW_NUM = 6
COL_NUM = 7
gc = GameController(ROW_NUM, COL_NUM)


def setup():
    size(SPACE['w'],SPACE['h'])
    


def draw():
    BACKGROUND = -1
    TRANSLATE = (10,130)
    background(BACKGROUND)
    translate(*TRANSLATE)
    gc.update()
