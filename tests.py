import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells2(self):
        num_cols = 40
        num_rows = 40
        m1 = Maze(10, 5, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells3(self):
        num_cols = 600
        num_rows = 400
        m1 = Maze(59, 225, num_rows, num_cols, 50, 50)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_enter_and_exit(self):
        num_cols = 40
        num_rows = 40
        m1 = Maze(10, 5, num_rows, num_cols, 10, 10)
        self.assertFalse(
            m1._cells[0][0].has_left_wall
        )
        self.assertFalse(
            m1._cells[-1][-1].has_right_wall
        )


    

if __name__ == "__main__":
    unittest.main()