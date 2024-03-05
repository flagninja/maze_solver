from graphics import *
from maze import *


def main():
    win = Window(800, 600)
    testbed(win)
    win.wait_for_close()

def testbed(win):
    """ line1 = Line(Point(20,20),Point(50,50))
    line2 = Line(Point(100,100),Point(30,100))
    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    cell1 = Cell(Point(150,150),Point(160,160),win)
    cell1.draw()
    cell2 = Cell(Point(170,170),Point(180,180),win)
    cell2.has_right = False
    cell3 = Cell(Point(180,170),Point(190,180),win)
    cell3.has_left = False
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3,True)
    cell3.draw_move(cell1) """
    maze = Maze(10,10,20,20,20,20,win=win)
main()