from window import Window
from line import Line, Point
from cell import Cell


def main():
    win = Window(800, 600)
    test_cell = Cell(100, 100, 200, 200, win)
    test_cell2 = Cell(400, 400, 500, 500, win)
    test_cell.draw()
    test_cell2.draw()
    test_cell.draw_move(test_cell2, True)
    win.wait_for_close()


if __name__ == "__main__":
    main()
