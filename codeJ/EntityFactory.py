from codeJ.Backgroud import Background
from codeJ.Const import WIN_WIDTH


class EntityFactory:
    
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case '1.png':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'5', (0, 0)))
                    list_bg.append(Background(f'5', (WIN_WIDTH, 0)))
                return list_bg
