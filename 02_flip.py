"""
We need to use flip() if we want to update the screen.

This is useful if you're just playing around and want to
update the screen manually while you experiment.

Better is to use functions (see next example).

Kris Pritchard / @krisrp
"""
import pyxel
import time


# Initialize a new window
pyxel.init(160, 120)

# Clear the screen with color 0 (black)
pyxel.cls(0)

for i in range(100):
    # Clear the screen with color i modulo 16.
    pyxel.cls(i % 16)  # Modulo keeps i bound within 0 and 15.

    # Add some text
    pyxel.text(10, 40, f'Hello World! i = {i} and i % 16 = {i % 16}', (i + 1) % 16)

    # Update the screen
    pyxel.flip()
    time.sleep(1)
