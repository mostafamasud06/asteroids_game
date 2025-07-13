import pygame
from constants import *
def main():
    pygame.init()
    # Open the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # 3) Draw: fill the screen with black
        screen.fill("black")
        pygame.display.flip()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
if __name__ == "__main__":
    main()
