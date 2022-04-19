"""
Display colors available in pyxel with the default palette.

Same as 02_colors but in a for loop and with added circles.

Kris Pritchard / @krp
"""
import pyxel


text_x = 80
text_y = 40

rect_x = 120
rect_y = 40
rect_width = 15
rect_height = 5

# Initialize the screen.
pyxel.init(256, 256)    

# Clear the screen with color 0 (black)
pyxel.cls(0)

# Draw a small white rectangle so that we can see black text.
pyxel.rect(rect_x-60, rect_y-3, rect_width+120, rect_height+6, 7)

for i in range(16):
    # Draw some text which has the color number.
    pyxel.text(text_x, text_y + 10*i, f'COLOR: {i}', i)

    # Draw a filled rectangle.
    pyxel.rect(rect_x, rect_y + 10*i, rect_width, rect_height, i)

    # Draw a rectangle outline/border.
    pyxel.rectb(rect_x + 20, rect_y + 10*i, rect_width, rect_height, i)


    # Draw a filled circle.
    pyxel.circ(text_x+83, text_y + 2 + 10*i, 3, i)

    # Draw a circle outline/border.
    pyxel.circb(text_x+83 + 10, text_y + 2 + 10*i, 3, i)


# Show the screen. show() only works once then freezes.
pyxel.show()
