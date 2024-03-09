from graphics import *
import time
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
        self.win = win
        if seed is not None:
            random.seed(seed)
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
        self._break_walls_r(0,0)
        self._reset_cells_visited()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left = False
        self._cells[-1][-1].has_right = False
        try:
            self._cells[0][0].draw()
            self._animate()
            self._cells[-1][-1].draw()
            self._animate()
        except Exception as e:
            print(e)

    def _break_walls_r(self,i,j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            can_visit = []
            for cell in self._get_adjacent(i,j):
                if not self._cells[cell[0]][cell[1]].visited:
                    can_visit.append(cell)
            if can_visit == []:
                try:
                    current.draw()
                    self._animate()
                except Exception as e:
                    print(e)
                return
            next_cell = random.choice(can_visit)
            if next_cell[2] == "r":
                current.has_right = False
                self._cells[next_cell[0]][next_cell[1]].has_left = False
                self._break_walls_r(next_cell[0],next_cell[1])
            elif next_cell[2] == "l":
                current.has_left = False
                self._cells[next_cell[0]][next_cell[1]].has_right = False
                self._break_walls_r(next_cell[0],next_cell[1])
            elif next_cell[2] == "u":
                current.has_top = False
                self._cells[next_cell[0]][next_cell[1]].has_bot = False
                self._break_walls_r(next_cell[0],next_cell[1])
            elif next_cell[2] == "d":
                current.has_bot = False
                self._cells[next_cell[0]][next_cell[1]].has_top = False
                self._break_walls_r(next_cell[0],next_cell[1])
            else:
                raise Exception("Next cell during maze drawing has invalid directionality")
            
    def _reset_cells_visited(self):
        for x in self._cells:
            for y in x:
                y.visited = False

    def _get_adjacent(self,i,j):
        adjacent = []
        if i == 0:
            adjacent.append((i+1,j,"r"))
        elif i == len(self._cells)-1:
            adjacent.append((i-1,j,"l"))
        else:
            adjacent.append((i+1,j,"r"))
            adjacent.append((i-1,j,"l"))
        if j == 0:
            adjacent.append((i,j+1,"d"))
        elif j == len(self._cells[i])-1:
            adjacent.append((i,j-1,"u"))
        else:
            adjacent.append((i,j+1,"d"))
            adjacent.append((i,j-1,"u"))
        return adjacent
    
    def _solver_r(self,i,j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        for cell in self._get_adjacent(i,j):
            next_cell = self._cells[cell[0]][cell[1]]
            if cell[2] == "r" and not current.has_right and not next_cell.visited:
                current.draw_move(next_cell)
                if self._solver_r(cell[0],cell[1]):
                    return True
                current.draw_move(next_cell,undo=True)
            elif cell[2] == "d" and not current.has_bot and not next_cell.visited:
                current.draw_move(next_cell)
                if self._solver_r(cell[0],cell[1]):
                    return True
                current.draw_move(next_cell,undo=True)
            elif cell[2] == "l" and not current.has_left and not next_cell.visited:
                current.draw_move(next_cell)
                if self._solver_r(cell[0],cell[1]):
                    return True
                current.draw_move(next_cell,undo=True)
            elif cell[2] == "u" and not current.has_top and not next_cell.visited:
                current.draw_move(next_cell)
                if self._solver_r(cell[0],cell[1]):
                    return True
                current.draw_move(next_cell,undo=True)
        return False