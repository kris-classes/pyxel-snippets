"""
Instead of using functions and global variables, let's store state using classes.

Kris Pritchard / @krp
"""
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.cls(0)

        self.text_x = 10
        self.text_y = 20
        # Give run the update/draw callbacks
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_W):
            self.text_y -= 1
        if pyxel.btnp(pyxel.KEY_S):
            self.text_y += 1
        if pyxel.btnp(pyxel.KEY_A):
            self.text_x -= 1
        if pyxel.btnp(pyxel.KEY_D):
            self.text_x += 1

    def draw(self):
        # Don't forget to clear screen on every frame!
        pyxel.cls(0)

        # Draw the text at position: (text_x, text_y)
        pyxel.text(self.text_x, self.text_y, "Press W, A, S, D to move this text!", 9)



if __name__ == "__main__":
    App()
