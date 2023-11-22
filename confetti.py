import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Confetti Animation")

# Define colors
white = (255, 255, 255)

# Define confetti
confetti_size = 10
confetti_color = (255, 0, 0)  # Red confetti for example

# Create a list to store confetti positions
confetti_positions = [(random.randint(0, screen_width), random.randint(0, screen_height)) for _ in range(100)]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw confetti
    screen.fill(white)
    for confetti in confetti_positions:
        pygame.draw.circle(screen, confetti_color, confetti, confetti_size)

    # Update display
    pygame.display.flip()

    # Add a slight delay to control the speed of animation
    pygame.time.delay(50)

    # Move confetti (falling effect)
    confetti_positions = [(x, y + 5) for x, y in confetti_positions]

    # Reset confetti that has fallen off the screen
    confetti_positions = [(x, y) if y < screen_height else (random.randint(0, screen_width), 0) for x, y in confetti_positions]