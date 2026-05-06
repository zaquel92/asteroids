import pygame
from constants import *
from logger import log_state
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start of game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        player.draw(screen)
        player.update(dt)

        # screen render
        pygame.display.flip()

        # to reduce refresh resource consumption
        clock.tick(60)
        dt = clock.tick(60) / 1000

    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(
         f"Screen width: {SCREEN_WIDTH}\
         Screen height: {SCREEN_HEIGHT}"
         )


if __name__ == "__main__":
    main()
