import pygame
from logger import log_state  # Assuming log_state is imported from your previous file
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # 1. Initialize clock and dt
    gameClock = pygame.time.Clock()
    dt = 0
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        log_state() # This checks internal frame count
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        dt = gameClock.tick(60) / 1000 
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    player.draw(screen)

if __name__ == "__main__":
    main()