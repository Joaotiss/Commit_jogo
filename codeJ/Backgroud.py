from codeJ.Const import ENTITY_SPEED, WIN_WIDTH
from codeJ.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0 :
            self.rect.left = WIN_WIDTH
        pass
