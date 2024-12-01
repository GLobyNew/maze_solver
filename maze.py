from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__cells = []
        self.__win = win

    def _create_cells(self):
        x_cur_pos = self.x1
        y_cur_pos = self.y1
        for i in range(self.num_cols):
            x_cur_pos = self.x1
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(
                    x_cur_pos, y_cur_pos, x_cur_pos+self.cell_size_x, y_cur_pos+self.cell_size_y, self.__win))
                x_cur_pos += self.cell_size_x
            y_cur_pos += self.cell_size_y


