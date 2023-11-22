import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balloon Animation")

white = (255, 255, 255)
balloon_radius = 20
balloon_color = (0, 0, 255)  # Blue balloons for example

balloons = [{'x': random.randint(0, screen_width),
             'y': random.randint(screen_height // 2, screen_height),
             'speed': random.randint(1, 3)} for _ in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    for balloon in balloons:
        pygame.draw.circle(screen, balloon_color, (balloon['x'], balloon['y']), balloon_radius)

    pygame.display.flip()
    pygame.time.delay(30)

    for balloon in balloons:
        balloon['y'] -= balloon['speed']

        # Reset balloon at the bottom when it goes off the screen
        if balloon['y'] < 0:
            balloon['y'] = screen_height
            balloon['x'] = random.randint(0, screen_width)
            balloon['speed'] = random.randint(1, 3)