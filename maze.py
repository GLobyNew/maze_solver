from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()

    def _create_cells(self):
        x_cur_pos = self.x1
        y_cur_pos = self.y1
        for i in range(self.num_cols):
            x_cur_pos = self.x1
            self._cells.append([])
            for j in range(self.num_rows):
                self._cells[i].append(Cell(
                    x_cur_pos, y_cur_pos, x_cur_pos+self.cell_size_x,
                    y_cur_pos+self.cell_size_y, self._win))
                x_cur_pos += self.cell_size_x
            y_cur_pos += self.cell_size_y

        # Start to draw
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._calculate_cell_and_draw(i, j)

        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_right_wall = False
        self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = {}
            if i+1 < len(self._cells) and self._cells[i+1][j].visited == False:
                to_visit["down"] = (i+1, j)
            if j+1 < len(self._cells[i]) and self._cells[i][j+1].visited == False:
                to_visit["right"] = (i, j+1)
            if i-1 >= 0 and self._cells[i-1][j].visited == False:
                to_visit["up"] = (i-1, j)
            if j-1 >= 0 and self._cells[i][j-1].visited == False:
                to_visit["left"] = (i, j-1)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                direction = random.choice(list(to_visit.keys()))
                direction_x = to_visit[direction][0]
                direction_y = to_visit[direction][1]
                # print(f"Breaking {direction} wall at {self._cells[i][j]._x1} / {self._cells[i][j]._y1}")
                match direction:
                    case "up":
                        self._cells[i][j].has_top_wall = False
                        self._cells[direction_x][direction_y].has_bottom_wall = False
                    case "right":
                        self._cells[i][j].has_right_wall = False
                        self._cells[direction_x][direction_y].has_left_wall = False
                    case "down":
                        self._cells[i][j].has_down_wall = False
                        self._cells[direction_x][direction_y].has_top_wall = False
                    case "left":
                        self._cells[i][j].has_left_wall = False
                        self._cells[direction_x][direction_y].has_right_wall = False
                    case _:
                        raise Exception("No direction given")
                self._break_walls_r(direction_x, direction_y)

    def _calculate_cell_and_draw(self, i, j):
        self._cells[i][j]._x1 += self.x1
        self._cells[i][j]._y1 += self.y1
        self._cells[i][j]._x2 += self.x1
        self._cells[i][j]._y2 += self.x1
        self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate()

    def _animate(self):
        self._win.redraw()
        #sleep(0.005)
