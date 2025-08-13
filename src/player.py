import pygame

class Player:
    def __init__(self, x, y, color):
        """
        Initialize the player.
        Parameters:
            x: Initial x-coordinate
            y: Initial y-coordinate
            color: Color of the player's trail
        """
        # Set initial position, color, direction (e.g., [1, 0] for right)
        # Initialize an empty list for the player's trail

        self.x = x
        self.y = y
        self.color = color
        self.direction = [1, 0]
        self.trail = []


    def move(self):
        """
        Move the player based on their current direction.
        """
        # Update the player's position based on their direction
        # Add the new position to the trail
        
        self.x += self.direction[0]
        self.y += self.direction[1]

        self.trail.append([self.x, self.y])


    def change_direction(self, new_direction):
        """
        Change the player's direction.
        :param direction: New direction as a list [dx, dy]
        """
        # Update the player's direction
        # Ensure the new direction is not opposite to the current direction

        new_direction_x, new_direction_y = new_direction
        curr_direction_x, curr_direction_y = self.direction

        # Can't change 180 degrees
        if (new_direction_x == -curr_direction_x or new_direction_y == -curr_direction_y):
            return False
        
        self.direction = new_direction
        return True


    def draw(self, screen, cell_width, cell_height):
        """
        Draw the player and their trail on the screen.
        Parameter:
            screen: Pygame screen object to draw on
        """
        # Draw the player's current position and their entire trail
        # Player is drawn in GameBoard
        
        pass

