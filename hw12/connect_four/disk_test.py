from disk import Disk


def test_constructor():
    x = 50
    y = -45
    col = 0

    d = Disk(x, y, col)
    assert d.x == 50 and \
           d.y == -45 and \
           d.col == 0 and \
           d.RADIUS == 95
