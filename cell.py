from line import Line, Point


class Cell:
    def __init__(self, x1, y1, x2, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__win = window

    def draw(self, fill_color="Red"):
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1),
                             Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, fill_color)
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1),
                              Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall, fill_color)
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1),
                            Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall, fill_color)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2),
                               Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall, fill_color)

    def draw_move(self, to_cell, undo=False):
        fill_color = "Red" if undo == False else "Gray"
        xCenter_1 = (self.__x1 + self.__x2) / 2
        yCenter_1 = (self.__y1 + self.__y2) / 2
        xCenter_2 = (to_cell.__x1 + to_cell.__x2) / 2
        yCenter_2 = (to_cell.__y1 + to_cell.__y2) / 2
        line_CtoC = Line(Point(xCenter_1, yCenter_1),
                         Point(xCenter_2, yCenter_2))
        self.__win.draw_line(line_CtoC, fill_color)
