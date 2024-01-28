import pygame, random, math, sys

#initilialize the game
pygame.init()

#create the screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("First Level")

#create background
background = pygame.image.load("skeldmap.jpg")
background_with_walls = pygame.image.load("walloverlay.png").convert_alpha()  # Load wall image with alpha channel
defaultMapSize = (800,600)
mapImage = pygame.transform.scale(background,defaultMapSize)
wallImage = pygame.transform.scale(background_with_walls,defaultMapSize)

# Determine the valid spawn area based on the walls' positions and dimensions
valid_spawn_area = []

#title and icon
pygame.display.set_caption("Suspicious Activity")
icon = pygame.image.load('cyber-security.png')
pygame.display.set_icon(icon)

x = 0
y = 0

#player
#use playerX = random.randint(50,150) for randomized placement - numbers are based on screen display size.

playerImg = pygame.image.load("sus.png")
defaultPlayerSize = (24,24)
playerimage = pygame.transform.scale(playerImg,defaultPlayerSize)
playerX = random.randint(50,250)
playerY = random.randint(300,520)
playerX_change = 0
playerY_change = 0

# playerImg2 = pygame.image.load("sus.png")
# defaultPlayerSize = (64,64)
# playerimage2 = pygame.transform.scale(playerImg2,defaultPlayerSize)
# playerX2 = random.randint(50,250)
# playerY2 = random.randint(300,520)
# playerX_change2 = 0
# playerY_change2 = 0

# playerImg3 = pygame.image.load("sus.png")
# defaultPlayerSize = (64,64)
# playerimage3 = pygame.transform.scale(playerImg3,defaultPlayerSize)
# playerX3 = random.randint(50,250)
# playerY3 = random.randint(300,520)
# playerX_change3 = 0
# playerY_change3 = 0

# playerImg4 = pygame.image.load("sus.png")
# defaultPlayerSize = (64,64)
# playerimage4 = pygame.transform.scale(playerImg4,defaultPlayerSize)
# playerX4 = random.randint(50,250)
# playerY4 = random.randint(300,520)
# playerX_change4 = 0
# playerY_change4 = 0

enemyImg = pygame.image.load("us.png")
defaultPlayerSize = (32,32)
enemyimage = pygame.transform.scale(enemyImg,defaultPlayerSize)
enemyX = random.randint(50,250)
enemyY = random.randint(300,520)
enemyX_change = 0
enemyY_change = 0


# Randomly select a spawn position until a suitable one is found
player_spawned = False
while not player_spawned:
    playerX = random.randint(50, 250)  # Modify these values based on your desired spawn area
    playerY = random.randint(300, 520)  # Modify these values based on your desired spawn area

    # Check if the player's spawn position overlaps with any wall
    #player_rect = pygame.Rect(playerX, playerY, playerimage.get_width(), playerimage.get_height())
    rect = pygame.Rect(playerX, playerY, playerimage.get_width(), playerimage.get_height())
    overlapping = any(rect.colliderect(area) for area in valid_spawn_area)

    # If no overlapping occurs, the player can spawn at that position
    if not overlapping:
        player_spawned = True

# clock = pygame.time.Clock()

# Function to check collision with walls
def wall_collision(player_x, player_y):
    # Define a smaller rectangle around the player's position to check for collision
    player_rect = pygame.Rect(player_x, player_y + 20, playerimage.get_width() -10, playerimage.get_height()-5)
    
    # Check if any black pixel is present within the defined rectangle
    for area in valid_spawn_area:
        if player_rect.colliderect(area):
            return True  # Collision detected

    return False  # No collision

def player(x,y):
    screen.blit(playerimage,(x,y))

# def player2(x,y):
#     screen.blit(playerimage2,(x,y))
# def player3(x,y):
#     screen.blit(playerimage3,(x,y))
# def player4(x,y):
#     screen.blit(playerimage4,(x,y))

def enemy(x,y):
    screen.blit(enemyimage,(x,y))

### fix this when the enemy weapon is defined
# def isCollision(enemyX,enemyY):
#     distance = math.sqrt((math.pow(enemyX-enemyY,2)) + (math.pow(enemyY-enemyX,2)))
#     if distance < 1: #
#         return True
#     else:
#         return False

#game loop
running = True
while running:

    # RGB only if background image not used
    screen.fill((0, 0, 255))
    # Background Image
    screen.blit(mapImage, (0,0))

    # Create a new surface to blit the image at the new position
    new_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
    new_surface.blit(wallImage, (0,-20))
    screen.blit(new_surface, (0,0))

    # Clear the valid_spawn_area list to recompute it in each iteration
    valid_spawn_area.clear()

    # Iterate through the wallImage to find black pixels (walls) and add corresponding rectangles to valid_spawn_area
    for y_wall in range(wallImage.get_height()):
        for x_wall in range(wallImage.get_width()):
            pixel_color = wallImage.get_at((x_wall, y_wall))
            if pixel_color[0] == 0 and pixel_color[1] == 0 and pixel_color[2] == 0:  # Black pixel
                valid_spawn_area.append(pygame.Rect(x_wall, y_wall, 1, 1))



    # automatic velocity
    # playerX -= 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check if keystroke is left key or right key
        if event.type == pygame.KEYDOWN:
            # print("A key has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("Right arrow is pressed")
            if event.key == pygame.K_UP:
                playerY_change -= 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("Up arrow is pressed")
            if event.key == pygame.K_DOWN:
                playerY_change += 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("Down arrow is pressed")
            if event.key == pygame.K_a:
                playerX_change = -10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("a key is pressed")
            if event.key == pygame.K_d:
                playerX_change = 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("d key is pressed")
            if event.key == pygame.K_w:
                playerY_change -= 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerY += playerX_change
                # print("w key is pressed")
            if event.key == pygame.K_s:
                playerY_change += 10
                if not wall_collision(playerX + playerX_change, playerY):
                    playerX += playerX_change
                # print("s key is pressed")
            elif event.key == ord('q'):
                pygame.quit(); sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or \
                event.key == pygame.K_RIGHT or \
                event.key == pygame.K_UP or \
                event.key == pygame.K_DOWN or \
                event.key == pygame.K_a or \
                event.key == pygame.K_d or \
                event.key == pygame.K_s or \
                event.key == pygame.K_w:
                    playerX_change = 0
                    playerY_change = 0
                    # print("Key has been released")

        # pygame.display.flip()
    
    keys = pygame.key.get_pressed() 

    # player coordinate 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # player coordinate 5 = 5 + 0.1 -> 5 = 5 + 0.1
    playerY += playerY_change
    playerX += playerX_change
    # playerX2 += playerX_change2
    # playerX3 += playerX_change3
    # playerX4 += playerX_change4
    enemyX += enemyX_change
    
    # Check collision with walls after updating player position
    if wall_collision(playerX, playerY):
        # Revert player position to previous position to avoid collision
        playerX -= playerX_change
        playerY -= playerY_change

    # Ensure player stays within screen bounds
    playerX = max(0, min(playerX, 736))  # Adjust bounds according to your screen size
    playerY = max(0, min(playerY, 536))  # Adjust bounds according to your screen size


    # Collision
    ### fix this when enemy weapon is defined.
    #collision = isCollision(enemyX,enemyY)
    #if collision:    

    player(playerX,playerY)
    # player2(playerX2,playerY2)
    # player3(playerX3,playerY3)
    # player4(playerX4,playerY4)
    enemy(enemyX,enemyY)
    pygame.display.update()
    # clock.tick(60)