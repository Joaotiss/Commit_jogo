import pygame 

class Game:
    def __init__(self):
        self.window = None

    
    def run(self, ):
        print('Setup Start')
        pygame.init()

        window = pygame.display.set_mode(size=(800, 480))

        while True:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()