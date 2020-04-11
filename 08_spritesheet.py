"""
Exactly the same as the colorkey example but using a
spritesheet now and breaking it into smaller "sprites".

Kris Pritchard / @krisrp
"""
import pyxel


# Using color 15 as our color key now instead.
COLORKEY_COLOR = 15
# NOTE: Pyxel has 3 image banks numbered 0-2.
FIRST_IMG_BANK = 0
MARIO_IMG_BANK = 1

class App:
    def __init__(self):
        pyxel.init(256, 256)

        # NOTE: We load this into img bank 0
        pyxel.image(FIRST_IMG_BANK).load(0, 0, "assets/08_spritesheet.png")

        # NOTE: We load this into img bank 1
        pyxel.image(MARIO_IMG_BANK).load(0, 0, "assets/08_mario_spritesheet.png")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        # blt arguments:
        # x position = 10
        # y position = 10
        # img bank (0-2) = 0 
        # u img/texture coordinate = 0
        # v img/texture coordinate = 0
        # w img/texture width = 100
        # v img/texture/height = 100

        pyxel.text(5, 5, 'The full sprite sheet in img bank 0:', 7)
        pyxel.blt(10, 12, FIRST_IMG_BANK, 0, 0, 240, 240, COLORKEY_COLOR)

        # NOTE: It helps when creating your spritesheet
        # to position each sprite an equal distance apart.

        # Number 1, got through trial and error.
        pyxel.blt(100, 12, FIRST_IMG_BANK, 0, 0, 10, 10, COLORKEY_COLOR)

        # Number 2, got through trial and error.
        pyxel.blt(125, 12, FIRST_IMG_BANK, 10, 0, 10, 10, COLORKEY_COLOR)

        # Numbers 3-5, got through trial and error.
        pyxel.blt(145, 12, FIRST_IMG_BANK, 20, 0, 30, 10, COLORKEY_COLOR)

        # Numbers 1-3, loaded backwards with negative u/v.
        pyxel.blt(185, 12, FIRST_IMG_BANK, 0, 0, -30, 10, COLORKEY_COLOR)

        # Show how to load sprites from a second image bank.
        pyxel.text(5, 50, 'The full sprite sheet in img bank 1:', 7)
        pyxel.blt(5, 62, MARIO_IMG_BANK, 0, 0, 240, 240, COLORKEY_COLOR)


if __name__ == "__main__":
    App()
