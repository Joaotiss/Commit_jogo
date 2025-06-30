import pygame
from codeJ.Menu import Menu
from codeJ.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    
    def run(self):
       
        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                pass
            elif menu_return == MENU_OPTION[4]:
               pygame.quit()
               quit()
            else: 
                pass   




           
            