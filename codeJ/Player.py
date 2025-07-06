
import pygame
from codeJ.Const import ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
from codeJ.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.left -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.right += ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_UP[self.name]] and self.rect.top > 480:
            self.rect.top -= ENTITY_SPEED[self.name]
        if pressed_keys[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.bottom += ENTITY_SPEED[self.name]
