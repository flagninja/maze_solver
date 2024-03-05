import unittest
import random
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_cells_rand(self):
        num_cols = random.randint(2,50)
        num_rows = random.randint(2,50)
        m1 = Maze(0,0,num_rows,num_cols, 10,10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[random.randint(0,num_cols-1)]),
            num_rows
        )

    def test_entrance_exit(self):
        num_cols = random.randint(2,50)
        num_rows = random.randint(2,50)
        m1 = Maze(0,0,num_rows,num_cols, 10,10)
        self.assertFalse(m1._cells[0][0].has_left)
        self.assertFalse(m1._cells[-1][-1].has_right)

    def test_cell_reset(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0,0,num_rows,num_cols,10,10)
        for column in m1._cells:
            for cell in column:
                self.assertFalse(cell.visited)

random.seed()
if __name__=="__main__":
    unittest.main()