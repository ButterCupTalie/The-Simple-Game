
# This is a simple game created with pygame in which a player (picture of a player is a picture of my husband
# who hates vegetables and loves meat :) is able to move around the screen by using the up, down, left and right arrows.
# There are three enemies, which are angry vegetables that all move across the screen from different positions.
# If the player collides with any angry vegetable player loses the game and the game ends.
# Game has one ‘prize’ object which is a happy steak.
# If the player collides with the happy steak player wins, and the game ends.


import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 


# Initialize the pygame modules to get everything started.

pygame.init()

# Creates the screen and gives it the width and height specified as a 2 item sequence.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

# This creates the player, enemies and the prize and gives it the images found in this folder.

player = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy1.jpg")
enemy2 = pygame.image.load("enemy2.jpg")
enemy3 = pygame.image.load("enemy3.jpg")
prize = pygame.image.load("prize.jpg")

# Width and height of the images in order to do boundary detection

image_height = player.get_height()
image_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player, enemies and the prize as variables. 

playerXPosition = 100
playerYPosition = 50

# Enemies start off screen and at a random y position.

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, 460) 

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, 460)
while (enemy2YPosition == enemy1YPosition):
    enemy2Yposition = random.randint(0, 460)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, 460)
while (enemy3YPosition == enemy1YPosition) or (enemy3YPosition == enemy2YPosition):
    enemy3Yposition = random.randint(0, 460)

prizeXPosition =  screen_width
prizeYPosition =  random.randint(540, 660 - prize_height)

# This checks if the up, down, left or right key is pressed.


keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop. To represent real time game play the screen window is refreshed/updated and changes applied.

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting).
   

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position. 
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition > 0 : # This makes sure that the user does not move the player off the screen on the left.
            playerXPosition -= 1
    if keyRight == True:
        if playerXPosition < screen_width - image_width: # This makes sure that the user does not move the player off the screen on the right.
            playerXPosition += 1
    
    # Check for collision of the enemies and prize with the player with bounding boxes around the images of the player, enemies and prize.
    # Test if these boxes intersect, if they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemies:
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    #Bounding box for the prize:

    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
    # Test collision of the boxes:
    
    # If the player box collide with one of the enemy boxes player looses the game and game ends and loosing status is displayed.
    
    if playerBox.colliderect(enemy1Box):
        print("\n **********YOU LOSE!**********")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy2Box):
        print("\n **********YOU LOSE!**********")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(enemy3Box):
        print("\n **********YOU LOSE!**********")
        pygame.quit()
        exit(0)

    elif playerBox.colliderect(prizeBox):
        print("\n **********YOU WIN!**********")
        pygame.quit()
        exit(0)

        

    
 
    
    # Make enemies and prize approach the player.
    
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.15
    enemy3XPosition -= 0.15
    prizeXPosition -= 0.15
    

# ******References******

# Angry Broccoli Illustrations & Vectors. Retrieved 21 January 2021, from
# https://www.dreamstime.com/illustration/angry-broccoli.html

# Angry carrot. Retrieved 21 January 2021, from
# https://www.redbubble.com/i/kids-t-shirt/Lean-Mean-Full-of-Beta-
# Carotene-Angry-Carrot-Design-by-BrobocopPrime/28440515.MZ153

# Steak cartoon images. Retrieved 21 January 2021, from
# https://www.shutterstock.com/search/steak+cartoon

# Angry sweet yellow pepper in kitchen cartoon vector image. Retrieved 21 January 2021, from
# https://www.vectorstock.com/royalty-free-vector/angry-sweet-yellow-pepper-in-kitchen-cartoon-vector-22100249


  
