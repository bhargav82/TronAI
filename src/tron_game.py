import pygame
from game_board import GameBoard
from player import Player


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
        

        # Move the player based on key presses
       
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                new_direction = (-1, 0)
                player.change_direction(new_direction)

            elif event.key == pygame.K_RIGHT:
                new_direction = (1, 0)
                player.change_direction(new_direction)

            elif event.key == pygame.K_UP:
                new_direction = (0, -1)
                player.change_direction(new_direction)

            elif event.key == pygame.K_DOWN:
                new_direction = (0, 1)
                player.change_direction(new_direction)

    return True
    


def update_game_state(player, game_board):
    """
    Update the game state, including player movement and collision detection.
    Parameters:
        player: Player object to update
        game_board: GameBoard object to check collisions against
    Return: False if the game is over (collision), True otherwise
    """
    # Move the player
    # Check for collisions with game_board
    # Update game_board with new player position
    

    next_x = player.x + player.direction[0]
    next_y = player.y + player.direction[1]
    

    # Game over due to collision
    if game_board and game_board.is_collision(next_x, next_y):
        return False  
    
    # If no collision, move the player
    player.move()
    
    # Update game_board with new player position (mark as trail)
    if game_board:
        game_board.gridCells[player.y][player.x] = 1

    
    return True



def draw_game(screen, game_board, player):
    """
    Draw the current game state.
    Parameters:
        Pygame screen object to draw on
        game_board: GameBoard object to draw
        player: Player object to draw
    """
    # Clear the screen
    # Draw the game board
    # Draw the player
    # Update the display

    screen.fill((0, 0, 0))
    game_board.draw(screen)
    player.draw(screen, game_board.width, game_board.height)

    pygame.display.flip()



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

    screen = initialize_game()
    player = Player(10, 10, (50, 50, 50))
    game_board = GameBoard(50, 50)
    

    clock = pygame.time.Clock()
    
    running = True
    while (running):
        
        if not handle_events(player):
            running = False
    
        if not update_game_state(player, game_board):
            running = False

        draw_game(screen, game_board, player)
       

        clock.tick(10)



    pygame.quit()
    
    
main()