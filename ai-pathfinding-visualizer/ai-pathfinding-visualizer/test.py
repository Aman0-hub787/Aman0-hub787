import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Rectangle properties
rect_x, rect_y = 50, 50
rect_width, rect_height = 100, 50
rect_speed_x, rect_speed_y = 5, 5

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update rectangle position
    rect_x += rect_speed_x
    rect_y += rect_speed_y

    # Bounce the rectangle off the edges
    if rect_x <= 0 or rect_x + rect_width >= WIDTH:
        rect_speed_x = -rect_speed_x
    if rect_y <= 0 or rect_y + rect_height >= HEIGHT:
        rect_speed_y = -rect_speed_y

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)