#importing external packages
import sys, pygame, random
from pygame.locals import * 

#importing internal programs
import boardsD2, positionsD2, diceD2

#initializing pygame
pygame.init()

#setting up window
windowSurface = pygame.display.set_mode((1536, 793))
pygame.display.set_caption("Snakes and Ladders")

#setting up RGB colour vals
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (185, 0, 50)
GREEN = (50, 145, 25)
BLUE = (1, 130, 235)
GREY = (185, 185, 185)
VIOLET = (65, 40, 110)
ORANGE = (255, 165, 0)
BG_COLOR_AUTUMN = (125, 179, 67)
BG_COLOR_SUMMER = (255, 211, 88)
BG_COLOR_WINTER = WHITE
COLOR = BG_COLOR_AUTUMN

#setting up font
Font = pygame.font.Font('assets/game_font.otf', 50)



#misc info
dice_coordinates = (1245, 160)
turn = 1
snakes = boardsD2.snakes
ladders = boardsD2.ladders
FRAMES = 6
button_size1 = (250, 94)
button_size2 = (200, 75)
ICON_SIZE = (80, 80)
ICON_SIZE2 = (90, 90)

#setting up startscreen, dice, player icons, end screen and board images
autumnboard = pygame.image.load('assets/board_1.jpg')
summerboard = pygame.image.load('assets/board_2.jpg')
winterboard = pygame.image.load('assets/board_3.jpg')
StartScreenImg = pygame.image.load('assets/StartScreen.png')
imagelist = diceD2.images
icons_img = [pygame.image.load(f"assets/icon{i}.png") for i in range(2, 7)]
iconsImg = [pygame.transform.scale(icons_img[i], ICON_SIZE) for i in range(5)]
iconsImgRect = [iconsImg[i].get_rect() for i in range(5)]
icons_highlight_img = [pygame.image.load(f"assets/icon{i}H.png") for i in range(2, 7)]
iconsHighlight = [pygame.transform.scale(icons_highlight_img[i], ICON_SIZE2) for i in range(5)]
iconsHighlightRect = [iconsHighlight[i].get_rect() for i in range(5)]
endScreenInitial = pygame.image.load('assets/end_screen.png')
endScreen = pygame.transform.scale(endScreenInitial, (800, 600))
boardimg = autumnboard

#setting up button images
twoPlayersBtnInitial = pygame.image.load('assets/two_players.png')
twoPlayersBtn = pygame.transform.scale(twoPlayersBtnInitial, button_size1)
twoPlayersBtnRect = twoPlayersBtn.get_rect(topleft= (70, 450))
threePlayersBtnInitial = pygame.image.load('assets/three_players.png')
threePlayersBtn = pygame.transform.scale(threePlayersBtnInitial, button_size1)
threePlayersBtnRect = threePlayersBtn.get_rect(topleft= (350, 450))
fourPlayersBtnInitial = pygame.image.load('assets/four_players.png')
fourPlayersBtn = pygame.transform.scale(fourPlayersBtnInitial, button_size1)
fourPlayersBtnRect = fourPlayersBtn.get_rect(topleft= (70, 570))
fivePlayersBtnInitial = pygame.image.load('assets/five_players.png')
fivePlayersBtn = pygame.transform.scale(fivePlayersBtnInitial, button_size1)
fivePlayersBtnRect = fivePlayersBtn.get_rect(topleft= (350, 570))
autumnTheme = pygame.image.load('assets/autumn.png')
autumnThemeBtn = pygame.transform.scale(autumnTheme, button_size2)
autumnThemeBtnRect = autumnThemeBtn.get_rect(topleft= (30, 10))
summerTheme = pygame.image.load('assets/summer.png')
summerThemeBtn = pygame.transform.scale(summerTheme, button_size2)
summerThemeBtnRect = summerThemeBtn.get_rect(topleft= (250, 10))
winterTheme = pygame.image.load('assets/winter.png')
winterThemeBtn = pygame.transform.scale(winterTheme, button_size2)
winterThemeBtnRect = winterThemeBtn.get_rect(topleft= (470, 10))
highscoreBtnInitial = pygame.image.load('assets/highscores.png')
highscoreBtn = pygame.transform.scale(highscoreBtnInitial, button_size1)
endgameBtnInitial = pygame.image.load('assets/end_game.png')
endgameBtn = pygame.transform.scale(endgameBtnInitial,(420, 210))
endgameBtnRect = endgameBtn.get_rect(topleft = (1120, 550))
rollDiceBtnInitial = pygame.image.load('assets/roll_dice.png')
rollDiceBtn = pygame.transform.scale(rollDiceBtnInitial, button_size2)
rollDiceBtnRect = rollDiceBtn.get_rect(topleft=(1200, 50))
exitGameBtnInitial = pygame.image.load('assets/exit.png')
exitGameBtn = pygame.transform.scale(exitGameBtnInitial, button_size1)
exitGameBtnRect = exitGameBtn.get_rect(topright = (1025, 475))
newGameBtnInitial = pygame.image.load('assets/new_game.png')
newGameBtn = pygame.transform.scale(newGameBtnInitial, button_size1)
newGameBtnRect = newGameBtn.get_rect(topleft = (460, 475))


buttons1 = [twoPlayersBtnRect, threePlayersBtnRect, fourPlayersBtnRect, fivePlayersBtnRect, autumnThemeBtnRect, 
            summerThemeBtnRect, winterThemeBtnRect]
buttons2 = [endgameBtnRect, rollDiceBtnRect]
buttons3 = [exitGameBtnRect, newGameBtnRect]

#basic player info
numPlayers = 5
PlayerPositions = [0] * numPlayers
PlayerCoordinates = [boardsD2.cell_coords[0]] * numPlayers

#game state
game_over = 0
entered_game = 0
game = "running"
started_game = 0

#startscreen graphics
def draw_start_screen():
    windowSurface.fill(COLOR)
    
    windowSurface.blit(StartScreenImg, (0, 0))
    windowSurface.blit(twoPlayersBtn, twoPlayersBtnRect)
    windowSurface.blit(threePlayersBtn, threePlayersBtnRect)
    windowSurface.blit(fourPlayersBtn, fourPlayersBtnRect)
    windowSurface.blit(fivePlayersBtn, fivePlayersBtnRect)
    windowSurface.blit(autumnThemeBtn, autumnThemeBtnRect)
    windowSurface.blit(summerThemeBtn, summerThemeBtnRect)
    windowSurface.blit(winterThemeBtn, winterThemeBtnRect)
    pygame.display.update()

#main board graphics
def draw_main_board():
    windowSurface.fill(BG_COLOR_AUTUMN)
    windowSurface.blit(boardimg, (0, 0))
    windowSurface.blit(endgameBtn, endgameBtnRect)
    windowSurface.blit(rollDiceBtn, rollDiceBtnRect)
    pygame.display.update()

#player graphics
def draw_players(i):
    j = turn % numPlayers - 1
    if j == -1 :
        j = numPlayers - 1

    iconsImgRect[i].center = PlayerCoordinates[i]
    if i == j:
        iconsHighlightRect[i].center = PlayerCoordinates[i]
        windowSurface.blit(iconsHighlight[i], iconsHighlightRect[i])

    windowSurface.blit(iconsImg[i], iconsImgRect[i])
    pygame.display.update()

def animate(i, initial_coords, final_coords, diceroll):
    for j in range(FRAMES + 1):
        pygame.time.delay(100)
        x = initial_coords[0] + j * ((final_coords[0] - initial_coords[0]) / FRAMES)
        y = initial_coords[1] + j * ((final_coords[1] - initial_coords[1]) / FRAMES)
        PlayerCoordinates[i] = (x, y)
        draw_main_board()
        windowSurface.blit(diceD2.images[diceroll-1], dice_coordinates)
        for k in range(numPlayers):
            #if k != i:
            draw_players(k)

        #windowSurface.blit(iconsHighlight[i], iconsHighlightRect[i])
        draw_players(i)

def draw_end_screen():
    windowSurface.blit(endScreen, (350, 95))
    player_no = (turn - 1) % numPlayers
    if player_no == 0:
        player_no = numPlayers
    text = Font.render(f"GAME OVER", True, RED)
    windowSurface.blit(text, (600, 200))
    NumWords = {1 : "One", 2 : "Two", 3 : "Three", 4 : "Four", 5 : "Five"}
    text1 = Font.render(f"Player {NumWords[player_no]} has won", True, RED)
    windowSurface.blit(text1, (550, 270))
    windowSurface.blit(exitGameBtn, exitGameBtnRect)
    windowSurface.blit(newGameBtn, newGameBtnRect)
    pygame.display.update()    

#main game logic (doing rn)
def main_game():
    
    global PlayerCoordinates
    global game_over
    global PlayerPositions

    draw_main_board()
    for i in range(numPlayers):
        draw_players(i)
    diceroll = random.randint(1, 6)
    diceD2.dice_animations(diceroll, imagelist, windowSurface, dice_coordinates)

    
    i = turn % numPlayers - 1
    if i == -1:
        i = numPlayers - 1
    position = PlayerPositions[i]
    initial_coords = boardsD2.cell_coords[position]
    position1 = positionsD2.check(position, diceroll)
    final_coords = boardsD2.cell_coords[position1]
    animate(i, initial_coords, final_coords, diceroll)
    position2 = positionsD2.change(position1, snakes, ladders)
    if position1 != position2:
        initial_coords = final_coords
        final_coords = boardsD2.cell_coords[position2]
        animate(i, initial_coords, final_coords, diceroll)
    PlayerPositions[i] = position2
    PlayerCoordinates[i] = final_coords
    if 32 in PlayerPositions:
        global game_over 
        game_over = 1
        draw_start_screen()
        return




while game == "running":
    if not entered_game and not game_over:
        draw_start_screen()
        #mouse_coords = pygame.mouse.get_pos()
    
    if game_over:
        draw_end_screen()

                
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEMOTION:
            if not entered_game and not game_over:
                for ele in buttons1:
                    if ele.collidepoint(pygame.mouse.get_pos()):
                        ele.x += 8
                        ele.y += 8
                        draw_start_screen()
                        pygame.time.delay(1000)
                        ele.x -= 8
                        ele.y -= 8
            
            if game_over:
                for ele in buttons3:
                    if ele.collidepoint(pygame.mouse.get_pos()):
                        ele.x += 8
                        ele.y += 8
                        draw_end_screen()
                        pygame.time.delay(1000)
                        ele.x -= 8
                        ele.y -= 8
                
        if event.type == MOUSEBUTTONDOWN:
            #mouse_coords = pygame.mouse.get_pos()
            if game_over:
                if newGameBtnRect.collidepoint(pygame.mouse.get_pos()):
                    entered_game = 0
                    game_over = 0
                    numPlayers = 5
                    PlayerPositions = [0] * numPlayers
                    PlayerCoordinates = [boardsD2.cell_coords[0]] * numPlayers
                if exitGameBtnRect.collidepoint(pygame.mouse.get_pos()):
                    sys.exit()

            if not entered_game and not game_over:
                btn = 0
                if twoPlayersBtnRect.collidepoint(pygame.mouse.get_pos()):
                    numPlayers = 2
                    btn = 2
                    entered_game = 1
                if threePlayersBtnRect.collidepoint(pygame.mouse.get_pos()):
                    numPlayers = 3
                    btn = 3
                    entered_game = 1
                if fourPlayersBtnRect.collidepoint(pygame.mouse.get_pos()):
                    numPlayers = 4
                    btn = 4
                    entered_game = 1
                if fivePlayersBtnRect.collidepoint(pygame.mouse.get_pos()):
                    numPlayers = 5
                    btn = 5
                    entered_game = 1
                if autumnThemeBtnRect.collidepoint(pygame.mouse.get_pos()):
                    boardimg = autumnboard
                    COLOR = BG_COLOR_AUTUMN
                    draw_start_screen()
                if winterThemeBtnRect.collidepoint(pygame.mouse.get_pos()):
                    boardimg = winterboard
                    COLOR = BG_COLOR_WINTER
                    draw_start_screen()
                if summerThemeBtnRect.collidepoint(pygame.mouse.get_pos()):
                    boardimg = summerboard
                    COLOR = BG_COLOR_SUMMER
                    draw_start_screen()

            if entered_game and not game_over:
                if endgameBtnRect.collidepoint(pygame.mouse.get_pos()):
                        entered_game = 0
                        numPlayers = 5
                        PlayerPositions = [0] * numPlayers
                        PlayerCoordinates = [boardsD2.cell_coords[0]] * numPlayers

                        
                if entered_game:
                    draw_main_board()
                    for i in range(numPlayers):
                        draw_players(i)
                    pygame.display.update()

                if rollDiceBtnRect.collidepoint(pygame.mouse.get_pos()):
                    rollDiceBtnRect.x += 8
                    rollDiceBtnRect.y += 8
                    draw_main_board()
                    main_game()
                    for i in range(numPlayers):
                        draw_players(i)
                        pygame.display.update()
                    turn += 1
                    rollDiceBtnRect.x -= 8
                    rollDiceBtnRect.y -= 8
                    draw_main_board()
                    for i in range(numPlayers):
                        draw_players(i)
                        pygame.display.update()

pygame.quit()


