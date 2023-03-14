# Base game from: https://www.edureka.co/blog/snake-game-with-pygame/#install
# However I modified it to play a bit differently, and added in more features.

# Importing nessesary packages.
import pygame
import random
import time

# Starts up the game.
pygame.init()

# If this is true the game ends and the window closes.
endGame = False

# Defines the colors for different objects.
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (50, 255, 0)
yellow = (255, 255, 100)

# Sets the size of the display window.
displayWidth = 800
displayHeight = 600

# Creates the display window at the size specified above.
# Also names the display window.
dis = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Snake Game')

# Defines how much the snake moves each tick.
snakeSpeed = 10

# Sets the size of the snake blocks, and the food blocks.
snakeBlock = 10

# Sets the tick speed.
clockSpeed = 15

# Defining the clock.
clock = pygame.time.Clock()

# Setting a font for the messages.
gameFont = pygame.font.SysFont("bahnschrift", 22)

# Displays the main menu on the screen.
def menu():

    # Declaring these variables to be the global ones.
    global clockSpeed
    global endGame

    # Initilizing this to be true.
    inMenu = True

    # Clearing the screen.
    dis.fill(black)

    # Ask for what difficulty the player wants.
    message("Press e for easy mode, m for medium, and h for hard.", white)
    pygame.display.update()

    # While a game mode hasn't been chosen and the game hasn't been closed, do stuff.
    while inMenu == True and endGame == False:

        # Get and check all or any game events.
        for event in pygame.event.get():

            # If window is closed, exit menu and end the game.
            if event.type == pygame.QUIT:
                inMenu = False
                endGame = True
            if event.type == pygame.KEYDOWN:

                # If 'e' clicked, game set to easy (Slow movement speed).
                if event.key == pygame.K_e:
                    clockSpeed = 10
                    inMenu = False
                
                # If 'm' clicked, game set to medium (Normal movement speed).
                if event.key == pygame.K_m:
                    clockSpeed = 20
                    inMenu = False
                
                # If 'h' clicked, game set to hard (Fast movement speed).
                if event.key == pygame.K_h:
                    clockSpeed = 30
                    inMenu = False
    

# Displays the score on the screen.
def score(num):
    msg = gameFont.render("Score: " + str(num), True, yellow)
    dis.blit(msg, [0, 0])

# Draws the snake on the screen.
def mySnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, white, [x[0], x[1], snakeBlock, snakeBlock])

# Displays a message on the screen.
def message(msg, color):
    mesg = gameFont.render(msg, True, color)
    dis.blit(mesg, [displayWidth/6, displayHeight/3])

# Loop to play the game.
def gameLoop():

    # Initiates gameOver to be false.
    gameOver = False

    # Setting all the movement directions to be false.
    left = False
    right = False
    up = False
    down = False

    # declaring endGame to be the global variable.
    global endGame

    # Creating the list to hold all the snakes blocks.
    snakeList = []

    # Initilizing the snake to be size 1.
    snakeLength = 1

    # Setting the initial posision to be the middle of the screen.
    # hx is the x position of the head of the snake, hy is for the y.
    hx = displayWidth / 2
    hy = displayHeight / 2

    # Initilizing the change in x and y to 0.
    dx = 0
    dy = 0

    # Placing the first piece of food at a random spot on the game board.
    foodx = round(random.randrange(0, (displayWidth - snakeBlock * 2)) / 10.0) * 10.0
    foody = round(random.randrange(0, (displayHeight - snakeBlock * 2)) / 10.0) * 10.0

    # While the player hasn't lost and the window hasn't been closed, play the game.
    while not gameOver and endGame == False:

        # Getting and checking all the game events.
        for event in pygame.event.get():

            # If the X on the window is clicked, stop the game.
            if event.type == pygame.QUIT:
                gameOver = True
                endGame = True

            # Getting input from the arrow keys to change direction.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and right != True:
                    left = True
                    right = False
                    up = False
                    down = False
                elif event.key == pygame.K_RIGHT and left != True:
                    left = False
                    right = True
                    up = False
                    down = False
                elif event.key == pygame.K_UP and down != True:
                    left = False
                    right = False
                    up = True
                    down = False
                elif event.key == pygame.K_DOWN and up != True:
                    left = False
                    right = False
                    up = False
                    down = True

            # Changing the x or y of the snake based on which direction it is going.
            if left:
                dx = -snakeSpeed
                dy = 0
            elif right:
                dx = snakeSpeed
                dy = 0
            elif up:
                dx = 0
                dy = -snakeSpeed
            elif down:
                dx = 0
                dy = snakeSpeed

        # Stop the game if the snake goes outside the bounds of the screen.
        if hx >= displayWidth or hx < 0 or hy >= displayHeight or hy < 0:
                gameOver = True

        # Updating the current location of the snake.
        hx += dx
        hy += dy

        # Clear the screen.
        dis.fill(black)

        # Making the snake.
        snakeHead = []
        snakeHead.append(hx)
        snakeHead.append(hy)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        # Checking if the snake is touching itself.
        for x in snakeList[:-1]:
            if x == snakeHead:
                gameOver = True

        # Drawing the snake and the score on the screen.
        mySnake(snakeBlock, snakeList)
        score(snakeLength - 1)

        # If the food is eaten, place another randomly, increment the snakes length.
        if hx == foodx and hy == foody:
            foodx = round(random.randrange(0, (displayWidth - snakeBlock * 2)) / 10.0) * 10.0
            foody = round(random.randrange(0, (displayHeight - snakeBlock * 2)) / 10.0) * 10.0
            snakeLength += 1

        # Drawing the food on the screen.
        pygame.draw.rect(dis, green, [foodx, foody, snakeBlock, snakeBlock])

        # Updating the display window.
        pygame.display.update()

        # Setting the frame rate.
        clock.tick(clockSpeed)



if __name__ == "__main__":

    # Running the main menu.
    menu()
    dis.fill(black)

    # Displaying game instructions if the window has not been closed.
    if endGame == False:
        message("You are the white dot, the green dot is food.", white)
        pygame.display.update()
        time.sleep(3)
        dis.fill(black)
        message("Use the arrow keys to move, press one to start moving.", white)
        pygame.display.update()
        time.sleep(3)

    # Playing the game.
    gameLoop()
    dis.fill(black)

    # Play the game if the player wants to play again.
    while endGame == False:

        # Display "You lost" message.
        message("You Lost! Press C to Play again, Press Q to Quit", red)
        pygame.display.update()

        # Find out if the player wants to play again or not.
        for event in pygame.event.get():

            # If window is closed, end the game.
            if event.type == pygame.QUIT:
                endGame = True
            if event.type == pygame.KEYDOWN:

                # If they don't want to play the game again, end the game.
                if event.key == pygame.K_q or event.type == pygame.QUIT:
                    endGame = True
                
                # If they do, ask for difficulty level and play again.
                if event.key == pygame.K_c:
                    menu()
                    gameLoop()
                    dis.fill(black)

    # Stop the game and quit at the end.
    pygame.quit()
    quit()