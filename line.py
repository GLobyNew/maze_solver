class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start, end):
        self.x1 = start.x
        self.y1 = start.y
        self.x2 = end.x
        self.y2 = end.y

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2,
                           self.y2, fill=fill_color, width=2)
