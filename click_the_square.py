import pyxel
import random


class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        self.color = 1
        self.square_size = 8
        self.x_direction = 1
        pyxel.mouse(True)
        self.won = False
        self.dx = random.randint(1, 4)
        self.dy = random.randint(1, 4)
        self.wins = 0
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.won = False
        self.x = 0
        self.y = 0
        self.color = 1

    def update(self):
        self.x = self.x + self.dx * self.x_direction  #% pyxel.width
        if self.x + self.square_size > pyxel.width:
            self.x_direction = -1
        elif self.x < 0:
            self.x_direction = 1
        self.y = (self.y + self.dy) % pyxel.height
        if pyxel.frame_count % 30 == 0:
            self.color = (self.color + 1) % 15
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.x_direction = self.x_direction * -1
        # print(pyxel.mouse_x, pyxel.mouse_y)
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y
            if self.x <= mouse_x <= self.x + self.square_size \
                    and self.y <= mouse_y <= self.y + self.square_size:
                self.won = True
                self.wins += 1
        if pyxel.btnp(pyxel.KEY_R):
            self.reset()
        if pyxel.frame_count % random.randint(40, 120):
            self.dx = random.randint(1, 4)
            self.dy = random.randint(1, 4)
            self.square_size = random.randint(5, 15)
            # self.x_direction = self.x_direction * -1

    def draw(self):
        if self.won:
            pyxel.cls(0)
            pyxel.text(100, 100, 'you won!', 11)
        else:
            pyxel.cls(0)
            pyxel.rect(self.x, self.y, self.square_size, self.square_size, self.color)
        pyxel.text(pyxel.width - 50, 10, f'score: {self.wins}', 11)

App()