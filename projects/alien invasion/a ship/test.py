import pygame
from ship import Ship  # Assuming ship.py is the file with the Ship class

def run_game():
    # Initialize the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance of Ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Redraw the screen during each pass through the loop
        screen.fill((230, 230, 230))
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
