# Modules
import pygame
from pygame.locals import *

pygame.init()

# Screen variables
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

# Variables
line_width = 6
symbols = []
clicked = False
pos = []
player = 1
winner = 0
tier = 0
tie = False
game_over = False
count = 0

# colours:
red = (255, 0, 0)
black = (0, 0, 0)
chalk_white = (251, 247, 245)
chalkboard = (8, 0, 52)

# Font
font = pygame.font.SysFont(None, 40)

# Rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)


# functions

def draw_grid():
    bg = (8, 0, 52)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
        pygame.draw.line(screen, grid, (x * 100, 0), (x * 100, screen_height), line_width)


for x in range(3):
    row = [0] * 3
    symbols.append(row)


def draw_symbols():
    global count
    x_pos = 0
    for x in symbols:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, chalk_white, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, chalk_white, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, chalk_white, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in symbols:
        # Check cols
        if sum(x) == 3:
            winner = 'Crosses'
            game_over = True
        if sum(x) == -3:
            winner = 'Circles'
            game_over = True
        # Check rows
        if symbols[0][y_pos] + symbols[1][y_pos] + symbols[2][y_pos] == 3:
            winner = 'Crosses'
            game_over = True
        if symbols[0][y_pos] + symbols[1][y_pos] + symbols[2][y_pos] == -3:
            winner = 'Circles'
            game_over = True
        y_pos += 1
    # Check diagonal
    if symbols[0][0] + symbols[1][1] + symbols[2][2] == 3 or symbols[2][0] + symbols[1][1] + symbols[0][2] == 3:
        winner = 'Crosses'
        game_over = True
    if symbols[0][0] + symbols[1][1] + symbols[2][2] == -3 or symbols[2][0] + symbols[1][1] + symbols[0][2] == -3:
        winner = 'Circles'
        game_over = True


def check_tie():
    global count
    global tie
    if count == 9:
        tie = True


def draw_winner(winner):
    win_text = winner + " wins!"
    win_img = font.render(win_text, True, red)
    pygame.draw.rect(screen, chalkboard, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = '   Restart?'
    again_img = font.render(again_text, True, red)
    pygame.draw.rect(screen, chalkboard, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


def draw_tie():
    tie_text = '    It is a tie!'
    tie_img = font.render(tie_text, True, red)
    pygame.draw.rect(screen, chalkboard, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(tie_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = '   Restart?'
    again_img = font.render(again_text, True, red)
    pygame.draw.rect(screen, chalkboard, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


run = True
while run:

    draw_grid()
    draw_symbols()

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0 and tie == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if symbols[cell_x // 100][cell_y // 100] == 0:
                    symbols[cell_x // 100][cell_y // 100] = player
                    count += 1
                    player *= -1
                    check_winner()
                    check_tie()

    if game_over == True:
        draw_winner(winner)
        # check for mouse click to see if user has clicked on play again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                symbols = []
                pos = []
                player = 1
                count = 0
                winner = 0
                tie = False
                game_over = False
                for x in range(3):
                    row = [0] * 3
                    symbols.append(row)
    if tie == True:
        draw_tie()
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # reset variables
                symbols = []
                pos = []
                player = 1
                count = 0
                winner = 0
                game_over = False
                tie = False
                for x in range(3):
                    row = [0] * 3
                    symbols.append(row)


    pygame.display.update()

pygame.quit()
