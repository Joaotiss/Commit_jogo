from pygame import Rect, Surface
from pygame.font import Font
import pygame.image

from codeJ.Const import COLOR_BLACK, COLOR_RED, MENU_OPTION, WIN_WIDTH

class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("asset/login.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
         menu_option = 0
         pygame.mixer_music.load('asset/813150__mikeysaints__130bpm-kick-drum.wav')
         pygame.mixer_music.play(-1)

         while True:
             self.window.blit(source=self.surf, dest=self.rect)
             self.menu_text( text_size=70, text='Phantom', text_color=COLOR_RED, text_center_pos=((WIN_WIDTH // 2), 70))
             self.menu_text( text_size=70, text='Attack', text_color=COLOR_RED, text_center_pos=((WIN_WIDTH // 2), 120))

             for i in range(len(MENU_OPTION)):
                 if i == menu_option:
                   self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_RED, text_center_pos=((WIN_WIDTH // 2), 200 + (i * 25)))
                 else:
                   self.menu_text(text_size=22, text=MENU_OPTION[i], text_color=COLOR_BLACK, text_center_pos=((WIN_WIDTH // 2), 200 + (i * 25)))
                    



             pygame.display.flip()
             
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     quit()

                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                       if menu_option < len(MENU_OPTION) - 1:
                          menu_option += 1
                       else:
                          menu_option = 0

                    if event.key == pygame.K_UP:
                       if menu_option > 0:
                           menu_option -= 1
                       else:
                           menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
     text_font: Font = pygame.font.SysFont(name="Courier New", size=text_size, bold=True)
     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
     self.window.blit(source=text_surf, dest=text_rect)