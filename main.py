# Import and initialize the pygame library
import pygame
pygame.init()

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((612, 306))

# Set the title of the pygame screen
pygame.display.set_caption("My Corkboard")

#Set the backround image 
corkboard = pygame.image.load("corkboard.jpg")
corkboard = pygame.transform.scale(corkboard, (550, 306))
screen.blit(corkboard, (0, 0))

#my name
#font that i download
baloo_42 = pygame.font.Font("baloo.ttf", 42)
baloo_64 = pygame.font.Font("baloo.ttf", 32)
...
#this will show my name with a color blue 
game_over_image = baloo_64.render("Karl Chester Ballacillo", True, "blue")
...
#this can render text into an image and displaying the image 
game_over_rect = game_over_image.get_rect(center = (270, 30))
screen.blit(game_over_image, game_over_rect)

#my picture
#in this 5 blocks have a image loading, transforming scales, flipping, blitting and zooming
me = pygame.image.load("me.jpeg").convert_alpha()
me = pygame.transform.scale(me, (270, 250))
me = pygame.transform.rotozoom(me, 15, 0.50)
screen.blit(me, (40, 40))
pin = pygame.image.load("pin.png").convert_alpha()
pin = pygame.transform.scale(pin, (35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (80, 50))

#my country i want to travel
country = pygame.image.load("country.jpeg").convert_alpha()
country = pygame.transform.scale(country, (200, 150))
country = pygame.transform.rotozoom(country, 15, 0.50)
screen.blit(country, (200, 190))
pin = pygame.image.load("pin.png").convert_alpha()
pin = pygame.transform.scale(pin, (35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (200, 205))

#my pet 
pet = pygame.image.load("pet.jpeg").convert_alpha()
pet = pygame.transform.scale(pet, (250, 210))
pet = pygame.transform.rotozoom(pet, 15, 0.50)
screen.blit(pet, (50, 180))
pin = pygame.image.load("pin.png").convert_alpha()
pin = pygame.transform.scale(pin, (35, 35))
pin = pygame.transform.flip(pin, True, False)
screen.blit(pin, (100, 185))

#award medal
award = pygame.image.load("award.png").convert_alpha()
award = pygame.transform.scale(award, (870, 970))
award = pygame.transform.rotozoom(award, 15, 0.15)
screen.blit(award, (180, 40))

#favorite show
movie = pygame.image.load("squidgame.jpeg").convert_alpha()
movie = pygame.transform.scale(movie,(350, 495))
movie = pygame.transform.rotozoom(movie, -5, 0.50)
screen.blit(movie, (330, 45))

#in this we're going to blit the 2 pins because we want the program to be organized, instead of putting 5 copies of pins every block
# Load the picture
smiley = pygame.image.load("pin.png")

# Blit the pins in two locations
screen.blit(pin, (240,60))
screen.blit(pin, (430,50))

# Uncomment the next lines to show a grid
#from pygame_grid import draw_grid
#draw_grid()

# Flip3the changes to the screen to the computer display
pygame.display.flip()
