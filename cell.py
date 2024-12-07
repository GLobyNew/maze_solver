from line import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
        self.visited = False

    def draw(self, fill_color="Red"):
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1),
                             Point(self._x1, self._y2))
            self._win.draw_line(left_wall, fill_color)
        else:
            left_wall = Line(Point(self._x1, self._y1),
                             Point(self._x1, self._y2))
            self._win.draw_line(left_wall, "#323232")
        if self.has_right_wall:
            right_wall = Line(Point(self._x2, self._y1),
                              Point(self._x2, self._y2))
            self._win.draw_line(right_wall, fill_color)
        else:
            right_wall = Line(Point(self._x2, self._y1),
                              Point(self._x2, self._y2))
            self._win.draw_line(right_wall, "#323232")
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1),
                            Point(self._x2, self._y1))
            self._win.draw_line(top_wall, fill_color)
        else:
            top_wall = Line(Point(self._x1, self._y1),
                            Point(self._x2, self._y1))
            self._win.draw_line(top_wall, "#323232")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2),
                               Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, fill_color)
        else:
            bottom_wall = Line(Point(self._x1, self._y2),
                               Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall, "#323232")

    def draw_move(self, to_cell, undo=False):
        fill_color = "Red" if undo == False else "Gray"
        xCenter_1 = (self._x1 + self._x2) / 2
        yCenter_1 = (self._y1 + self._y2) / 2
        xCenter_2 = (to_cell._x1 + to_cell._x2) / 2
        yCenter_2 = (to_cell._y1 + to_cell._y2) / 2
        line_CtoC = Line(Point(xCenter_1, yCenter_1),
                         Point(xCenter_2, yCenter_2))
        self._win.draw_line(line_CtoC, fill_color)

    