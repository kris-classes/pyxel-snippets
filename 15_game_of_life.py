"""
Tribute to John Conway (26 Dec 1937 - 11 Apr 2020).

Game of Life is a simulation with the following rules:

    Start with a grid of cells (pixels) which are either alive (on) or dead (off).
    - Any live cell with less than two live neighbours dies (from underpopulation).
    - Any live cell with two or three live neighbours lives on to the next generation.
    - Any live cell with more than 3 live neighbours dies (from overpopulation).
    - Any dead cell with exactly 3 live neighbours becomes a live cell (from reproduction).

    TLDR:
    - Any live cell with 2-3 neighbours survives.
    - Any dead cell with 3 live neighbours becomes alive.
    - Everything else dies, and dead cells stay dead.

    There are more efficient ways to code this, but I'm using pget/pset to 
    demonstrate using pyxel for cellular automata.
    There may be race conditions that I haven't had time to investigate yet, so consider this to be pre-alpha quality software.

    Kris Pritchard / @krisrp.
"""
import collections
import math
import random
import pyxel


#logging.basicConfig(level=logging.DEBUG)


DEAD = 0  # Colors to use for 'dead' cells
ALIVE = 8  # Color to use for 'alive' cells
MAX_SEED = 100000  # Max random number seed
WINDOW_WIDTH = 160
WINDOW_HEIGHT = 120

#WINDOW_WIDTH = 256  # Runs much slower at this size
#WINDOW_HEIGHT = 256


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'<Cell: ({self.x}, {self.y})>'

    def __eq__(self, other):
        """Cells are equal if their x and y position is equal."""
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.x, self.y))


# TODO: Add the ability to insert random Game of Life objects.
blinker = {Cell(1, 0), Cell(1, 1), Cell(1, 2)}


class Grid:
    """Keeps track of the grid of cells."""
    def __init__(self):
        # Create an empty set of cells.
        self.seed = random.randrange(MAX_SEED)
        self.initial_population = 0.5
        self.frame_update_delay = 15
        self.cells = set()

        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT

        self.initialize_world()

        self.is_running = False
        self.is_paused = False

        self.random_color()

        self.generation = 0
        self.stats_enabled = True
        #self.print_cells()

        #for cell in self.cells:
        #    logging.info(f'Cell {cell} has {self.num_neighbours(cell)}')

    def start(self, initialize=False):
        self.is_running = True
        self.cells = set()
        if initialize:
            self.generation = 0
            self.initialize_world()

    def stop(self):
        self.is_running = False

    def initialize_world(self):
        """Set initial cells for the world."""
        #random.seed(SEED)
        random.seed(self.seed)
        for y in range(self.height):
            for x in range(self.width):
                if random.random() > (1 - self.initial_population):
                    self.cells.add(Cell(x, y))
        #glider = {
        #    Cell(1, 0),
        #    Cell(2, 1),
        #    Cell(0, 2),
        #    Cell(1, 2),
        #    Cell(2, 2),
        #}
        #self.cells = glider



    def print_cells(self):
        logging.info('')
        logging.info('=====')
        for y in range(self.height):
            for x in range(self.width):
                if Cell(x, y) in self.cells:
                    logging.info('X', end='')
                else:
                    logging.info('O', end='')
            logging.info('')
        logging.info('=====')
        logging.info('')

    def neighbours(self, cell):
        neighbours = {
            'top_left': Cell(cell.x-1, cell.y-1),
            'top': Cell(cell.x, cell.y-1),
            'top_right': Cell(cell.x+1, cell.y-1),
            'left': Cell(cell.x-1, cell.y),
            'right': Cell(cell.x+1, cell.y),
            'bottom_left': Cell(cell.x-1, cell.y+1),
            'bottom': Cell(cell.x, cell.y+1),
            'bottom_right': Cell(cell.x+1, cell.y+1),
        }
        #logging.info(f'neighbours of {cell}: {neighbours}')
        return neighbours

    def num_neighbours(self, cell):
        """Potentially refactor to just check for each cell in cells instead
        of using self.neighbours"""

        cell_neighbours = self.neighbours(cell)
        num_neighbours = 0
        for position, neighbour in cell_neighbours.items():
            if neighbour in self.cells:
                #logging.info(f'{cell}: {neighbour} found at {position}!')
                num_neighbours += 1
            else:
                #logging.info(f'{neighbour} NOT found!')
                pass

        return num_neighbours

    def simulate(self):
        """
        For every cell we need to check the following:
        If the cell has exactly 3 neighbours it comes to life.

        NOTE: Can optimize this to only check neighbours of living cells.
        """
        cells = set.copy(self.cells)
        if self.is_running:
            for y in range(self.height):
                for x in range(self.width):
                    cell = Cell(x, y)
                    num_neighbours = self.num_neighbours(cell)
                    if cell in self.cells:
                        if num_neighbours in [2, 3]:
                            #logging.info(f'Cell: {cell} remains alive!')
                            pass
                        else:
                            #logging.info(f'Cell: {cell} dies!')
                            cells.remove(cell)
                    elif cell not in self.cells and num_neighbours == 3:
                        #logging.info(f'New Cell: {cell} was born!')
                        cells.add(cell)  # It's ALIVE!
        self.generation += 1
        self.cells = set.copy(cells)

    def random_color(self):
        self.alive_color = random.choice([1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15])

    def update(self):
        """For every living cell, checks how many neighbours it has."""
        if pyxel.btnp(pyxel.KEY_S):
            self.stats_enabled = not self.stats_enabled

        if self.is_running:
            if pyxel.frame_count % self.frame_update_delay == 0:
                self.simulate()
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.stop()
                
        else:
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.start(initialize=True)
            if pyxel.btnp(pyxel.KEY_1):
                self.initial_population = 0.1
                self.random_color()
            if pyxel.btnp(pyxel.KEY_2):
                self.initial_population = 0.2
                self.random_color()
            if pyxel.btnp(pyxel.KEY_3):
                self.initial_population = 0.3
                self.random_color()
            if pyxel.btnp(pyxel.KEY_4):
                self.initial_population = 0.4
                self.random_color()
            if pyxel.btnp(pyxel.KEY_5):
                self.initial_population = 0.5
                self.random_color()
            if pyxel.btnp(pyxel.KEY_6):
                self.initial_population = 0.6
                self.random_color()
            if pyxel.btnp(pyxel.KEY_7):
                self.initial_population = 0.7
                self.random_color()
            if pyxel.btnp(pyxel.KEY_8):
                self.initial_population = 0.8
                self.random_color()
            if pyxel.btnp(pyxel.KEY_9):
                self.initial_population = 0.9
                self.random_color()
            if pyxel.btnp(pyxel.KEY_0):
                self.initial_population = 0.95
                self.random_color()
            if pyxel.btnp(pyxel.KEY_R):
                self.seed = random.randrange(MAX_SEED)
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()


    def draw_stats(self):
        if self.stats_enabled:
            s = 'Gen: {gen} Cells: {cells} Seed: {seed} {population}%'.format(
                    gen=self.generation,
                    cells=len(self.cells),
                    seed=self.seed,
                    population=self.initial_population * 100,
                )
            pyxel.rect(0, 0, self.width, 7, DEAD)
            pyxel.text(5, 1, s, 7)


    def draw(self):
        if self.is_running:
            for cell in self.cells:
                pyxel.pset(cell.x, cell.y, self.alive_color)
                #pyxel.pset(cell.x, cell.y, px_color)
        else:
            for cell in self.cells:
                pyxel.pset(cell.x, cell.y, self.alive_color)

            s = "Conway's Game of Life\n" \
                "A Pyxel Tribute by @krisrp\n" \
                "John Horton Conway\n" \
                "1937/12/26 - 2020/04/11\n" \
                "\n" \
                "Space: Start/Reset\n" \
                "R: Change Random Seed\n" \
                "S: Toggle Stats\n" \
                "0-9: Initial Population %\n" \
                "Q: Quit\n"

            pyxel.rect(WINDOW_WIDTH / 4 - 20, WINDOW_HEIGHT / 4, 125, 80, DEAD)

            pyxel.text(WINDOW_WIDTH / 4 - 10, WINDOW_HEIGHT / 4 + 8, s, 7)


class App:
    def __init__(self):
        # Initialize the window and caption
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption='Game of Life')

        # Create our world.
        self.world = Grid()

        pyxel.run(self.update, self.draw)


    def update(self):
        self.world.update()

    def draw(self):
        pyxel.cls(DEAD)
        self.world.draw()
        self.world.draw_stats()



if __name__ == "__main__":
    App()
