from game_controller import GameController
from board import Board


SPACE = {'w': 720, 'h':740 }
ROW_NUM = 6
COL_NUM = 7
gc = GameController(ROW_NUM, COL_NUM)


def setup():
    size(SPACE['w'],SPACE['h'])
    gc.setup()


def draw():
    BACKGROUND = -1
    X = 10
    Y = 130
    TRANSLATE = (X, Y)
    background(BACKGROUND)
    translate(*TRANSLATE)
    gc.update()
    
