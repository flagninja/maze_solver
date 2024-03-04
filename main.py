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

def main():
    win = Window(800, 600)
    line1 = Line(Point(20,20),Point(50,50))
    line2 = Line(Point(100,100),Point(30,100))
    win.draw_line(line1, "red")
    win.draw_line(line2, "green")
    win.wait_for_close()

main()