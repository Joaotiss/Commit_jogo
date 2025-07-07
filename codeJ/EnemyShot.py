from codeJ.Const import ENTITY_SPEED
from codeJ.Entity import Entity 

class EnemyShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.left -= self.speed