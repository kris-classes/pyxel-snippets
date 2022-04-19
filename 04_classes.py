"""
Instead of using functions and global variables, let's store state using classes.

Kris Pritchard / @krp
"""
import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120)
        pyxel.cls(0)

        # Give run the update/draw callbacks
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.text(30, 50, "Hello World from a class!", 9)



if __name__ == "__main__":
    App()
