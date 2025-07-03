from codeJ.Player import Player
from codeJ.Backgroud import Background
from codeJ.Const import WIN_HEIGHT, WIN_WIDTH


class EntityFactory:
    
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case '0.png':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'{i}', (0, 0)))
                    list_bg.append(Background(f'{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10, WIN_HEIGHT - 260))
            case 'Player2':
                return Player('Player2',(10, WIN_HEIGHT - 130))
