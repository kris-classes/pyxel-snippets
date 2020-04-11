"""
Display colors available in pyxel with the default palette.

This example is more verbose than necessary but is done for teaching purposes.

Kris Pritchard / @krisrp
"""
import pyxel


text_x = 80
text_y = 40

rect_x = 120
rect_y = 40
rect_width = 50
rect_height = 5

# Initialize the screen.
pyxel.init(256, 256)    

# Clear the screen with color 0 (black).
pyxel.cls(0)

# Draw a small white rectangle so that we can see black text.
pyxel.rect(rect_x-80, rect_y-3, rect_width+120, rect_height+6, 7)

# Color 0
pyxel.text(text_x, text_y, f'COLOR: 0', 0)
pyxel.rect(rect_x, rect_y, rect_width, rect_height, 0)

# Color 1
pyxel.text(text_x, text_y+10, f'COLOR: 1', 1)
pyxel.rect(rect_x, rect_y+10, rect_width, rect_height, 1)

# Color 2
pyxel.text(text_x, text_y+20, f'COLOR: 2', 2)
pyxel.rect(rect_x, rect_y+20, rect_width, rect_height, 2)

# Color 3
pyxel.text(text_x, text_y+30, f'COLOR: 3', 3)
pyxel.rect(rect_x, rect_y+30, rect_width, rect_height, 3)

# Color 4
pyxel.text(text_x, text_y+40, f'COLOR: 4', 4)
pyxel.rect(rect_x, rect_y+40, rect_width, rect_height, 4)

# Color 5
pyxel.text(text_x, text_y+50, f'COLOR: 5', 5)
pyxel.rect(rect_x, rect_y+50, rect_width, rect_height, 5)

# Color 6
pyxel.text(text_x, text_y+60, f'COLOR: 6', 6)
pyxel.rect(rect_x, rect_y+60, rect_width, rect_height, 6)

# Color 7
pyxel.text(text_x, text_y+70, f'COLOR: 7', 7)
pyxel.rect(rect_x, rect_y+70, rect_width, rect_height, 7)

# Color 8
pyxel.text(text_x, text_y+80, f'COLOR: 8', 8)
pyxel.rect(rect_x, rect_y+80, rect_width, rect_height, 8)

# Color 9
pyxel.text(text_x, text_y+90, f'COLOR: 9', 9)
pyxel.rect(rect_x, rect_y+90, rect_width, rect_height, 9)

# Color 10
pyxel.text(text_x, text_y+100, f'COLOR: 10', 10)
pyxel.rect(rect_x, rect_y+100, rect_width, rect_height, 10)

# Color 11
pyxel.text(text_x, text_y+110, f'COLOR: 11', 11)
pyxel.rect(rect_x, rect_y+110, rect_width, rect_height, 11)

# Color 12
pyxel.text(text_x, text_y+120, f'COLOR: 12', 12)
pyxel.rect(rect_x, rect_y+120, rect_width, rect_height, 12)

# Color 13
pyxel.text(text_x, text_y+130, f'COLOR: 13', 13)
pyxel.rect(rect_x, rect_y+130, rect_width, rect_height, 13)

# Color 14
pyxel.text(text_x, text_y+140, f'COLOR: 14', 14)
pyxel.rect(rect_x, rect_y+140, rect_width, rect_height, 14)

# Color 15
pyxel.text(text_x, text_y+150, f'COLOR: 15', 15)
pyxel.rect(rect_x, rect_y+150, rect_width, rect_height, 15)

# Show the screen and wait forever. Don't use it in a normal app.
pyxel.show()
