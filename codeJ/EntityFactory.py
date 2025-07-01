from codeJ.Backgroud import Background


class EntityFactory:
    
    
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case '1.png':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'1.png{i}', (0, 0)))
                    return list_bg
