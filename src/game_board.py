import pygame

class Gameboard:
    def __init__(self, width, height):
        ''' 
        Initialize the game window.
        Parameters:
            Width: width of game board in grid cells
            Height: height of game board in grid cells
        '''
        
        # 2D List: 0's represent empty cells, 1's represent player trail

        self.width = width
        self.height = height
        

        gridCells = [[0 for w in range(height)] for h in range(width)]
        gridCells[0][1] = 1

        self.gridCells = gridCells
        print (gridCells)
    
    def draw(self, screen):
        """
        Draw the game board on the screen.
        Parameters:
            Pygame screen object to draw on
        """
        # Iterate through the 2D list and draw rectangles for each cell
        # Empty cells can be one color, trails another

        screen_width, screen_height = screen.get_size()
        rect_width = screen_width // self.width
        rect_height = screen_height // self.height
        
        

        for r in range(self.height):
            for c in  range(self.width):
                if (self.gridCells[r][c] == 1):
                    # Red Rectangle - Player Trail
                    pygame.draw.rect(screen, (255, 0, 0), (c * rect_width, r * rect_height, rect_width, rect_height))
                else:
                    # Green Rectangle - Empty Cells
                    pygame.draw.rect(screen, (0, 255, 0), (c * rect_width, r * rect_height, rect_width, rect_height))

    def is_collision(self, x, y):
        """
        Check if the given coordinates collide with the board boundaries or a trail.
        Parameters:
            x: X-coordinate
            y: Y-coordinate
        Return: True if collision, False otherwise
        """
        # Check if x and y are within board boundaries
        # Also check if the cell at (x, y) is not empty (i.e., has a trail)

        if (x < 0 or x > self.width or y < 0 or y > self.height):
            return False

        # True if cell is a Player Trail (collision)
        return (self.gridCells[y][x] == 1)




