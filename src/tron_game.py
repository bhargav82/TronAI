import pygame
from game_board import GameBoard
from player import Player
from mockAI import MockAI
from rl_ai import RLAgent

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



def handle_events() -> bool:
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
        
    return True
    


def update_game_state(player1: Player, player2: Player, game_board: GameBoard) -> int:
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
    


    next_x1 = player1.x + player1.direction[0]
    next_y1 = player1.y + player1.direction[1]

    next_x2 = player2.x + player2.direction[0]
    next_y2= player2.y + player2.direction[1]

    collision1 = game_board.is_collision(next_x1, next_y1)
    collision2 = game_board.is_collision(next_x2, next_y2)

    head_on_collision = (next_x1, next_x2) == (next_y1, next_y2)


    if head_on_collision:
        return 3
    elif collision1 and collision2:
        return 3
    elif collision1:
        return 2                        # Player2 Wins
    elif collision2:
        return 1                        # Player1 Wins
    

    # No collision, then players can move
    player1.move(game_board)
    player2.move(game_board)
    
    # Update gameboard with new player position (mark as trail)
    
    game_board.gridCells[player1.y][player1.x] = player1.player_id
    game_board.gridCells[player2.y][player2.x] = player2.player_id


    
    return 0


def draw_score(screen, players):

    font = pygame.font.SysFont('Arial', 30)
    screen.fill((0, 0, 0))

    screen_width, screen_height = screen.get_size()


    for i, player in enumerate(players):
        score_surface = font.render(f"Player {player.player_id} Score: {player.score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (screen_width * 0.33 * (i + 1), screen_height // 2))
        screen.blit(score_surface, score_rect)

    text_surface = font.render("Press Enter to Play Again!", True, (255, 255, 255))
    screen.blit(text_surface, (screen_width // 2.6, screen_height // 1.2))
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
    clock = pygame.time.Clock()
    running = True
    player1score = 0
    player2score = 0

    while (running):

        # New Game Initalization
        ai1 = RLAgent(state_size=49, action_size=4, model_file="tron_survival_model.pth")
        ai2 = RLAgent(state_size=49, action_size=4, model_file="tron_survival_model.pth")

        player1 = Player(10, 10, (255, 0, 0), 1, [1, 0], player1score, ai1)
        player2 = Player(40, 40, (0, 0, 255), 2, [-1, 0], player2score, ai2)
        game_board = GameBoard(50, 50)
        
        players = [player1, player2]
        
        game_over = False
        
        while not game_over:
            # Game Loop
            if not handle_events():
                running = False
                break

            result = update_game_state(player1, player2, game_board)
            if result != 0:
                if result == 1:
                    player1score += 1
                    player1.score = player1score
                elif result == 2:
                    player2score += 1
                    player2.score = player2score

                game_over = True

            else:
                draw_game(screen, game_board)
                clock.tick(10)

        if not running:
            break
        

        draw_score(screen, players)

        waiting_for_enter = True
        while waiting_for_enter:
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        waiting_for_enter = False
                    elif event.key == pygame.K_q:
                        running = False
                        waiting_for_enter = False
  
   
    pygame.quit()




# Run Main Game Function
if __name__ == "__main__":
    main()