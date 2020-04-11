"""
Registering mouse clicks and drawing objects.
Left Mouse Button: Single "splat".
Right Mouse Button: Hold it for multi-splat.

Kris Pritchard / @krisrp
"""
import pyxel
import random


class Splat:
    """Create a splat on the screen."""
    def __init__(self, x, y, color):
        # Create the splat at position (x, y)
        self.x = x
        self.y = y

        # Give the splat a random radius
        self.radius = random.randint(1, 10)
        self.color = color

    def draw(self):
        # Draw our splat
        pyxel.circ(self.x, self.y, self.radius, self.color)

        # Slowly decrease our radius every 30 frames.
        if pyxel.frame_count % 30 == 0 and self.radius > 0:
            self.radius -= 1


class Crosshair:
    """Draws a crosshair at the mouse position."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = 11

    def update(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        # East line
        pyxel.line(self.x + 5, self.y, self.x + 10, self.y, self.color)

        # West line
        pyxel.line(self.x - 5, self.y, self.x - 10, self.y, self.color)

        # North line
        pyxel.line(self.x, self.y - 5, self.x, self.y - 10, self.color)

        # South line
        pyxel.line(self.x, self.y + 5, self.x, self.y + 10, self.color)


class App:
    def __init__(self):
        pyxel.init(256, 256, fps=60)

        # Hide the mouse cursor
        pyxel.mouse(False)

        # Create a list of "splats"
        self.splats = []

        # Create the crosshair.
        self.crosshair = Crosshair()

        # Run the update/draw callback functions
        pyxel.run(self.update, self.draw)


    def update(self):
        # Update the crosshair position
        self.crosshair.update(pyxel.mouse_x, pyxel.mouse_y)

        # Create a copy of our splat list but remove any small splats.
        self.splats = [splat for splat in self.splats if splat.radius >= 1]

        # If the user left-clicked, create a splat at the mouse cursor position.
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
            self.splats.append(Splat(pyxel.mouse_x, pyxel.mouse_y, 8))

        # If the user right-clicked, create a bunch of splats at the mouse cursor position.
        if pyxel.btn(pyxel.MOUSE_RIGHT_BUTTON):
            self.splats.append(Splat(pyxel.mouse_x, pyxel.mouse_y, 6))


    def draw(self):
        pyxel.cls(0)

        # Draw the crosshair
        self.crosshair.draw()

        # Display our splats.
        for splat in self.splats:
            splat.draw()

        # Display the help text.
        pyxel.text(40, 120, f'Try both left click and hold right mouse button.', 7)



if __name__ == "__main__":
    App()
