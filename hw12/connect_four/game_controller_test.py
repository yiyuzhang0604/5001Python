from game_controller import GameController
from board import Board
from disk import Disk
import random

ROW_NUM = 6
COL_NUM = 7
LIMIT = 550
gc = GameController(ROW_NUM, COL_NUM)


def test_constructor():
    assert gc.ROW_NUM == ROW_NUM
    assert gc.COL_NUM == COL_NUM
    assert gc.current_width == [LIMIT, LIMIT, LIMIT, LIMIT,
                                LIMIT, LIMIT, LIMIT]
    assert gc.player1_win is False
    assert gc.player2_win is False
    assert gc.X_COORDINATES == [50, 150, 250, 350, 450, 550, 650]
    assert gc.Y_COORDINATES == [50, 150, 250, 350, 450, 550]
    assert gc.time == 60
    assert gc.is_player_turn is True
    assert gc.ai_disk == []
    assert gc.players == dict()


def test_computer():
    next_x = random.randint(0, gc.COL_NUM-1)
    next_y = random.randint(0, gc.ROW_NUM-1)
    while gc.board.grid[next_y][next_x] is not None:
        next_x = random.randint(0, gc.COL_NUM-1)
        next_y = random.randint(0, gc.ROW_NUM-1)
    assert gc.board.grid[next_x][next_y] is None

    Y = -45
    COL = 203
    d = Disk(gc.X_COORDINATES[next_x], Y, COL)
    assert d.x == gc.X_COORDINATES[next_x]
    assert d.y == Y
    assert d.col == COL
    assert gc.is_player_turn is True


def test_update():
    COL1 = 0
    COL2 = 203
    TIME = 0
    col = 0

    if gc.is_player_turn:
        assert col == COL1
    else:
        assert col == COL2
        gc.time -= 1
        assert gc.time == TIME
