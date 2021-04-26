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


def test_computer_make_move():
    next_x = random.randint(0, gc.ROW_NUM-1)
    next_y = random.randint(0, gc.COL_NUM-1)
    if gc.check_over() is False:
        while gc.board.grid[next_y][next_x] is not None:
            next_x = random.randint(0, gc.ROW_NUM-1)
            next_y = random.randint(0, gc.COL_NUM-1)
        assert gc.board.grid[next_x][next_y] is None

    Y = -45
    COL = 203
    d = Disk(gc.X_COORDINATES[next_x], Y, COL)
    assert d.x == gc.X_COORDINATES[next_x]
    assert d.y == Y
    assert d.col == COL
    assert gc.is_player_turn is True


def test_player_make_move():
    assert gc.check_over() is False
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


def test_check_row_win():
    gc.board.grid = [[None, None, 1, 1, 1, 1, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, 2, 2, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]
    gc.check_row_win()
    assert gc.player1_win is True

    gc.board.grid = [[None, None, None, 2, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, 1, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, 1, 2, 2, None],
                     [None, None, None, 1, 1, 1, None]]
    gc.check_row_win()
    assert gc.player2_win is False


def test_check_column_win():
    gc.board.grid = [[None, None, 1, 1, 1, None, None],
                     [1, None, None, None, None, None, None],
                     [1, None, None, None, None, None, None],
                     [1, 2, 2, None, None, None, None],
                     [1, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]
    gc.check_column_win()
    assert gc.player1_win is True

    gc.board.grid = [[None, None, None, 2, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, 1, 2, None, None, None, None],
                     [None, None, 2, None, None, None, None],
                     [None, None, 2, 1, 2, 2, None],
                     [None, None, 2, 1, 1, 1, None]]
    gc.check_column_win()
    assert gc.player2_win is True


def test_check_diagional_win():
    gc.board.grid = [[None, None, 1, 1, 1, None, None],
                     [None, None, None, 1, None, None, None],
                     [1, None, 1, None, None, None, None],
                     [1, 1, 2, None, None, None, None],
                     [1, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]
    gc.check_diagional_win()
    assert gc.player1_win is True

    gc.board.grid = [[None, None, None, 2, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, 1, 2, None, None, 2, None],
                     [None, None, 2, None, 2, None, None],
                     [None, None, 2, 2, 2, None, None],
                     [None, None, 2, None, 1, 1, None]]
    gc.check_diagional_win()
    assert gc.player2_win is True


def test_check_over():
    if gc.player1_win:
        assert gc.check_over() is True
    elif gc.palyer2_win:
        assert gc.check_over() is True
    else:
        assert gc.check_over() is False


def test_convert():
    pressed_x = 50
    assert gc.convert(pressed_x) == 0


def test_convert_y():
    y = 50
    assert gc.convert_y(y) == 0
