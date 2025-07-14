# The pygame library is used to create games in Python.
# It provides functions to create windows, draw shapes, handle events, and play sounds.
import pygame


"""
This is the initial starting point to build the snake game.
It has the minimal boiler-plate pygame code to get started.
It will draw a COLOUR_GREEN square on a black background and wait for 2 seconds before quitting.
"""
# Set up constants for colours
# Each colour is a tuple of COLOUR_RED, COLOUR_GREEN,  Blue  values.  Each value can range from 0 to 255.
COLOUR_GREEN = (0, 255, 0)
COLOUR_BLACK = (0, 0, 0)
COLOUR_RED = (255, 0, 0)
COLOUR_BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((640, 480))

# Set the title of the window
pygame.display.set_caption("Python Snake Game")
clock = pygame.time.Clock()

colour = COLOUR_GREEN  # Set the colour to COLOUR_GREEN
game_over = False
while not game_over:
    for event in pygame.event.get():
        #print(event)
        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            # If the user presses the escape key, exit the game
            if event.key == pygame.K_b:
                colour = COLOUR_BLUE
            elif event.key == pygame.K_r:
                colour = COLOUR_RED

    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw a COLOUR_GREEN square (the snake) at the center of the screen
    # The square is 20x20 pixels in size and is drawn at (320, 240) on the screen.
    # The coordinates are the top-left corner of the square.
    pygame.draw.rect(screen, colour, [320, 240, 20,20])

    pygame.display.update()
    clock.tick(5)  # Limit the frame rate to 5 FPS


pygame.quit()