"""
Connecting points with lines

Kris Pritchard / @krisrp
"""
import pyxel


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class App:
    def __init__(self):
        pyxel.init(256, 256)

        pyxel.mouse(True)

        self.points = []

        pyxel.run(self.update, self.draw)


    def update(self):
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.points.append(Point(pyxel.mouse_x, pyxel.mouse_y))

    def draw_points(self):
        for point in self.points:
            pyxel.circ(point.x, point.y, 2, 2)
        
    def draw_lines(self):
        for i in range(len(self.points) - 1):
            x1 = self.points[i].x
            y1 = self.points[i].y
            x2 = self.points[i+1].x
            y2 = self.points[i+1].y
            pyxel.line(x1, y1, x2, y2, 8)

    def draw(self):
        pyxel.cls(0)

        self.draw_points()
        self.draw_lines()


if __name__ == "__main__":
    App()
