"""
Demonstrate passing the update and draw callback functions into pyxel.run().

The downside to show() is that it doesn't allow us to redraw the app because it waits forever.
We can use functions instead.

If you need to store a lot of state, better than using
global variables is to use classes instead.
See the next example.

Kris Pritchard / @krisrp
"""
import pyxel

# Initialize the screen.
pyxel.init(160, 120)    

# Set the default color
color = 0

# Define a function that updates in-game logic.
def update():
    global color  # globals are bad practice but are ok for this example.
    if pyxel.btnp(pyxel.KEY_R):
        color += 1

# Define a function responsible for drawing.
def draw():
    global color  # globals are bad practice but are ok for this example.
    pyxel.cls(color % 16)
    pyxel.text(40, 20, f'Frame Count: {pyxel.frame_count}', (color + 1) % 16)
    pyxel.text(40, 30, f'Frame Count % 30: {pyxel.frame_count % 30}', (color + 1) % 16)
    pyxel.text(40, 60, 'Press R to change color', (color + 1) % 16)
    pyxel.text(40, 70, f'Background Color: {color}', (color % 16))
    pyxel.text(40, 80, f'Text Color: {(color + 1) % 16}', (color + 1) % 16)
    print(f'color: {color}')


# Pass in the functions as arguments (callbacks).
pyxel.run(update, draw)
