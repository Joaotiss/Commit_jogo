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
    'Player1': 5,
    'Enemy1': 2,
    'Enemy2': 3,
    'Enemy1Shot': 4,
    'Enemy2Shot': 4,
    'Player1Shot': 5  # Velocidade do tiro do Player1
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,  # 20 ms delay for player shots
    'Enemy1': 100,  # 100 ms delay for enemy shots
    'Enemy2': 200   # 200 ms delay for enemy shots
}

ENTITY_HEALTH = {
    '0': 999,
    '1': 999,
    '2': 999,
    '3': 999,
    '4': 999,
    'Player1': 300,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Player1Shot': 100
}

ENTITY_DAMAGE = {
    '0': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    'Player1': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy1Shot': 2,
    'Enemy2Shot': 3,
    'Player1Shot': 20
}

EVENT_ENEMY = pygame.USEREVENT + 1

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