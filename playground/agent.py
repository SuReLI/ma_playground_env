import numpy as np


class Agent:
    """
        Represents an agent in the environment of PLAYGROUND.
        In PLAYGROUND, an agent is simply a collection of some attributes:
            a unique integer id
            a position:                    2-uple in 2D space.
            a gripper state:               whether the agent is grasping or not.
            a change flag for the gripper: whether the state of the gripper
                                         changed.
            a flag that tells whether the agent is grasping something or not.
            a flag that tells the nature of the object being grasped.
            some colors.
    """

    def __init__(self, id):
        self.id: int = id
        self.pos: np.ndarray = np.empty((2,))
        self.gripper: int = -1
        self.gripper_change: bool = False
        self.grasping: bool = False
        self.obj_grasped: str = ''
        self.color_idle: tuple[int, int, int, int] = (-1, -1, -1, -1)
        self.color_grip: tuple[int, int, int, int] = (-1, -1, -1, -1)

    def grip(self) -> bool:
        return self.gripper > 0
