import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting Asteroids with pygame version:", pygame.version.vernum)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)    

    game_clock = pygame.time.Clock()
    dt = 0

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while(True):
        
        log_state()
        for event in pygame.event.get():
            pass

        updatable.update(dt)
        pygame.Surface.fill(screen, "black")
        
        for thang in drawable:
            thang.draw(screen)
        
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
if __name__ == "__main__":
    main()