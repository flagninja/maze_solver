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
            win
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
                self._cells[x][y].draw()
                self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(.05)