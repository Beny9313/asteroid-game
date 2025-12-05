import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # --- HACK: Safe Target Practice ---
    # Spawn a large asteroid 250 pixels away (downwards). 
    # This is far enough so the player doesn't crash immediately, 
    # but close enough for the auto-fire bullets to hit and split it.
    Asteroid(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 250, ASTEROID_MAX_RADIUS)

    while True:
        log_state() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            # Check for player death
            if asteroid.collides_with(player):
                print("Game over!")
                log_event("player_hit")
                sys.exit()
            
            # Check for bullet hits (Nested Loop)
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    # We now split instead of just killing
                    asteroid.split()
                    log_event("asteroid_shot")
        
        pygame.display.flip()
        
        dt = gameClock.tick(60) / 1000

if __name__ == "__main__":
    main()