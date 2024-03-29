from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__can = Canvas(self.__root, bg = "white", width=width, height=height)
        self.__can.pack(fill = BOTH, expand = 1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed")
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__can, fill_color)

class Point:
    def __init__(self, x, y):
        # 0,0 is the top left of the screen
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2)
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, p1, p2, win=None):
        # p1 is top left, p2 is bottom right
        self.has_left = True
        self.has_right = True
        self.has_top = True
        self.has_bot = True
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.__win = win
        self.visited=False

    def draw(self):
        if self.has_left:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2)),fill_color="white")
        if self.has_right:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2)),fill_color="white")
        if self.has_top:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1)),fill_color="white")
        if self.has_bot:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)))
        else:
            self.__win.draw_line(Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2)),fill_color="white")

    def get_center(self):
        return Point((self.__x1+self.__x2)//2,(self.__y1+self.__y2)//2)

    def draw_move(self, to_cell, undo=False):
        start = self.get_center()
        end = to_cell.get_center()
        if undo:
            self.__win.draw_line(Line(start,end), "gray")
        else:
            self.__win.draw_line(Line(start,end), "red")