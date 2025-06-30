
class Entity:
    def __init__(self, name, entity_type):
        self.name = name
        self.entity_type = entity_type
        self.position = (0, 0)
        self.velocity = (0, 0)

    def move(self):
        pass
