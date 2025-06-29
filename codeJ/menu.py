from pygame import Rect, Surface
from pygame.font import Font
import pygame.image

from codeJ.Const import COLOR_BLACK, COLOR_ORANGE, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/login.png")
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
         pygame.mixer_music.load('asset/813150__mikeysaints__130bpm-kick-drum.wav')
         pygame.mixer_music.play(-1)

         while True:
             self.window.blit(source=self.surf, dest=self.rect)
             self.menu_text( text_size=50, text='MONTAIN', text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH // 2), 70))
             self.menu_text( text_size=50, text='HIGHSCORE', text_color=COLOR_ORANGE, text_center_pos=((WIN_WIDTH // 2), 120))

             for i in range(len(MENU_OPTION)):
                 self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH // 2), 200 + (i * 27)))

             pygame.display.flip()
             
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
     text_font: Font = pygame.font.SysFont(name="Impact", size=text_size)
     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
     self.window.blit(source=text_surf, dest=text_rect)