"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)      
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        # replace with an actual generator
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list) 
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        visited = poc_grid.Grid(self._grid_height, self._grid_width)
        distance_field = [ [self._grid_height * self._grid_width for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height) ]
        
        boundary = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for cell in self._zombie_list:
                boundary.enqueue(cell)
        elif entity_type == HUMAN:
            for cell in self._human_list:
                boundary.enqueue(cell)
        
        for cell in boundary:
            visited.set_full(cell[0], cell[1])
            distance_field[cell[0]][cell[1]] = 0
            
        # put full cells in obstacle_list into visited grid
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if self._cells[row][col] == FULL:
                    visited.set_full(row, col)

        # implement the BFS method
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            neighbors = visited.four_neighbors(current_cell[0], current_cell[1])
            for neighbor in neighbors:
                if visited.is_empty(neighbor[0], neighbor[1]):
                    visited.set_full(neighbor[0], neighbor[1])
                    distance_field[neighbor[0]][neighbor[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
                    boundary.enqueue(neighbor)
       
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        best_moves = []
        
        for human in self._human_list:
            human_neighbors = self.eight_neighbors(human[0], human[1])
            distance_from_zombie = {}
            for neighbor in human_neighbors:
                distance_from_zombie[neighbor] = zombie_distance_field[neighbor[0]][neighbor[1]]
            max_distance = max(distance_from_zombie.values())
            possible_moves = [move for move, distance in distance_from_zombie.items() if distance == max_distance]
            best_move = random.choice(possible_moves)
            best_moves.append(best_move)
        
        self._human_list = best_moves
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        best_moves = []
        
        for zombie in self._zombie_list:
            zombie_neighbors = self.four_neighbors(zombie[0], zombie[1])
            distance_from_human = {}
            for neighbor in zombie_neighbors:
                distance_from_human[neighbor] = human_distance_field[neighbor[0]][neighbor[1]]
            min_distance = min(distance_from_human.values())
            possible_moves = [move for move, distance in distance_from_human.items() if distance == min_distance]
            best_move = random.choice(possible_moves)
            best_moves.append(best_move)
        
        self._zombie_list = best_moves


poc_zombie_gui.run_gui(Apocalypse(30, 40))
