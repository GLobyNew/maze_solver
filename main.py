from window import Window
from line import Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    test_cell = Cell(100, 100, 200, 200, win)
    test_cell2 = Cell(300, 320, 550, 600, win)
    test_cell.draw()
    test_cell2.draw()
    win.wait_for_close()


if __name__ == "__main__":
    main()