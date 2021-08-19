#Vai herdar de sprite

class MegamanJumpingState:

    def __init__(self, megaman):
        self.megaman = megaman

    def jump(self):
        print('already jumping')
        pass

    def move(self, direction):
        print(f'moving to {direction} while jumpin')
        pass

    def stop(self):
        print('stopped while jumping')
        pass