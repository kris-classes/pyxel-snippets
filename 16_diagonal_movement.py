"""
Small snippet demonstrating diagonal pixel movement for Seubmarine on Discord.

Kris Pritchard / @krisrp
"""
import math
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.cls(0)

        self.x = 60
        self.y = 60
        # Give run the update/draw callbacks
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1
        if pyxel.btn(pyxel.KEY_S):
            self.y += 1
        if pyxel.btn(pyxel.KEY_A):
            self.x -= 1
        if pyxel.btn(pyxel.KEY_D):
            self.x += 1
        if pyxel.btn(pyxel.KEY_Q):
            self.x -= 1
            self.y -= 1
        if pyxel.btn(pyxel.KEY_E):
            self.x += 1
            self.y -= 1
        if pyxel.btn(pyxel.KEY_Z):
            self.x -= 1
            self.y += 1
        if pyxel.btn(pyxel.KEY_C):
            self.x += 1
            self.y += 1

    def draw(self):
        # Don't forget to clear screen on every frame!
        pyxel.cls(0)

        # Draw the pyxel location:
        pyxel.text(5, 5, f'({self.x}, {self.y})', 7)

        # Draw the text at position: (text_x, text_y)
        pyxel.pset(self.x, self.y, 8)



if __name__ == "__main__":
    App()
