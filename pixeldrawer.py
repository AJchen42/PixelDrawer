import pygame


# PRESS ENTER TO START THE PROGRAM


'''
TODO:
-figure out how to start game without pressing enter
-handle illegal color arguments without crashing
'''


# represents a pixel in the grid
class Box:
    # keeps track of the color of this pixel
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    # draws this pixel
    def draw_box(self, screen, x, y, gridOn):
        if gridOn:
            pygame.draw.rect(screen, (self.r, self.g, self.b), (x + 1, y + 1, 14, 14))
        else:
            pygame.draw.rect(screen, (self.r, self.g, self.b), (x, y, 15, 15))



# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# define grid size
gridWidth = 80
gridHeight = 60

# define boxes
boxes = [[Box(255, 255, 255) for i in range(gridHeight)] for j in range(gridWidth)]

# current selected color and list of color in r g b order
color = ['0', '0', '0']
currentColor = 0



# function to display the boxes
def draw_boxes(screen, boxes, gridOn):

    for i in range(gridWidth):
        for j in range(gridHeight):
            boxes[i][j].draw_box(screen, (i * 15 + 100), (j * 15), gridOn)


# function to change the collor of a selected box
def update_boxes(color, x, y, boxes):

    colNum = (x - 100) // 15
    rowNum = y // 15

    boxes[colNum][rowNum] = Box(int(color[0]), int(color[1]), int(color[2]))



# function to display the text
def draw_text(screen, color, currentColor):
    font = pygame.font.SysFont('Calibri', 20, False, False)
    if currentColor == 0:
        textRed = font.render("Red: " + color[0], True, RED)
    else:
        textRed = font.render("Red: " + color[0], True, WHITE)
    if currentColor == 1:
        textGreen = font.render("Green: " + color[1], True, RED)
    else:
        textGreen = font.render("Green: " + color[1], True, WHITE)
    if currentColor == 2:
        textBlue = font.render("Blue: " + color[2], True, RED)
    else:
        textBlue = font.render("Blue: " + color[2], True, WHITE)

    if gridOn:
        textGrid = font.render("Grid: ON", True, GREEN)
    else:
        textGrid = font.render("Grid: OFF", True, RED)

    screen.blit(textRed, (10, 10))
    screen.blit(textGreen, (10, 50))
    screen.blit(textBlue, (10, 90))
    screen.blit(textGrid, (10, 130))






# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = [(gridWidth * 15) + 100, gridHeight * 15]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False
firstIter = True
gridOn = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



# Main loop
while not done:

    # catch key and mouse events
    for event in pygame.event.get():
        # end the program
        if event.type == pygame.QUIT:
            done = True
        # a key has been pressed
        if event.type == pygame.KEYDOWN:
            # handle arrow keys
            if event.key == pygame.K_DOWN:
                if currentColor < 2:
                    currentColor += 1

            if event.key == pygame.K_UP:
                if currentColor > 0:
                    currentColor -= 1

            # handle backspace
            if event.key == pygame.K_BACKSPACE:
                if len(color[currentColor]) != 0:
                    color[currentColor] = color[currentColor][:len(color[currentColor]) - 1]


            # handle numerical values
            if event.key == pygame.K_0:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '0'
            if event.key == pygame.K_1:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '1'
            if event.key == pygame.K_2:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '2'
            if event.key == pygame.K_3:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '3'
            if event.key == pygame.K_4:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '4'
            if event.key == pygame.K_5:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '5'
            if event.key == pygame.K_6:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '6'
            if event.key == pygame.K_7:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '7'
            if event.key == pygame.K_8:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '8'
            if event.key == pygame.K_9:
                if len(color[currentColor]) < 3:
                    color[currentColor] = color[currentColor] + '9'

            # handle space bar
            if event.key == pygame.K_SPACE:
                if gridOn:
                    gridOn = False
                else:
                    gridOn = True

            # draw boxes and text on a black background
            screen.fill(BLACK)
            draw_boxes(screen, boxes, gridOn)
            draw_text(screen, color, currentColor)

            # update the display
            pygame.display.update()

            # handle mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Call draw stick figure function
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]

            # udpate the clicked box
            update_boxes(color, x, y, boxes)

            # reset the screen with new updated boxes
            screen.fill(BLACK)
            draw_boxes(screen, boxes, gridOn)
            draw_text(screen, color, currentColor)

            # update the display
            pygame.display.update()

    # Limit frames
    clock.tick(60)

# ensure program quits
pygame.quit()
