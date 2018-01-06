"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def slide_to_left(line):
    """
    To make all non-zero integers to be at the left of the list
    """
    length = len(line)
    count = 0
    output = [0] * length
    for i in range(length):
        if line[i] != 0:
            output[i - count] = line[i]
        else:
            count += 1
    return output

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    output = slide_to_left(line)
    for i in range(len(line) - 1):
        if output[i] != 0 and output[i] == output[i + 1]:
            output[i] *= 2
            output[i + 1] = 0
    output = slide_to_left(output)
    return output

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
        self.reset()
        self.start_cells = {UP: [(0, col) for col in range(self.width)], 
                            DOWN: [(self.height - 1, self.width - 1 - col) for col in range(self.width)], 
                            LEFT: [(row, 0) for row in range(self.height)], 
                            RIGHT: [(row, self.width - 1) for row in range(self.height)]}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.width)] for row in range(self.height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        print(self.grid)
        return "test"

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction in (UP, DOWN):
            temp_width = self.height
            temp_height = self.width
        if direction in (LEFT, RIGHT):
            temp_width = self.width
            temp_height = self.height
        # traverse to a temporary grid and merge
        temp_grid = [[0 for col in range(temp_width)] for row in range(temp_height)]
        for col in range(temp_width):
            for row in range(temp_height):
                temp_tuple = self.start_cells[direction][row]
                step_tuple = (col * OFFSETS[direction][0], col * OFFSETS[direction][1])
                # print(temp_tuple)
                # print(step_tuple)
                # print(temp_tuple[0]+step_tuple[0], temp_tuple[1]+step_tuple[1])
                # print("---")
                temp_grid[row][col] = self.grid[temp_tuple[0]+step_tuple[0]][temp_tuple[1]+step_tuple[1]]
        for row in range(temp_height):
            temp_grid[row] = merge(temp_grid[row])
        
        # traverse back
        output_grid = [[0 for col in range(self.width)] for row in range(self.height)]
        temp_start_cells = {UP: [(0, col) for col in range(temp_width)], 
                            DOWN: [(temp_height - 1, temp_width - 1 - col) for col in range(temp_width)], 
                            LEFT: [(row, 0) for row in range(temp_height)], 
                            RIGHT: [(row, temp_width - 1) for row in range(temp_height)]}
        for col in range(self.width):
            for row in range(self.height):
                temp_tuple = temp_start_cells[direction][row]
                step_tuple = (col * OFFSETS[direction][0], col * OFFSETS[direction][1])
                output_grid[row][col] = temp_grid[temp_tuple[0]+step_tuple[0]][temp_tuple[1]+step_tuple[1]]
        
        # determine whether a new tile
        if output_grid != self.grid:
            self.grid = output_grid
            self.new_tile()
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        zero_cells = []
        for row in range(self.height):
            for col in range(self.width):
                if self.grid[row][col] == 0:
                    zero_cells.append((row, col))
        random_cell = random.choice(zero_cells)
        row, col = random_cell
        if int(random.random() * 10) == 0:
            self.grid[row][col] = 4
        else:
            self.grid[row][col] = 2

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

a_grid = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(a_grid)
print(a_grid)