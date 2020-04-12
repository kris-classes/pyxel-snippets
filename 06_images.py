"""
Load an image.

Kris Pritchard / @krisrp
"""
import pyxel


class App:
    def __init__(self):
        pyxel.init(256, 256)

        pyxel.image(0).load(0, 0, "assets/06_never.png")

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        # blt arguments:
        # x position = 0
        # y position = 0
        # img bank (0-2) = 0 
        # u img/texture coordinate = 0
        # v img/texture coordinate = 0
        # w img/texture width = 100
        # v img/texture/height = 100
        pyxel.blt(0, 0, 0, 0, 0, 200, 200)

        pyxel.text(40, 220, 'Never Gonna Give You Up!', 7)



if __name__ == "__main__":
    App()
