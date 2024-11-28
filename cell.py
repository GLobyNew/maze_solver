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

    def draw(self):
        if self.has_left_wall:
            left_wall = Line(Point(self.__x1, self.__y1),
                             Point(self.__x1, self.__y2))
            self.__win.draw_line(left_wall, "Red")
        if self.has_right_wall:
            right_wall = Line(Point(self.__x2, self.__y1),
                              Point(self.__x2, self.__y2))
            self.__win.draw_line(right_wall, "Red")
        if self.has_top_wall:
            top_wall = Line(Point(self.__x1, self.__y1),
                            Point(self.__x2, self.__y1))
            self.__win.draw_line(top_wall, "Red")
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self.__x1, self.__y2),
                               Point(self.__x2, self.__y2))
            self.__win.draw_line(bottom_wall, "Red")
