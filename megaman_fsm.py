from pygame import Vector2

from idle_state import MegamanIdleState
# from jumping_state import MegamanJumpingState
from running_state import MegamanRunningState

class MegamanFSM:

    def __init__(self):
        self.direction = 'right'
        self.pos = Vector2((100, 300))
        self.idle_state = MegamanIdleState(self)
        # self.jumping_state = MegamanJumpingState(self)
        self.running_state = MegamanRunningState(self)

        self.state = self.idle_state

    # def jump(self):
    #     self.state.jump()

    def stop(self):
        self.state.stop()

    def move(self, direction):
        self.direction = direction
        self.state.move()
