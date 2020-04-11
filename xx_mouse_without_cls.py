"""
Demonstrates how show() behaves with a mouse cursor.

Kris Pritchard / @krisrp
"""
import pyxel
import time

# Initialize the screen.
pyxel.init(256, 256)    

# Clear the screen with color 0 (black).
pyxel.cls(0)

# Display the mouse cursor.
pyxel.mouse(True)

# Show the screen and wait forever.
pyxel.show()
