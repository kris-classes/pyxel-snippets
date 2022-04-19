"""
Same as previous example but attempts to animate the spritesheet with a for loop.

For an actual game we'd load the position of each sprite
and then control which sprite displays for a given animation.

Not every sprite in this spritesheet has the same size bounding box and I want to keep this example as simple as possible though.

Kris Pritchard / @krp
"""
import pyxel


# Using color 15 as our color key now instead.
COLORKEY_COLOR = 15
# NOTE: Pyxel has 3 image banks numbered 0-2.
MARIO_IMG_BANK = 0

class App:
    def __init__(self):
        # Initialize a 256x256 window.
        pyxel.init(256, 256)

        # NOTE: We load this into img bank 0
        pyxel.image(MARIO_IMG_BANK).load(0, 0, "assets/09_mario_spritesheet.png")

        # How big a cell is in the spritesheet.
        # We scan across the sprite sheet with a box this size.
        self.sprite_cell_width = 30 
        self.sprite_cell_height = 30

        # The current clip box position as it scans
        # through the sprite sheet.
        self.sprite_clip_x = 0
        self.sprite_clip_y = 0

        # NOTE: The mario spritesheet is 405px x 188px
        # but the small mario sprites only go 240px across.
        self.spritesheet_maxwidth = 240
        self.spritesheet_maxheight = 188

        # Run the app.
        pyxel.run(self.update, self.draw)

    def update(self):
        # Only perform these every 10 frames.
        if pyxel.frame_count % 10 == 0:
            # Reset the sprite clip positions if we go too far.
            if self.sprite_clip_x >= self.spritesheet_maxwidth:
                # Reset x to the start of the row
                self.sprite_clip_x = 0

                # NOTE: Uncomment this to see other sprites.
                # Go down a row.
                self.sprite_clip_y += self.sprite_cell_height

            if self.sprite_clip_y >= self.spritesheet_maxheight:
                self.sprite_clip_y = 0

            # Scan across the spritesheet every frame.
            # Jump the entire width of a sprite on each loop.
            self.sprite_clip_x += self.sprite_cell_width

    def draw(self):
        pyxel.cls(0)

        # blt arguments:
        # x position = 10
        # y position = 10
        # img bank (0-2) = 0 
        # u img/texture coordinate = 0
        # v img/texture coordinate = 0
        # w img/texture width = 100
        # v img/texture/height = 100


        # Show how to load sprites from a second image bank.
        pyxel.text(5, 50, f'Sprite Clip Position: ({self.sprite_clip_x}, {self.sprite_clip_y})', 7)

        # Place the sprite at (100, 100)
        pyxel.blt(100, 100, MARIO_IMG_BANK, self.sprite_clip_x, self.sprite_clip_y, self.sprite_cell_width, self.sprite_cell_height, COLORKEY_COLOR)


if __name__ == "__main__":
    App()
