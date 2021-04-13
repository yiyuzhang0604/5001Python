from game_controller import GameController
from board import Board


SPACE = {'w': 220, 'h': 320}
ROW_NUM = 2
COL_NUM = 2
gc = GameController(ROW_NUM, COL_NUM)


def setup():
    size(SPACE['w'],SPACE['h'])
    


def draw():
    BACKGROUND = -1
    TRANSLATE = (10,100)
    background(BACKGROUND)
    translate(*TRANSLATE)
    gc.update()

    
                
    



    
    
        
                
