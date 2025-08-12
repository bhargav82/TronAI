import pygame
from game_board import Gameboard
from player import Player



Board = Gameboard(20, 20)


# Draw Grid
Board.draw(screen)
   



# End Game




# Game Display Setup
def initialize_game():
    """
    Initialize Pygame and create the game window.
    Return: Pygame screen object
    """
    # Initialize Pygame
    # Create and return a Pygame screen object

    pygame.init()
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tron Game")
    screen.fill((0, 0, 0))
    
    pygame.display.flip()

    return screen

def handle_events(player):
    """
    Handle Pygame events, including player input.
    Parameters:
        player: Player object to update based on input
    Return: False if the game should quit, True otherwise
    """
    # Loop through Pygame events
    # Handle QUIT event
    # Handle KEYDOWN events to change player direction

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        
        keys = pygame.key.get_pressed()
            

        # Move the player based on key presses
        if keys[pygame.K_LEFT]:
            player.
        if keys[pygame.K_RIGHT]:
            player_rect.x += speed
        if keys[pygame.K_UP]:
            player_rect.y -= speed
        if keys[pygame.K_DOWN]:
            player_rect.y += speed

        return True

def update_game_state(player, game_board):
    """
    Update the game state, including player movement and collision detection.
    :param player: Player object to update
    :param game_board: GameBoard object to check collisions against
    :return: False if the game is over (collision), True otherwise
    """
    # TODO: Move the player
    # Check for collisions with game_board
    # Update game_board with new player position

def draw_game(screen, game_board, player):
    """
    Draw the current game state.
    :param screen: Pygame screen object to draw on
    :param game_board: GameBoard object to draw
    :param player: Player object to draw
    """
    # TODO: Clear the screen
    # Draw the game board
    # Draw the player
    # Update the display

def main():
    """
    Main game loop.
    """
    #  Initialize the game
    # Create game objects (game_board, player)
    # Run the game loop:
    #   - Handle events
    #   - Update game state
    #   - Draw game
    #   - Control game speed

    initialize_game()
    draw_game()
    
    while (handle_events)

    
    pygame.quit()