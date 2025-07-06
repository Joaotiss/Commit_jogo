import pygame


WIN_WIDTH = 800
WIN_HEIGHT = 700

#C
COLOR_RED = (255, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

#M
MENU_OPTION = ('NEW GAME 1P',
               'SCORE',
               'EXIT')

#E
ENTITY_SPEED = {
    '0': 0,
    '1': 1,
    '2': 1,
    '3': 2,
    '4': 3,
    'Player1': 3,
    'Player2': 3
}

#P
PLAYER_KEY_UP = {
    'Player1': pygame.K_UP,
    'Player2': pygame.K_w
}
PLAYER_KEY_DOWN = {
    'Player1': pygame.K_DOWN,
    'Player2': pygame.K_s
}
PLAYER_KEY_LEFT = {
    'Player1': pygame.K_LEFT,
    'Player2': pygame.K_a
}
PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_RIGHT,
    'Player2': pygame.K_d
}
PLAYER_KEY_SHOOT = {
    'Player1': pygame.K_SPACE,
    'Player2': pygame.K_f
}