#Import pygame library
import pygame

#import random library
import random


#Defining colors
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0,0,255)


#Setting up width and height of each box
WIDTH = 20
HEIGHT = 20

#Margin between each cell
MARGIN = 5

#Creating a 2-Dimensional array - list of lists
grid = []
for row in range(10):
    #Add an empty list
    grid.append([])
    for column in range(10):
        grid[row].append(0) #Append a cell


# Initialize pygame
pygame.init()


#Set the dimensions of the screen
WINDOW_SIZE = [255,255]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Set the title of the screen
pygame.display.set_caption("Pixel War")

#Loop till the user QUITS
done = False;

#update 60 frames per second
clock = pygame.time.Clock()

#--------Main Program Loop-------------

while not done:
    #Capture all events
    for event in pygame.event.get():
        #Close if the player quits
        if event.type == pygame.QUIT:
            done = True
        #Else look if there is a keypress
        elif event.type == pygame.KEYDOWN:
            found = False
            # Find grid co-ordinates which is non-zero
            while not found:
                random_row = random.randint(0,9)
                random_column = random.randint(0,9)
                #print (random_row)
                #print (random_column)
                if grid[random_row][random_column]==0:
                    found = True

            
            # "r" correspods to red and "b" corresponds to blue        
            if event.key == pygame.K_r:
                grid[random_row][random_column] = 5
            if event.key == pygame.K_b:
                grid[random_row][random_column] = 10

    # Set the screen background
    screen.fill(WHITE)

    #Draw the grid
    for row in range(10):
        for column in range(10):
            color = BLACK

            if grid[row][column] == 5:
                color = RED
            elif grid[row][column] == 10:
                color = BLUE

            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) *
                                            row + MARGIN, WIDTH, HEIGHT])

    #Limit to 60 frames per second
    clock.tick(60)

    #Update the screen
    pygame.display.flip()

#Quit when the program exits
pygame.quit()




                

