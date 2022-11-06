# Import and initialize the pygame library
import pygame
pygame.init()

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((612, 306))

# Set the title of the pygame screen
pygame.display.set_caption("My Corkboard")

#Set the backround image 
corkboard = pygame.image.load("corkboard.jpg")
corkboard =  pygame.transform.scale(corkboard,(550, 306))
screen.blit(corkboard, (0, 0))

#my name
baloo_32 = pygame.font.Font("baloo.ttf", 42)
baloo_64 = pygame.font.Font("baloo.ttf", 32)
...
game_over_image = baloo_64.render("Karl Chester Ballacillo", True, "blue")
...
game_over_rect = game_over_image.get_rect(center=(270, 30))
screen.blit(game_over_image, game_over_rect)

#my picture
me = pygame.image.load("me.jpeg").convert_alpha()
me = pygame.transform.scale(me,(230, 250))
me = pygame.transform.rotozoom(me, 15, 0.50)
screen.blit(me, (40, 40))
pin = pygame.image.load("push_pin.png").convert_alpha()
pin = pygame.transform.scale(pin,(35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (80, 50))

#my country i want to travel
country = pygame.image.load("country.jpeg").convert_alpha()
country = pygame.transform.scale(country,(200, 150))
country = pygame.transform.rotozoom(country, 15, 0.50)
screen.blit(country, (200, 190))
pin = pygame.image.load("push_pin.png").convert_alpha()
pin = pygame.transform.scale(pin,(35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (200, 200))

#my pet 
pet = pygame.image.load("pet.jpeg").convert_alpha()
pet = pygame.transform.scale(pet, (180, 220))
pet = pygame.transform.rotozoom(pet, 15, 0.50)
screen.blit(pet, (50, 180))
pin = pygame.image.load("push_pin.png").convert_alpha()
pin = pygame.transform.scale(pin,(35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (75, 185))

#award medal
award = pygame.image.load("award.png").convert_alpha()
award = pygame.transform.scale(award,(870, 970))
award = pygame.transform.rotozoom(award, 15, 0.15)
screen.blit(award, (180, 40))
pin = pygame.image.load("push_pin.png").convert_alpha()
pin = pygame.transform.scale(pin,(35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (230, 70))

#favorite show
movie = pygame.image.load("squidgame.jpeg").convert_alpha()
movie = pygame.transform.scale(movie,(350, 495))
movie = pygame.transform.rotozoom(movie, -5, 0.50)
screen.blit(movie, (330, 45))
pin = pygame.image.load("push_pin.png").convert_alpha()
pin = pygame.transform.scale(pin,(35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (425, 45))

# Uncomment the next lines to show a grid
from pygame_grid import draw_grid
draw_grid()

# Flip3the changes to the screen to the computer display
pygame.display.flip()
