import pygame

# Game Display Setup
pygame.init()
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tron Game")


# Main Game
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Black Background
    screen.fill((0, 0, 0))

    

    # Red Rectangle, Green Circle
    pygame.draw.rect(screen, (255, 0, 0), (400, 300, 50, 30))
   

    # Update Display
    pygame.display.flip()

# End Game
pygame.quit()
