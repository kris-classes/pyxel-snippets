"""
Registering mouse clicks and drawing buttons.
Left Mouse Button: Single "splat".
Right Mouse Button: Hold it for multi-splat.

Kris Pritchard / @krp
"""
import pyxel
import random


class Button:
    """Create a button on the screen."""
    def __init__(self, x, y, w, h, label, color):
        # Create the splat at position (x, y)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.label = label
        self.color = color

    def draw(self):
        # Draw our button
        pyxel.rect(self.x, self.y, self.w, self.h, self.color)
        pyxel.text(self.x+5, self.y+5, self.label, self.color+1)

    def check_clicked(self, mouse_x, mouse_y):
        if self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h:
            print('clicked!')
            return True
        else:
            print('not clicked!')
            return False



class App:
    def __init__(self):
        pyxel.init(256, 256, fps=60)

        # Show the mouse cursor
        pyxel.mouse(True)

        # Create the buttons.
        self.buttonA = Button(100, 100, 50, 20, 'clickme A', 2)
        self.buttonB = Button(100, 150, 50, 20, 'clickme B', 8)

        # Run the update/draw callback functions
        pyxel.run(self.update, self.draw)


    def update(self):

        # If the user left-clicked, create a splat at the mouse cursor position.
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if self.buttonA.check_clicked(pyxel.mouse_x, pyxel.mouse_y):
                self.buttonA.color = (self.buttonA.color + 1) % 15
                print('Do the thing for button A')
            if self.buttonB.check_clicked(pyxel.mouse_x, pyxel.mouse_y):
                self.buttonB.color = (self.buttonB.color + 1) % 15
                print('Do the thing for button B')


    def draw(self):
        pyxel.cls(0)

        self.buttonA.draw()
        self.buttonB.draw()


if __name__ == "__main__":
    App()
