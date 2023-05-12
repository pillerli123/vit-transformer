# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# Difficulty extra apples associated code and highscores added by Neonzz
# http://inventwithpython.com/pygame
# Creative Commons BY-NC-SA 3.0 US
# I'm looking for people to join me and make this clone have the best features!

import random, pygame, sys, time, pickle, os
from tkinter import messagebox
from pygame.locals import *
from operator import itemgetter

FPS = 60
MENUFPS = 15
drawHighApple = float(10)
drawSuperHighApple = float(40)
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)
#               R    G    B
WHITE       = (255, 255, 255)
BLACK       = ( 0,    0,   0)
RED         = (255,   0,   0)
YELLOW      = (255, 255,   0)
GREEN       = (  0, 255,   0)
GRAY        = (185, 185, 185)
BLUE        = (  0,   0, 255)
NAVYBLUE    = ( 60,  60, 100)
ORANGE      = (255, 128,   0)
PURPLE      = (170,   0, 255)
CYAN        = (  0, 255, 255)
LIGHTRED    = (175,  20,  20)
LIGHTGREEN  = ( 20, 175,  20)
LIGHTBLUE   = ( 20,  20, 175)
LIGHTYELLOW = (175, 175,  20)
DARKGREEN   = (  0, 155,   0)
DARKGRAY    = ( 40,  40,  40)
ALICEBLUE   = (240, 248, 255)
AQUA        = (0, 255, 255)
AZURE1      = (240, 255, 255)
AZURE2      = (224, 238, 238)
AZURE3      = (193, 205, 205)
AZURE4      = (131, 139, 139)
BANANA      = (227, 207, 87)
BEIGE       = (245, 245, 220)
ALMOND      = (255, 235, 205)
ROYALBLUE   = (0, 0, 238)
BLUEVIOLET  = (138, 43, 226)
BRICK       = (156, 102, 31)
BROWN       = (165, 42, 42)
BROWN1      = (255, 64, 64)
BROWN2      = (238, 59, 59)
BURLYWOOD   = (222, 184, 135)
CARROT      = (237, 145, 33)
CHARTREUSE1 = (127, 255, 0)
COBALT      = (61, 89, 171)
COBALTGREEN = (61, 145, 64)
COLDGREY    = (128, 138, 135)
CORAL       = (255, 127, 80)
CORAL1      = (255, 114, 86)
CORAL2      = (238, 106, 80)
CORNSILK    = (255, 248, 220)
CRIMSON     = (220, 20, 60)
CYAN2       = (0, 238, 238)
CYAN3       = (0, 205, 205)
CYAN4       = (0, 139, 139)
DARKGREEN   = (0, 100, 0)
DARKVIOLET  = (148, 0, 211)
DEEPPINK1   = (255, 20, 147)
DEEPPINK2   = (238, 18, 137)
EGGSHELL    = (252, 230, 201)
EMERALD     = (0, 201, 87)
FIREBRICK   = (178, 34, 34)
FIREBRICK1  = (255, 48, 48)
FIREBRICK2  = (238, 44, 44)
FLESH       = (255, 125, 64)
FLORALWHITE = (255, 250, 240)
FORESTGREEN = (34, 139, 34)
GAINSBORO   = (220, 220, 220)
GHOSTWHITE  = (248, 248, 255)
GOLD1       = (255, 215, 0)
GOLD2       = (238, 201, 0)
GOLDENROD   = (218, 165, 32)
GOLDENROD1  = (255, 193, 37)
GOLDENROD2  = (238, 180, 34)
GRAY7       = (18, 18, 18)
GRAY89      = (227, 227, 227)
GRAY9       = (23, 23, 23)
GRAY90      = (229, 229, 229)
GREEN1      = (0, 255, 0)
GREEN2      = (0, 238, 0)
HONEYDEW1   = (240, 255, 240)
HONEYDEW2   = (224, 238, 224)
INDIGO      = (75, 0, 130)
IVORY1      = (255, 255, 240)
IVORY2      = (238, 238, 224)
IVORYBLACK  = (41, 36, 33)
KHAKI       = (240, 230, 140)
KHAKI1      = (255, 246, 143)
KHAKI2      = (238, 230, 133)
LAVENDER    = (230, 230, 250)
LAWNGREEN   = (124, 252, 0)
LIGHTBLUE   = (173, 216, 230)
LIMEGREEN   = (50, 205, 50)
LINEN       = (250, 240, 230)
MAGENTA     = (255, 0, 255)
MAGENTA2    = (238, 0, 238)
MAROON      = (128, 0, 0)
MAROON1     = (255, 52, 179)
MAROON2     = (238, 48, 167)
MELON       = (227, 168, 105)
MINT        = (189, 252, 201)
MOCCASIN    = (255, 228, 181)
NAVY        = (0, 0, 128)
OLDLACE     = (253, 245, 230)
OLIVE       = (128, 128, 0)
OLIVEDRAB   = (107, 142, 35)
OLIVEDRAB1  = (192, 255, 62)
ORCHID      = (218, 112, 214)
ORCHID1     = (255, 131, 250)
ORCHID2     = (238, 122, 233)
PALEGREEN   = (152, 251, 152)
PEACOCK     = (51, 161, 201)
PINK        = (255, 192, 203)
PINK1       = (255, 181, 197)
POWDERBLUE  = (176, 224, 230)
PURPLE1     = (155, 48, 255)
PURPLE2     = (145, 44, 238)
RASPBERRY   = (135, 38, 87)
RAWSIENNA   = (199, 97, 20)
RED3        = (205, 0, 0)
RED4        = (139, 0, 0)
ROSYBROWN   = (188, 143, 143)
ROSYBROWN1  = (255, 193, 193)
ROSYBROWN   = (238, 180, 180)
ROYALBLUE   = (65, 105, 225)
ROYALBLUE1  = (72, 118, 255)
ROYALROYALBLUE  = (67, 110, 238)
SALMON      = (250, 128, 114)
SALMON1     = (255, 140, 105)
SALMON2     = (238, 130, 98)
SANDYBROWN  = (244, 164, 96)
SAPGREEN    = (48, 128, 20)
SEAGREEN1   = (84, 255, 159)
SEAGREEN2   = (78, 238, 148)
SEPIA       = (94, 38, 18)
SGIDARKGRAY = (85, 85, 85)
SIENNA      = (160, 82, 45)
SIENNA1     = (255, 130, 71)
SIENNA2     = (238, 121, 66)
SILVER      = (192, 192, 192)
SKYBLUE     = (135, 206, 235)
SKYBLUE1    = (135, 206, 255)
SKYROYALBLUE    = (126, 192, 238)
SLATEBLUE   = (106, 90, 205)
SLATEGRAY   = (112, 128, 144)
SNOW1       = (255, 250, 250)
SNOW2       = (238, 233, 233)
SPRINGGREEN = (0, 255, 127)
STEELBLUE   = (70, 130, 180)
STEELBLUE1  = (99, 184, 255)
STEELROYALBLUE  = (92, 172, 238)
TAN         = (210, 180, 140)
TAN1        = (255, 165, 79)
TAN2        = (238, 154, 73)
TEAL        = (0, 128, 128)
THISTLE     = (216, 191, 216)
THISTLE1    = (255, 225, 255)
THISTLE2    = (238, 210, 238)
TOMATO1     = (255, 99, 71)
TOMATO2     = (238, 92, 66)
TURQUOISE   = (64, 224, 208)
TURQUOISE1  = (0, 245, 255)
TURQUOISE2  = (0, 229, 238)
VIOLET      = (238, 130, 238)
VIOLETRED   = (208, 32, 144)
VIOLETRED1  = (255, 62, 150)
VIOLETRED2  = (238, 58, 140)
WARMGREY    = (128, 128, 105)
WHEAT       = (245, 222, 179)
YELLOW1     = (255, 255, 0)
YELLOW2     = (238, 238, 0)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
worm_color_inside = input('Inside WormColor:')
worm_color_outside = input('Outside WormColor:')
HEAD = 0
player_name = input('Name: ')
high_score = 0
file_name = 'highscore.neonzz'
file_name2 = 'easyhighscore.neonzz'
file_name3 = 'hardhighscore.neonzz'
file_name4 = 'insanehighscore.neonzz'

def main():
    noSelection = True
    easySelection = False
    normalSelection = False
    hardSelection = False
    insaneSelection = False
    
    global FPSCLOCK, DISPLAYSURF, BASICFONT, EASY_SURF, EASY_RECT, NORMAL_SURF, NORMAL_RECT, HARD_SURF, HARD_RECT, INSANE_SURF, INSANE_RECT, HIGHSCORE_SURF, HIGHSCORE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    # add game levels 
    EASY_SURF = BASICFONT.render('Easy mode', True, GREEN)
    EASY_RECT = EASY_SURF.get_rect()
    EASY_RECT.bottomright = (WINDOWWIDTH - 30, WINDOWHEIGHT - 90)
    
    NORMAL_SURF = BASICFONT.render('Normal Mode', True, YELLOW)
    NORMAL_RECT = NORMAL_SURF.get_rect()
    NORMAL_RECT.bottomright = (WINDOWWIDTH - 30, WINDOWHEIGHT - 60)
    
    HARD_SURF = BASICFONT.render('Hard Mode', True, ORANGE)
    HARD_RECT = HARD_SURF.get_rect()
    HARD_RECT.bottomright = (WINDOWWIDTH - 30, WINDOWHEIGHT - 30)
    
    INSANE_SURF = BASICFONT.render('Insane Mode', True, RED)
    INSANE_RECT = INSANE_SURF.get_rect()
    INSANE_RECT.bottomright = (WINDOWWIDTH - 30, WINDOWHEIGHT - 10)
    HIGHSCORE_SURF = BASICFONT.render('High Scores', True, LIGHTGREEN)
    HIGHSCORE_RECT = HIGHSCORE_SURF.get_rect()
    HIGHSCORE_RECT.bottomright = (WINDOWWIDTH - 500, WINDOWHEIGHT - 30)
    newWallColour = BLUE
    pygame.display.set_caption('Worms')
    get_high_scores(file_name)
    get_high_scores2(file_name2)
    get_high_scores3(file_name3)
    get_high_scores4(file_name4)

    showStartScreen()
    mousex = 0
    mousey = 0
    
    while True:
        noSelection = True
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                
        if EASY_RECT.collidepoint( (mousex, mousey) ):
            easySelection = True
            noSelection = False
        elif NORMAL_RECT.collidepoint( (mousex, mousey) ):
            normalSelection = True
            noSelection = False
        elif HARD_RECT.collidepoint( (mousex, mousey) ):
            hardSelection = True
            noSelection = False
        elif INSANE_RECT.collidepoint( (mousex, mousey) ):
            insaneSelection = True
            noSelection = False
        
        if noSelection == True:
            runGame()
            showGameOverScreen()

def runGame():
    # Sets a random start point.
    startx = int(5)
    starty = int(5)
    wallsx = int(19)
    wallsy = int(12)
    wallsx2 = int(9)
    wallsy2 = int(10)
    wallsx3 = int(17)
    wallsy3 = int(17)
    wallsx4 = int(4)
    wallsy4 = int(18)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y':  starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    change_to = direction
    wallCoords = [{'x': wallsx,      'y': wallsy},
                  {'x': wallsx,      'y': wallsy + 1},
                  {'x': wallsx,      'y': wallsy + 2}]
    wallCoords2 = [{'x': wallsx2,    'y': wallsy2 },
                   {'x': wallsx2,    'y': wallsy2 + 1},
                   {'x': wallsx2,    'y': wallsy2 + 2},
                   {'x': wallsx2 + 1, 'y': wallsy2 },
                   {'x': wallsx2 + 1, 'y': wallsy2 + 2 }]
    all_Walls = wallCoords + wallCoords2

    # Start the apple in a random place.
    apple = getRandomLocation()
    highValueApple = getRandomLocation()
    superHighValueApple = getRandomLocation()

    lastHighValueApple = time.time()
    lastSuperHighApple = time.time()

    HIGH_SCORE_FILE = 'highscore.neonzz'
    score = int(0)
    run_once = False
    while True: # main game loop

        if highValueApple == False:
            # No high value apple
            highValueApple = getRandomLocation()
            lastHighValueApple = time.time()
        if superHighValueApple == False:
            #No super high value apple
            superHighValueApple = getRandomLocation()
            lastSuperHighApple = time.time()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itsself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            high_score = score
            set_high_score(HIGH_SCORE_FILE, player_name, high_score)
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                high_score = score
                set_high_score(HIGH_SCORE_FILE, player_name, high_score)
                return        
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worms tal segment
            score += 1
            apple = getRandomLocation()
        elif wormCoords[HEAD]['x']  == highValueApple['x'] and wormCoords[HEAD]['y'] == highValueApple['y']:
            if time.time() - lastHighValueApple > drawHighApple:
                lastHighValueApple = time.time() # Resets lastHighValueApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 2
                highValueApple = getRandomLocation()
            else:
                score = score
        elif wormCoords[HEAD]['x'] == superHighValueApple['x'] and wormCoords[HEAD]['y'] == superHighValueApple['y']:
            if time.time() - lastSuperHighApple > drawSuperHighApple:
                lastSuperHighApple = time.time() #resets lastSuperHighApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 5
                superHighValueApple = getRandomLocation()
            else:
                score = score
        else:
            del wormCoords[-1] # remove worms tail segment

                # move the worm by adding segment in direction it is moving
        if direction == UP:
            pygame.time.delay(100)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            pygame.time.delay(100)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            pygame.time.delay(100)
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            pygame.time.delay(100)
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid() 
        for coord in wormCoords:
            x = coord['x'] * CELLSIZE
            y = coord['y'] * CELLSIZE
            wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
            pygame.draw.rect(DISPLAYSURF, worm_color_outside, wormSegmentRect)
            wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
            pygame.draw.rect(DISPLAYSURF, worm_color_inside, wormInnerSegmentRect)
        
        for pscore in range(score):
            pscore = score
            for walls in all_Walls[0:]:
                if walls['x'] == apple['x'] and walls['y'] == apple['y']:
                    apple = getRandomLocation()
                    drawApple(apple)
                if walls['x'] == highValueApple['x'] and walls['y'] == highValueApple['y']:
                    highValueApple = getRandomLocation()
                    drawHighValueApple(highValueApple)
                if walls['x'] == superHighValueApple['x'] and walls['y'] == superHighValueApple['y']:
                    superHighValueApple = getRandomLocation()
                    drawSuperHighValueApple(superHighValueApple)
            if pscore >= int(10):
                global newWallColour
                newWallColour = BLUE
                drawWall(all_Walls[0:3])
                for walls in all_Walls[0:3]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE, player_name, high_score)
                        return
            if pscore >= int(20):
                newWallColour = GREEN
                drawWall(all_Walls[3:8])
                for walls in all_Walls[3:8]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE, player_name, high_score)
                        return
            if pscore >= int(30):
                newWallColour = YELLOW
                wallCoords3 = [{'x': wallsx3, 'y': wallsy3},
                               {'x': wallsx3, 'y': wallsy3 + 1},
                               {'x': wallsx3, 'y': wallsy3 + 2}]
                all_Walls = wallCoords + wallCoords2 + wallCoords3
                drawWall(all_Walls[8:11])
                for walls in all_Walls[8:11]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE, player_name, high_score)
                        return
            if pscore >= (50):
                newWallColour = ROYALBLUE
                wallCoords4 = [{'x': wallsx4,    'y': wallsy4 },
                               {'x': wallsx4,    'y': wallsy4 + 1},
                               {'x': wallsx4,    'y': wallsy4 + 2},
                               {'x': wallsx4 + 1, 'y': wallsy4 },
                               {'x': wallsx4 + 1, 'y': wallsy4 + 2 }]
                all_Walls = all_Walls + wallCoords4
                if run_once == True:
                    new_AllWalls = all_Walls[0:16]
                    all_Walls = new_AllWalls
                    drawWall(all_Walls[11:16])
                    for walls in all_Walls[11:16]:
                        if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                            high_score = score
                            set_high_score(HIGH_SCORE_FILE, player_name, high_score)
                            return
                run_once = True                        
        if time.time() - lastHighValueApple > drawHighApple:
            drawHighValueApple(highValueApple)
        drawApple(apple)
        if time.time() - lastSuperHighApple > drawSuperHighApple:
            drawSuperHighValueApple(superHighValueApple)
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def easyMode():
    # Sets a random start point.
    startx = int(5)
    starty = int(5)
    wallsx = int(19)
    wallsy = int(12)
    wallsx2 = int(9)
    wallsy2 = int(10)
    wallsx3 = int(11)
    wallsy3 = int(17)
    wallsx4 = int(4)
    wallsy4 = int(18)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y':  starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    wallCoords = [{'x': wallsx,      'y': wallsy},
                  {'x': wallsx,      'y': wallsy + 1},
                  {'x': wallsx,      'y': wallsy + 2}]
    wallCoords2 = [{'x': wallsx2,    'y': wallsy2 },
                   {'x': wallsx2,    'y': wallsy2 + 1},
                   {'x': wallsx2,    'y': wallsy2 + 2},
                   {'x': wallsx2 + 1, 'y': wallsy2 },
                   {'x': wallsx2 + 1, 'y': wallsy2 + 2 }]
    all_Walls = wallCoords + wallCoords2

    # Start the apple in a random place.
    apple = getRandomLocation()
    highValueApple = getRandomLocation()
    superHighValueApple = getRandomLocation()

    lastHighValueApple = time.time()
    lastSuperHighApple = time.time()

    HIGH_SCORE_FILE2 = 'easyhighscore.neonzz'
    score = int(0)
    while True: # main game loop

        if highValueApple == False:
            # No high value apple
            highValueApple = getRandomLocation()
            lastHighValueApple = time.time()
        if superHighValueApple == False:
            #No super high value apple
            superHighValueApple = getRandomLocation()
            lastSuperHighApple = time.time()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itsself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            high_score = score
            set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                high_score = score
                set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
                return
        #Wall logic & spawning
        
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worms tal segment
            score += 1
            apple = getRandomLocation()
        elif wormCoords[HEAD]['x']  == highValueApple['x'] and wormCoords[HEAD]['y'] == highValueApple['y']:
            if time.time() - lastHighValueApple > drawHighApple:
                lastHighValueApple = time.time() # Resets lastHighValueApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 2
                highValueApple = getRandomLocation()
            else:
                score = score
        elif wormCoords[HEAD]['x'] == superHighValueApple['x'] and wormCoords[HEAD]['y'] == superHighValueApple['y']:
            if time.time() - lastSuperHighApple > drawSuperHighApple:
                lastSuperHighApple = time.time() #resets lastSuperHighApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 5
                superHighValueApple = getRandomLocation()
            else:
                score = score
        else:
            del wormCoords[-1] # remove worms tail segment

                # move the worm by adding segment in direction it is moving
        if direction == UP:
            pygame.time.delay(200)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            pygame.time.delay(200)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            pygame.time.delay(200)
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            pygame.time.delay(200)
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid() 
        drawWorm(wormCoords)
        for pscore in range(score):
            pscore = score
            for walls in all_Walls[0:]:
                if walls['x'] == apple['x'] and walls['y'] == apple['y']:
                    apple = getRandomLocation()
                    drawApple(apple)
                if walls['x'] == highValueApple['x'] and walls['y'] == highValueApple['y']:
                    highValueApple = getRandomLocation()
                    drawHighValueApple(highValueApple)
                if walls['x'] == superHighValueApple['x'] and walls['y'] == superHighValueApple['y']:
                    superHighValueApple = getRandomLocation()
                    drawSuperHighValueApple(superHighValueApple)
            if pscore >= int(10):
                global newWallColour
                newWallColour = BLUE
                drawWall(all_Walls[0:3])
                for walls in all_Walls[0:3]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
                        return
            if pscore >= int(20):
                newWallColour = GREEN
                drawWall(all_Walls[3:8])
                for walls in all_Walls[3:8]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
                        return
            if pscore >= int(30):
                newWallColour = YELLOW
                wallCoords3 = [{'x': wallsx3, 'y': wallsy3},
                               {'x': wallsx3 + 1, 'y': wallsy3},
                               {'x': wallsx3 + 2, 'y': wallsy3}]
                all_Walls = wallCoords + wallCoords2 + wallCoords3
                drawWall(all_Walls[8:11])
                for walls in all_Walls[8:11]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
                        return
            if pscore >= (50):
                newWallColour = ROYALBLUE
                wallCoords4 = [{'x': wallsx4,    'y': wallsy4 },
                               {'x': wallsx4,    'y': wallsy4 + 1},
                               {'x': wallsx4,    'y': wallsy4 + 2},
                               {'x': wallsx4 + 1, 'y': wallsy4 },
                               {'x': wallsx4 + 1, 'y': wallsy4 + 2 }]
                all_Walls = all_Walls + wallCoords4
                if run_once == True: #Below required or wallcoords4 is constantly added to all_Walls
                    new_AllWalls = all_Walls[0:16]
                    all_Walls = new_AllWalls
                    drawWall(all_Walls[11:16])
                    for walls in all_Walls[11:16]:
                        if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                            high_score = score
                            set_high_score(HIGH_SCORE_FILE2, player_name, high_score)
                            return
                run_once = True                        
        if time.time() - lastHighValueApple > drawHighApple:
            drawHighValueApple(highValueApple)
        drawApple(apple)
        if time.time() - lastSuperHighApple > drawSuperHighApple:
            drawSuperHighValueApple(superHighValueApple)
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def hardMode():
    # Sets a random start point.
    startx = int(5)
    starty = int(5)
    wallsx = int(19)
    wallsy = int(12)
    wallsx2 = int(9)
    wallsy2 = int(10)
    wallsx3 = int(17)
    wallsy3 = int(17)
    wallsx4 = int(4)
    wallsy4 = int(18)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y':  starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    wallCoords = [{'x': wallsx,      'y': wallsy},
                  {'x': wallsx,      'y': wallsy + 1},
                  {'x': wallsx,      'y': wallsy + 2}]
    wallCoords2 = [{'x': wallsx2,    'y': wallsy2 },
                   {'x': wallsx2,    'y': wallsy2 + 1},
                   {'x': wallsx2,    'y': wallsy2 + 2},
                   {'x': wallsx2 + 1, 'y': wallsy2 },
                   {'x': wallsx2 + 1, 'y': wallsy2 + 2 }]
    all_Walls = wallCoords + wallCoords2

    # Start the apple in a random place.
    apple = getRandomLocation()
    highValueApple = getRandomLocation()
    superHighValueApple = getRandomLocation()

    lastHighValueApple = time.time()
    lastSuperHighApple = time.time()

    HIGH_SCORE_FILE3 = 'hardhighscore.neonzz'
    score = int(0)
    while True: # main game loop

        if highValueApple == False:
            # No high value apple
            highValueApple = getRandomLocation()
            lastHighValueApple = time.time()
        if superHighValueApple == False:
            #No super high value apple
            superHighValueApple = getRandomLocation()
            lastSuperHighApple = time.time()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itsself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            high_score = score
            set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                high_score = score
                set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
                return
        #Wall logic & spawning
        
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worms tal segment
            score += 1
            apple = getRandomLocation()
        elif wormCoords[HEAD]['x']  == highValueApple['x'] and wormCoords[HEAD]['y'] == highValueApple['y']:
            if time.time() - lastHighValueApple > drawHighApple:
                lastHighValueApple = time.time() # Resets lastHighValueApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 2
                highValueApple = getRandomLocation()
            else:
                score = score
        elif wormCoords[HEAD]['x'] == superHighValueApple['x'] and wormCoords[HEAD]['y'] == superHighValueApple['y']:
            if time.time() - lastSuperHighApple > drawSuperHighApple:
                lastSuperHighApple = time.time() #resets lastSuperHighApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 5
                superHighValueApple = getRandomLocation()
            else:
                score = score
        else:
            del wormCoords[-1] # remove worms tail segment

                # move the worm by adding segment in direction it is moving
        if direction == UP:
            pygame.time.delay(50)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            pygame.time.delay(50)
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            pygame.time.delay(50)
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            pygame.time.delay(50)
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid() 
        drawWorm(wormCoords)
        run_once = True
        for pscore in range(score):
            pscore = score
            for walls in all_Walls[0:]:
                if walls['x'] == apple['x'] and walls['y'] == apple['y']:
                    apple = getRandomLocation()
                    drawApple(apple)
                if walls['x'] == highValueApple['x'] and walls['y'] == highValueApple['y']:
                    highValueApple = getRandomLocation()
                    drawHighValueApple(highValueApple)
                if walls['x'] == superHighValueApple['x'] and walls['y'] == superHighValueApple['y']:
                    superHighValueApple = getRandomLocation()
                    drawSuperHighValueApple(superHighValueApple)
            if pscore >= int(10):
                global newWallColour
                newWallColour = BLUE
                drawWall(all_Walls[0:3])
                for walls in all_Walls[0:3]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
                        return
            if pscore >= int(20):
                newWallColour = GREEN
                drawWall(all_Walls[3:8])
                for walls in all_Walls[3:8]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
                        return
            if pscore >= int(30):
                newWallColour = YELLOW
                wallCoords3 = [{'x': wallsx3, 'y': wallsy3},
                               {'x': wallsx3 + 1, 'y': wallsy3},
                               {'x': wallsx3 + 2, 'y': wallsy3}]
                all_Walls = wallCoords + wallCoords2 + wallCoords3
                drawWall(all_Walls[8:11])
                for walls in all_Walls[8:11]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
                        return
            if pscore >= (50):
                newWallColour = ROYALBLUE
                wallCoords4 = [{'x': wallsx4,    'y': wallsy4 },
                               {'x': wallsx4,    'y': wallsy4 + 1},
                               {'x': wallsx4,    'y': wallsy4 + 2},
                               {'x': wallsx4 + 1, 'y': wallsy4 },
                               {'x': wallsx4 + 1, 'y': wallsy4 + 2 }]
                all_Walls = all_Walls + wallCoords4
                if run_once == True: #Below required or wallcoords4 is constantly added to all_Walls
                    new_AllWalls = all_Walls[0:16]
                    all_Walls = new_AllWalls
                    drawWall(all_Walls[11:16])
                    for walls in all_Walls[11:16]:
                        if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                            high_score = score
                            set_high_score(HIGH_SCORE_FILE3, player_name, high_score)
                            return
                run_once = True                        
        if time.time() - lastHighValueApple > drawHighApple:
            drawHighValueApple(highValueApple)
        drawApple(apple)
        if time.time() - lastSuperHighApple > drawSuperHighApple:
            drawSuperHighValueApple(superHighValueApple)
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def insaneMode():
    # Sets a random start point.
    startx = int(5)
    starty = int(5)
    wallsx = int(19)
    wallsy = int(12)
    wallsx2 = int(9)
    wallsy2 = int(10)
    wallsx3 = int(17)
    wallsy3 = int(17)
    wallsx4 = int(4)
    wallsy4 = int(18)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y':  starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    wallCoords = [{'x': wallsx,      'y': wallsy},
                  {'x': wallsx,      'y': wallsy + 1},
                  {'x': wallsx,      'y': wallsy + 2}]
    wallCoords2 = [{'x': wallsx2,    'y': wallsy2 },
                   {'x': wallsx2,    'y': wallsy2 + 1},
                   {'x': wallsx2,    'y': wallsy2 + 2},
                   {'x': wallsx2 + 1, 'y': wallsy2 },
                   {'x': wallsx2 + 1, 'y': wallsy2 + 2 }]
    all_Walls = wallCoords + wallCoords2

    # Start the apple in a random place.
    apple = getRandomLocation()
    highValueApple = getRandomLocation()
    superHighValueApple = getRandomLocation()

    lastHighValueApple = time.time()
    lastSuperHighApple = time.time()

    HIGH_SCORE_FILE4 = 'insanehighscore.neonzz'
    score = int(0)
    while True: # main game loop

        if highValueApple == False:
            # No high value apple
            highValueApple = getRandomLocation()
            lastHighValueApple = time.time()
        if superHighValueApple == False:
            #No super high value apple
            superHighValueApple = getRandomLocation()
            lastSuperHighApple = time.time()
            
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit itsself or the edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            high_score = score
            set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
            return
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                high_score = score
                set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
                return
        #Wall logic & spawning
        
        # check if worm has eaten an apply
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worms tal segment
            score += 1
            apple = getRandomLocation()
        elif wormCoords[HEAD]['x']  == highValueApple['x'] and wormCoords[HEAD]['y'] == highValueApple['y']:
            if time.time() - lastHighValueApple > drawHighApple:
                lastHighValueApple = time.time() # Resets lastHighValueApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 2
                highValueApple = getRandomLocation()
            else:
                score = score
        elif wormCoords[HEAD]['x'] == superHighValueApple['x'] and wormCoords[HEAD]['y'] == superHighValueApple['y']:
            if time.time() - lastSuperHighApple > drawSuperHighApple:
                lastSuperHighApple = time.time() #resets lastSuperHighApple  (IMPORTANT if you want to keep the draw delay after eating an apple)
                score += 5
                superHighValueApple = getRandomLocation()
            else:
                score = score
        else:
            del wormCoords[-1] # remove worms tail segment

                # move the worm by adding segment in direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)
        
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid() 
        drawWorm(wormCoords)
        for pscore in range(score):
            pscore = score
            for walls in all_Walls[0:]:
                if walls['x'] == apple['x'] and walls['y'] == apple['y']:
                    apple = getRandomLocation()
                    drawApple(apple)
                if walls['x'] == highValueApple['x'] and walls['y'] == highValueApple['y']:
                    highValueApple = getRandomLocation()
                    drawHighValueApple(highValueApple)
                if walls['x'] == superHighValueApple['x'] and walls['y'] == superHighValueApple['y']:
                    superHighValueApple = getRandomLocation()
                    drawSuperHighValueApple(superHighValueApple)
            if pscore >= int(10):
                global newWallColour
                newWallColour = BLUE
                drawWall(all_Walls[0:3])
                for walls in all_Walls[0:3]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
                        return
            if pscore >= int(20):
                newWallColour = GREEN
                drawWall(all_Walls[3:8])
                for walls in all_Walls[3:8]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
                        return
            if pscore >= int(30):
                newWallColour = YELLOW
                wallCoords3 = [{'x': wallsx3, 'y': wallsy3},
                               {'x': wallsx3 + 1, 'y': wallsy3},
                               {'x': wallsx3 + 2, 'y': wallsy3}]
                all_Walls = wallCoords + wallCoords2 + wallCoords3
                drawWall(all_Walls[8:11])
                for walls in all_Walls[8:11]:
                    if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                        high_score = score
                        set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
                        return
            if pscore >= (50):
                newWallColour = ROYALBLUE
                wallCoords4 = [{'x': wallsx4,    'y': wallsy4 },
                               {'x': wallsx4,    'y': wallsy4 + 1},
                               {'x': wallsx4,    'y': wallsy4 + 2},
                               {'x': wallsx4 + 1, 'y': wallsy4 },
                               {'x': wallsx4 + 1, 'y': wallsy4 + 2 }]
                all_Walls = all_Walls + wallCoords4
                if run_once == True: #Below required or wallcoords4 is constantly added to all_Walls
                    new_AllWalls = all_Walls[0:16]
                    all_Walls = new_AllWalls
                    drawWall(all_Walls[11:16])
                    for walls in all_Walls[11:16]:
                        if walls['x'] == wormCoords[HEAD]['x'] and walls['y'] == wormCoords[HEAD]['y']:
                            high_score = score
                            set_high_score(HIGH_SCORE_FILE4, player_name, high_score)
                            return
                run_once = True                        
        if time.time() - lastHighValueApple > drawHighApple:
            drawHighValueApple(highValueApple)
        drawApple(apple)
        if time.time() - lastSuperHighApple > drawSuperHighApple:
            drawSuperHighValueApple(superHighValueApple)
        drawScore(score)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawPressKeyMsg1():
    pressKeySurf = BASICFONT.render('select your difficulty to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomleft = (WINDOWWIDTH - 450, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def drawPressKeyMsg2():
    pressKeySurf = BASICFONT.render('Press a Key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (WINDOWWIDTH - 20, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def drawPressKeyMsg3():
    pressKeySurf = BASICFONT.render('Press a key to return to the main menu', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.bottomright = (WINDOWWIDTH - 20, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    elif keyUpEvents[0].key == K_q:
        showStartScreen()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    mousex = 0
    mousey = 0

    degrees1 = 0
    degrees2 = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if EASY_RECT.collidepoint( (mousex, mousey) ):
                    easyMode()
                    showGameOverScreen()
                elif NORMAL_RECT.collidepoint( (mousex, mousey) ):
                    runGame()
                    showGameOverScreen()
                elif HARD_RECT.collidepoint( (mousex, mousey) ):
                    hardMode()
                    showGameOverScreen()
                elif INSANE_RECT.collidepoint( (mousex, mousey) ):
                    insaneMode()
                    showGameOverScreen()
                elif HIGHSCORE_RECT.collidepoint( (mousex, mousey) ):
                    high_Scores()
                    
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg1()
        drawPressKeyMsg2()

        DISPLAYSURF.blit(EASY_SURF, EASY_RECT)
        DISPLAYSURF.blit(NORMAL_SURF, NORMAL_RECT)
        DISPLAYSURF.blit(HARD_SURF, HARD_RECT)
        DISPLAYSURF.blit(INSANE_SURF, INSANE_RECT)
        DISPLAYSURF.blit(HIGHSCORE_SURF, HIGHSCORE_RECT)

        if checkForKeyPress():
            pygame.event.get() #clear event que
            return
        pygame.display.update()
        FPSCLOCK.tick(MENUFPS)
        degrees1 += 3
        degrees2 += 7


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0,
CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    drawPressKeyMsg3()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress()

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, worm_color_outside, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, worm_color_inside, wormInnerSegmentRect)

def drawWall(wallCoords):
    for coord in wallCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wallSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, newWallColour, wallSegmentRect)
        wallInnerRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF, newWallColour, wallInnerRect)

def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = (x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawHighValueApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    highValueAppleRect = (x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, GREEN, highValueAppleRect)
    highValueInnerAppleRect = pygame.Rect(x + 2, y + 2, CELLSIZE - 10, CELLSIZE - 10)
    pygame.draw.rect(DISPLAYSURF, RED, highValueInnerAppleRect)


def drawSuperHighValueApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    superHighValueAppleRect = (x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, CYAN, superHighValueAppleRect)
    superHighValueInnerAppleRect = pygame.Rect(x + 3, y + 3, CELLSIZE - 10, CELLSIZE - 10)
    pygame.draw.rect(DISPLAYSURF, LIGHTGREEN, superHighValueInnerAppleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


def high_Scores():
    DISPLAYSURF.fill(BGCOLOR)
    
    scores = get_high_scores(file_name) #Get the high scores as a dictionary
    bigfont = pygame.font.Font('freesansbold.ttf', 36)
    #Draw the title
    highScoreText = bigfont.render("HIGH SCORES", 1, GREEN) #Create the text
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.midtop = (WINDOWWIDTH / 2, 10)
    firstfont = pygame.font.Font('freesansbold.ttf', 30)
    easyHighScore = firstfont.render('Easy HS', 1, GREEN)
    easyHighScoreRect = easyHighScore.get_rect()
    easyHighScoreRect. midtop = (60, 100)
    normalHighScore = firstfont.render('Normal HS', 2, GREEN)
    normalHighScoreRect = normalHighScore.get_rect()
    normalHighScoreRect.midtop = (210, 100)
    hardHighScore = firstfont.render('Hard HS', 3, GREEN)
    hardHighScoreRect = hardHighScore.get_rect()
    hardHighScoreRect.midtop = (360, 100)
    insaneHighScore = firstfont.render('Insane HS', 4, GREEN)
    insaneHighScoreRect = insaneHighScore.get_rect()
    insaneHighScoreRect.midtop = (500, 100)
    DISPLAYSURF.blit(highScoreText, highScoreTextRect)
    DISPLAYSURF.blit(easyHighScore, easyHighScoreRect)
    DISPLAYSURF.blit(normalHighScore, normalHighScoreRect)
    DISPLAYSURF.blit(hardHighScore, hardHighScoreRect)
    DISPLAYSURF.blit(insaneHighScore, insaneHighScoreRect)
    drawPressKeyMsg3()
    checkForKeyPress()
    pygame.display.update()
    pygame.time.wait(500)
    mousex = 0
    mousey = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if easyHighScoreRect.collidepoint( (mousex, mousey) ):
                    easy_high_scores()
                elif normalHighScoreRect.collidepoint( (mousex, mousey) ):
                    normal_high_scores()
                elif hardHighScoreRect.collidepoint( (mousex, mousey) ):
                    hard_high_scores()
                elif insaneHighScoreRect.collidepoint( (mousex, mousey) ):
                   insane_high_scores()
        if checkForKeyPress():
            pygame.event.get() #clear event que
            return


def easy_high_scores():
    DISPLAYSURF.fill(BGCOLOR)
    firstfont = pygame.font.Font('freesansbold.ttf', 30)
    bigfont = pygame.font.Font('freesansbold.ttf', 36)
    #Draw the title
    highScoreText = bigfont.render("EASY HIGH SCORES", 1, GREEN) #Create the text
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.midtop = (WINDOWWIDTH / 2, 10)
    
    scores = get_high_scores2(file_name2)
    firstscoretext = firstfont.render("1st: " + scores.get('high')[0] + " - " + scores.get('high')[1], 1, GREEN) #Create the text
    firstscoretextrect = firstscoretext.get_rect()
    firstscoretextrect.midtop = (WINDOWWIDTH / 2, firstscoretextrect.height + 10 + 25)
    #draw the next highest score
    secondfont = pygame.font.Font('freesansbold.ttf', 26)
    secondscoretext = secondfont.render("2nd: " + scores.get('mid')[0] + " - " + scores.get('mid')[1], 1, GREEN) #Create the text
    secondscoretextrect = secondscoretext.get_rect()
    secondscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 40 + 35)
    thirdfont = pygame.font.Font('freesansbold.ttf', 20)
    thirdscoretext = thirdfont.render("3rd: " + scores.get('low')[0] + " - " + scores.get('low')[1], 1, GREEN) #Create the text
    thirdscoretextrect = thirdscoretext.get_rect()
    thirdscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 80 + 35)
    DISPLAYSURF.blit(firstscoretext, firstscoretextrect)
    DISPLAYSURF.blit(secondscoretext, secondscoretextrect)
    DISPLAYSURF.blit(thirdscoretext, thirdscoretextrect)
    DISPLAYSURF.blit(highScoreText, highScoreTextRect)
    pygame.display.update()


def normal_high_scores():
    DISPLAYSURF.fill(BGCOLOR)
    firstfont = pygame.font.Font('freesansbold.ttf', 30)
    bigfont = pygame.font.Font('freesansbold.ttf', 36)
    #Draw the title
    highScoreText = bigfont.render("NORMAL HIGH SCORES", 1, GREEN) #Create the text
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.midtop = (WINDOWWIDTH / 2, 10)
    
    scores = get_high_scores(file_name)
    firstscoretext = firstfont.render("1st: " + scores.get('high')[0] + " - " + scores.get('high')[1], 1, GREEN) #Create the text
    firstscoretextrect = firstscoretext.get_rect()
    firstscoretextrect.midtop = (WINDOWWIDTH / 2, firstscoretextrect.height + 10 + 25)
    #draw the next highest score
    secondfont = pygame.font.Font('freesansbold.ttf', 26)
    secondscoretext = secondfont.render("2nd: " + scores.get('mid')[0] + " - " + scores.get('mid')[1], 1, GREEN) #Create the text
    secondscoretextrect = secondscoretext.get_rect()
    secondscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 40 + 35)
    thirdfont = pygame.font.Font('freesansbold.ttf', 20)
    thirdscoretext = thirdfont.render("3rd: " + scores.get('low')[0] + " - " + scores.get('low')[1], 1, GREEN) #Create the text
    thirdscoretextrect = thirdscoretext.get_rect()
    thirdscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 80 + 35)
    DISPLAYSURF.blit(firstscoretext, firstscoretextrect)
    DISPLAYSURF.blit(secondscoretext, secondscoretextrect)
    DISPLAYSURF.blit(thirdscoretext, thirdscoretextrect)
    DISPLAYSURF.blit(highScoreText, highScoreTextRect)
    pygame.display.update()


def hard_high_scores():
    DISPLAYSURF.fill(BGCOLOR)
    firstfont = pygame.font.Font('freesansbold.ttf', 30)
    bigfont = pygame.font.Font('freesansbold.ttf', 36)
    #Draw the title
    highScoreText = bigfont.render("HARD HIGH SCORES", 1, GREEN) #Create the text
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.midtop = (WINDOWWIDTH / 2, 10)
    
    scores = get_high_scores3(file_name3)
    firstscoretext = firstfont.render("1st: " + scores.get('high')[0] + " - " + scores.get('high')[1], 1, GREEN) #Create the text
    firstscoretextrect = firstscoretext.get_rect()
    firstscoretextrect.midtop = (WINDOWWIDTH / 2, firstscoretextrect.height + 10 + 25)
    #draw the next highest score
    secondfont = pygame.font.Font('freesansbold.ttf', 26)
    secondscoretext = secondfont.render("2nd: " + scores.get('mid')[0] + " - " + scores.get('mid')[1], 1, GREEN) #Create the text
    secondscoretextrect = secondscoretext.get_rect()
    secondscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 40 + 35)
    thirdfont = pygame.font.Font('freesansbold.ttf', 20)
    thirdscoretext = thirdfont.render("3rd: " + scores.get('low')[0] + " - " + scores.get('low')[1], 1, GREEN) #Create the text
    thirdscoretextrect = thirdscoretext.get_rect()
    thirdscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 80 + 35)
    DISPLAYSURF.blit(firstscoretext, firstscoretextrect)
    DISPLAYSURF.blit(secondscoretext, secondscoretextrect)
    DISPLAYSURF.blit(thirdscoretext, thirdscoretextrect)
    DISPLAYSURF.blit(highScoreText, highScoreTextRect)
    pygame.display.update()


def insane_high_scores():
    DISPLAYSURF.fill(BGCOLOR)
    firstfont = pygame.font.Font('freesansbold.ttf', 30)
    bigfont = pygame.font.Font('freesansbold.ttf', 36)
    #Draw the title
    highScoreText = bigfont.render("INSANE HIGH SCORES", 1, GREEN) #Create the text
    highScoreTextRect = highScoreText.get_rect()
    highScoreTextRect.midtop = (WINDOWWIDTH / 2, 10)
    
    scores = get_high_scores4(file_name4)
    firstscoretext = firstfont.render("1st: " + scores.get('high')[0] + " - " + scores.get('high')[1], 1, GREEN) #Create the text
    firstscoretextrect = firstscoretext.get_rect()
    firstscoretextrect.midtop = (WINDOWWIDTH / 2, firstscoretextrect.height + 10 + 25)
    #draw the next highest score
    secondfont = pygame.font.Font('freesansbold.ttf', 26)
    secondscoretext = secondfont.render("2nd: " + scores.get('mid')[0] + " - " + scores.get('mid')[1], 1, GREEN) #Create the text
    secondscoretextrect = secondscoretext.get_rect()
    secondscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 40 + 35)
    thirdfont = pygame.font.Font('freesansbold.ttf', 20)
    thirdscoretext = thirdfont.render("3rd: " + scores.get('low')[0] + " - " + scores.get('low')[1], 1, GREEN) #Create the text
    thirdscoretextrect = thirdscoretext.get_rect()
    thirdscoretextrect.midtop = (WINDOWWIDTH / 2, secondscoretextrect.height + 80 + 35)
    DISPLAYSURF.blit(firstscoretext, firstscoretextrect)
    DISPLAYSURF.blit(secondscoretext, secondscoretextrect)
    DISPLAYSURF.blit(thirdscoretext, thirdscoretextrect)
    DISPLAYSURF.blit(highScoreText, highScoreTextRect)
    pygame.display.update()
    
  
def get_high_scores(file_name):
    content = "" #Used to store content from the file

    #Check if the file exists, if it does exist...
    if os.path.isfile(file_name):
        #We open the file and save its contents to the content variable
        #When we open a file using with, the file is automatically closed after we
        #are finished, so we don't need to wory about closing it. If you're not accessing
        #a file in this way, you must remember to close it after use
        with open(file_name, 'r') as content_file:
            content = content_file.read()
    #If it doesn't exist, we create the file and populate it with default values
    else:
        f = open(file_name, 'w')
        content = "high::0,mid::0,low::0" #We also set content with the default values to avoid any errors in future code
        f.write(content) #write the contents to file
        f.close() #close the file
        

    content_list = content.split(',') #Split the content into different parts by splitting at every ','

    to_return = {} #create an empty dictionary that will be populated and then returned

    for element in content_list: #For each element in list 
        l = element.split(':') #Split the element into the title name and score sections, which are stored as a list in the variable l
        #use the first variable in the list l as the key in the dictionary to_return, which references a 
        #list containing the second and third values
        to_return[l[0]] = [l[1], l[2]] 

    return to_return #return the dictionary

#writes the high scores out to the high score file, taking the score dictionary and file_name as input


def get_high_scores2(file_name2):
    content = ""

    if os.path.isfile(file_name2):
        with open(file_name2, 'r') as content_file:
            content = content_file.read()

    else:
        f = open(file_name2, 'w')
        content = "high::0,mid::0,low::0"
        f.write(content)
        f.close()

    content_list = content.split(",")

    to_return = {}

    for element in content_list:
        l = element.split(":")
        to_return[l[0]] = [l[1], l[2]]

    return to_return


def get_high_scores3(file_name3):
    content = ""

    if os.path.isfile(file_name3):
        with open(file_name2, 'r') as content_file:
            content = content_file.read()

    else:
        f = open(file_name3, 'w')
        content = "high::0,mid::0,low::0"
        f.write(content)
        f.close()

    content_list = content.split(",")

    to_return = {}

    for element in content_list:
        l = element.split(":")
        to_return[l[0]] = [l[1], l[2]]  

    return to_return


def get_high_scores4(file_name4):
    content = ""

    if os.path.isfile(file_name4):
        with open(file_name2, 'r') as content_file:
            content = content_file.read()

    else:
        f = open(file_name4, 'w')
        content = "high::0,mid::0,low::0"
        f.write(content)
        f.close()

    content_list = content.split(",")

    to_return = {}

    for element in content_list:
        l = element.split(":")
        to_return[l[0]] = [l[1], l[2]]

    return to_return
        

def write_high_scores(file_name, scores):
    f = open(file_name, 'w') #open the file for writing
    to_write = "" #create an empty string to store the data we will write to our file
    #cycle through the different scores, writing the values in the correct format and adding them to the string 
    for name in ('high', 'mid', 'low'): 
        to_write += name
        to_write += ':'
        to_write += str(scores.get(name)[0])
        to_write += ':'
        to_write += str(scores.get(name)[1])
        to_write += ','

    print(to_write)
    to_write = to_write[:-1] #Remove the last character from the two_write string - this is an unnecessary comma created by our loop
    f.write(to_write) #write the string to the file
    f.close() #close the file

#Updates the high score file with a new score, placing it in the relevant location (i.e. highest, next highest etc.)
#Depending on the score
def set_high_score(file_name, player_name, score):
    scores = get_high_scores(file_name) #get a dictionary of the current high scores

    #If we have a new high score, update the values in the dictionary
    if (int(score) >= int(scores.get('high')[1])): 
        scores['high'][0] = player_name
        scores['high'][1] = score
    #Else if we have a new next highest score, update this value
    elif (int(score) >= int(scores.get('mid')[1])):
        scores['mid'][0] = player_name
        scores['mid'][1] = score
    #Else if our score is lower than anyone elses, update this value.
    elif (int(score) >= int(scores.get('low')[1])):
        scores['low'][0] = player_name
        scores['low'][1] = score

    write_high_scores(file_name, scores)
    print(scores)
    pygame.display.update()


def set_high_score2(file_name2, player_name, score):
    scores = get_high_scores2(file_name2) #get a dictionary of the current high scores

    #If we have a new high score, update the values in the dictionary
    if (int(score) >= int(scores.get('high')[1])): 
        scores['high'][0] = player_name
        scores['high'][1] = score
    #Else if we have a new next highest score, update this value
    elif (int(score) >= int(scores.get('mid')[1])):
        scores['mid'][0] = player_name
        scores['mid'][1] = score
    #Else if our score is lower than anyone elses, update this value.
    elif (int(score) >= int(scores.get('low')[1])):
        scores['low'][0] = player_name
        scores['low'][1] = score

    write_high_scores(file_name2, scores)
    print(scores)
    pygame.display.update()


def set_high_score3(file_name3, player_name, score):
    scores = get_high_scores3(file_name3) #get a dictionary of the current high scores

    #If we have a new high score, update the values in the dictionary
    if (int(score) >= int(scores.get('high')[1])): 
        scores['high'][0] = player_name
        scores['high'][1] = score
    #Else if we have a new next highest score, update this value
    elif (int(score) >= int(scores.get('mid')[1])):
        scores['mid'][0] = player_name
        scores['mid'][1] = score
    #Else if our score is lower than anyone elses, update this value.
    elif (int(score) >= int(scores.get('low')[1])):
        scores['low'][0] = player_name
        scores['low'][1] = score

    write_high_scores(file_name3, scores)
    print(scores)
    pygame.display.update()


def set_high_score4(file_name4, player_name, score):
    scores = get_high_scores4(file_name4) #get a dictionary of the current high scores

    #If we have a new high score, update the values in the dictionary
    if (int(score) >= int(scores.get('high')[1])): 
        scores['high'][0] = player_name
        scores['high'][1] = score
    #Else if we have a new next highest score, update this value
    elif (int(score) >= int(scores.get('mid')[1])):
        scores['mid'][0] = player_name
        scores['mid'][1] = score
    #Else if our score is lower than anyone elses, update this value.
    elif (int(score) >= int(scores.get('low')[1])):
        scores['low'][0] = player_name
        scores['low'][1] = score

    write_high_scores(file_name4, scores)
    print(scores)
    pygame.display.update()


if __name__ == '__main__':
    main()
