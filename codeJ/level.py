
import sys
import pygame
from codeJ.Const import COLOR_WHITE, MENU_OPTION, WIN_HEIGHT
from codeJ.EntityFactory import EntityFactory
from codeJ.Entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list :  list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('0.png'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000  # timeout em milissegundos (20 segundos)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

    def run(self):
        pygame.mixer_music.load('asset/813150__mikeysaints__130bpm-kick-drum.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() : 0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))  
            pygame.display.flip()
        pass 

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font = pygame.font.SysFont("Arial", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)


        