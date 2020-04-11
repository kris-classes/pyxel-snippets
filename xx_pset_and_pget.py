"""
pset sets a pixel color. pget gets a pixel color.

Kris Pritchard / @krisrp
"""
import pyxel


class App:
    def __init__(self):
        # Initialize the screen.
        pyxel.init(256, 256)

        # Clear the screen
        pyxel.cls(0)

        # Enable the mouse
        pyxel.mouse(True)

        # Run the app.
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        mouse_x = pyxel.mouse_x
        mouse_y = pyxel.mouse_y

        # Loop through the pixels, setting them different colors.
        pyxel.cls(0)

        # NOTE: This seems to be really slow. Probably best not to use pset()
        for i in range(256):
            for j in range(256):
                pyxel.pset(i, j, i % 16)

        # Draw a black rectangle
        pyxel.rect(60, 74, 150, 30, 0)

        # Draw text of mouse position
        pyxel.text(80, 80, f'Mouse Position: ({mouse_x}, {mouse_y})', 7)
        pyxel.text(80, 90, f'Pixel Color: {pyxel.pget(mouse_x, mouse_y)}', 7)


App()
