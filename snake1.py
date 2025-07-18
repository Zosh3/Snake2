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

NUM_SQUARES_X = 32  # Number of squares in the X direction
NUM_SQUARES_Y = 24  # Number of squares in the Y direction
SQUARE_SIZE = 20  # Size of the square (snake segment)
SCREEN_WIDTH = NUM_SQUARES_X * SQUARE_SIZE
SCREEN_HEIGHT = NUM_SQUARES_Y * SQUARE_SIZE
INITIAL_X = NUM_SQUARES_X // 2
INITIAL_Y = NUM_SQUARES_Y // 2

snake = [INITIAL_X, INITIAL_Y]  # Initialize the snake with one segment at the center of the screen

def out_of_bounds(x, y):
    """
    Check if the given coordinates are out of bounds.
    Returns True if out of bounds, False otherwise.
    """
    return x >= NUM_SQUARES_X or x < 0 or y >= NUM_SQUARES_Y or y < 0


# Initialize Pygame
pygame.init()
# Initialize the mixer module (which is used for sound)
pygame.mixer.init()  

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
            elif event.key == pygame.K_UP:
                snake[1] = snake[1] - 1
            elif event.key == pygame.K_DOWN:
                snake[1] = snake[1] + 1
            elif event.key == pygame.K_LEFT:
                snake[0] = snake[0] - 1
            elif event.key == pygame.K_RIGHT:
                snake[0] = snake[0] + 1

    if out_of_bounds(snake[0], snake[1]):
        game_over = True

    # Fill the background with black
    screen.fill(COLOUR_BLACK)

    # Draw a COLOUR_GREEN square (the snake) at the center of the screen
    # The square is SQUARE_SIZE x SQUARE_SIZE pixels in size and is drawn at (x, y) on the screen.
    # The coordinates are the top-left corner of the square.
    pygame.draw.rect(screen, colour, [snake[0]*SQUARE_SIZE, snake[1]*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE])

    pygame.display.update()
    clock.tick(5)  # Limit the frame rate to 5 FPS


pygame.quit()