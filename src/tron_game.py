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
    pygame.font.init()

    
    WIDTH, HEIGHT = 1200, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Tron Game")
    screen.fill((0, 0, 0))
    
    pygame.display.flip()

    return screen



def handle_events(players):
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
        
        player1 = players[0]
        player2 = players[1]
        # Move the player based on key presses
       
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                new_direction = (-1, 0)
                player1.change_direction(new_direction)

            elif event.key == pygame.K_RIGHT:
                new_direction = (1, 0)
                player1.change_direction(new_direction)

            elif event.key == pygame.K_UP:
                new_direction = (0, -1)
                player1.change_direction(new_direction)

            elif event.key == pygame.K_DOWN:
                new_direction = (0, 1)
                player1.change_direction(new_direction)



            if event.key == pygame.K_a:
                new_direction = (-1, 0)
                player2.change_direction(new_direction)

            elif event.key == pygame.K_d:
                new_direction = (1, 0)
                player2.change_direction(new_direction)

            elif event.key == pygame.K_w:
                new_direction = (0, -1)
                player2.change_direction(new_direction)

            elif event.key == pygame.K_s:
                new_direction = (0, 1)
                player2.change_direction(new_direction)

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
    
    # No collision, then player can move
    player.move()
    
    # Update gameboard with new player position (mark as trail)
    if game_board:
        game_board.gridCells[player.y][player.x] = player.player_id

    
    return True


def draw_score(screen, game_board, players):

    font = pygame.font.SysFont('Arial', 30)
    screen.fill((0, 0, 0))

    screen_width, screen_height = screen.get_size()
    rect_width = screen_width // game_board.width
    rect_height = screen_height // game_board.height

    for player in players:
        score_surface = font.render(f"Player {player.player_id} Score: {player.score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (player.x * 1.3 * rect_width, screen_height // 2))
        screen.blit(score_surface, score_rect)

    
    pygame.display.flip()


def draw_game(screen, game_board):
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
    player1 = Player(10, 10, (255, 0, 0), 1, [1, 0], 0)
    player2 = Player(40, 40, (0, 0, 255), 2, [-1, 0], 0)
    game_board = GameBoard(50, 50)
    
    players = [player1, player2]

    clock = pygame.time.Clock()
    
    running = True
    game_over = False
    while (running):
        
        while not game_over:
            if not handle_events(players):
                game_over = True
        
            for player in players:
                if not update_game_state(player, game_board):
                    game_over = True

            draw_game(screen, game_board)
            
            clock.tick(10)

        
        draw_score(screen, game_board, players)

        pygame.time.wait(2000)
        running = False
   
    pygame.quit()




# Run Main Game Function
if __name__ == "__main__":
    main()