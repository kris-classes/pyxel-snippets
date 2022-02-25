"""
Demonstrates how to use random numbers and datetimes to add an element of randomness to a game.

Kris Pritchard / @krisrp
"""
from datetime import datetime, timedelta
import pyxel
import random


MAX_BUBBLE_SIZE = 150


class Bubble:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1
        self.created = datetime.now()
        # Generate a random velocity for increasing in size
        self.dr = random.randint(1, 3)
        self.color = random.choice([2, 3, 6, 8, 9, 10, 11])

    def update(self):
        # Update the bubble size every 5 frames
        if pyxel.frame_count % 3 == 0 and self.radius <= MAX_BUBBLE_SIZE:
            self.radius += self.dr

    def draw(self):
        # Draw the bubble
        pyxel.circb(self.x, self.y, self.radius, self.color)


class App:
    def __init__(self):
        # Initialize a 256x256 window
        pyxel.init(256, 256)

        pyxel.mouse(True)
        # Create a list to store our bubbles
        self.bubbles = []

        # Run our callbacks
        pyxel.run(self.update, self.draw)

    def update(self):
        # Choose a random timedelta between 5 and 15 seconds.
        random_timedelta = timedelta(seconds=random.randint(8, 20))

        # Remove any bubbles older than random_duration seconds.
        self.bubbles = [bubble for bubble in self.bubbles if bubble.radius <= MAX_BUBBLE_SIZE and bubble.created < datetime.now() + random_timedelta]

        # Add a new bubble where the mouse was clicked
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bubbles.append(Bubble(pyxel.mouse_x, pyxel.mouse_y))

        # Increase the size of each bubble
        for bubble in self.bubbles:
            bubble.update()
        

    def draw(self):
        # Clear the screen with color 0 (black)
        pyxel.cls(0)

        # Draw the bubbles
        for bubble in self.bubbles:
            bubble.draw()
    
        # Tell the user how to use the app
        pyxel.text(120, 120, 'Click', 7)


if __name__ == "__main__":
    App()
