"""
Load an image and make the colorkey transparent.
Useful for loading sprite sheets/textures.

Kris Pritchard / @krisrp
"""
import pyxel


# This means that pixels of color '2' from the image
# will be made transparent, and will be the same as
# the background color.
COLORKEY_COLOR = 2

class App:
    def __init__(self):
        pyxel.init(256, 256)

        pyxel.image(0).load(0, 0, "assets/07_colorkey.png")

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        # Draw some circles first
        pyxel.circ(20, 20, 80, 11)
        pyxel.circ(170, 70, 30, 10)
        # blt arguments:
        # x position = 10
        # y position = 10
        # img bank (0-2) = 0 
        # u img/texture coordinate = 0
        # v img/texture coordinate = 0
        # w img/texture width = 100
        # v img/texture/height = 100

        pyxel.blt(10, 10, 0, 0, 0, 240, 240, COLORKEY_COLOR)



if __name__ == "__main__":
    App()
