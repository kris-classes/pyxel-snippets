"""
Display a simple text message.

Kris Pritchard / @krisrp
"""
import pyxel


# Initialize a window of width 160 x height 120
pyxel.init(160, 120)

# Clear the screen with color 0 (black)
pyxel.cls(0)

# Display some text
text_x = 60
text_y = 60
pyxel.text(text_x, text_y, "Hello World!", 8)  # Use color 8 (pink)

# Show the window and wait forever. Don't use show() in normal apps because it only updates once.
pyxel.show()
