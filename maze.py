from graphics import *
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        

    def _create_cells(self):
        for x in range(self.num_cols):
            self._cells.append([])
            for y in range(self.num_rows):
                self._cells[x].append(
                    Cell(
                        Point(
                            self.x1+(x*self.cell_size_x),
                            self.y1+(y*self.cell_size_y)
                            ),
                        Point(
                            self.x1+((x+1)*self.cell_size_x),
                            self.y1+((y+1)*self.cell_size_y)
                            ),
                        self.win
                        )
                    )
        try:
            for x in self._cells:
                for y in x:
                    y.draw()
                    self._animate()
        except Exception as e:
            print(e)
        self._break_entrance_and_exit()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left = False
        self._cells[-1][-1].has_right = False
        try:
            self._cells[0][0].draw()
            self._cells[-1][-1].draw()
        except Exception as e:
            print(e)