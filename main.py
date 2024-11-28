from window import Window
from line import Line, Point

def main():
    win = Window(800, 600)
    test_line = Line(Point(100, 100), Point(200, 200))
    test_line2 = Line(Point(100, 200), Point(150, 75))
    win.draw_line(test_line, "Black")
    win.draw_line(test_line2, "Red")
    win.wait_for_close()


if __name__ == "__main__":
    main()