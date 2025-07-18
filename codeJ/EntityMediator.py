from codeJ.Const import WIN_WIDTH, WIN_HEIGHT
from codeJ.Entity import Entity
from codeJ.Enemy import Enemy
from codeJ.Player import Player
from codeJ.PlayerShot import PlayerShot
from codeJ.EnemyShot import EnemyShot


class EntityMediator:

 @staticmethod
 def __verify_collision_window(ent: Entity):
    if isinstance(ent, Enemy):
        if ent.rect.right <= 0:
            ent.health = 0
    
 @staticmethod
 def __verify_collision_entity(ent1, ent2):
     valid_interaction = False
     if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
        valid_interaction = True
     elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
        valid_interaction = True
     elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
        valid_interaction = True
     elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
        valid_interaction = True

     if valid_interaction:
        if (ent1.rect.right >= ent2.rect.left and
             ent1.rect.left <= ent2.rect.right and
             ent1.rect.bottom >= ent2.rect.top and
             ent1.rect.top <= ent2.rect.bottom): 
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage
            ent1.last_dmg = ent2.name
            ent2.last_dmg = ent1.name
            


 @staticmethod
 def verify_collision(Entity_list: list[Entity]):
    for i in range(len(Entity_list)):
        entity1 = Entity_list[i]
        EntityMediator.__verify_collision_window(entity1)
        for j in range(i + 1,len(Entity_list)):
         entity2 = Entity_list[j]
         EntityMediator.__verify_collision_entity(entity1, entity2)


 @staticmethod
 def verify_health(Entity_list: list[Entity]):
    for ent in Entity_list:
       if ent.health <= 0:
           Entity_list.remove(ent)
           