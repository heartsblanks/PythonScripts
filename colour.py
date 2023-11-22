import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Exam Result Confetti")

white = (255, 255, 255)
failed_color = (255, 0, 0)  # Red for failed
passed_color = (0, 255, 0)  # Green for passed

confetti_size = 10

# Create a list to store confetti positions and their colors
confetti_positions = [(random.randint(0, screen_width), random.randint(0, screen_height), failed_color) for _ in range(50)]
confetti_positions += [(random.randint(0, screen_width), random.randint(0, screen_height), passed_color) for _ in range(50)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    for confetti in confetti_positions:
        pygame.draw.circle(screen, confetti[2], (confetti[0], confetti[1]), confetti_size)

    pygame.display.flip()
    pygame.time.delay(50)

    # Move confetti (falling effect)
    confetti_positions = [(x, y + 5, color) for x, y, color in confetti_positions]

    # Reset confetti that has fallen off the screen
    confetti_positions = [(x, y, color) if y < screen_height else (random.randint(0, screen_width), 0, color) for x, y, color in confetti_positions]