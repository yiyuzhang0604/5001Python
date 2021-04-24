from board import Board 


def test_constructor():
    ROW_NUM = 6
    COL_NUM = 7

    b = Board(ROW_NUM, COL_NUM)
    assert b.row_num == ROW_NUM and \
           b.col_num == COL_NUM and \
           b.grid == [[None] * b.col_num for _ in range(b.row_num)]

