import numpy as np


class Agent:
    """
        Represents an agent in the environment of PLAYGROUND.
        In PLAYGROUND, an agent is simply a collection of some attributes:
          a position:                    2-uple in 2D space.
          a gripper state:               whether the agent is grasping or not.
          a change flag for the gripper: whether the state of the gripper
                                         changed.
    """

    def __init__(self):
        self.pos: np.ndarray = np.empty((2,))
        self.gripper: int = -1
        self.gripper_change: bool = False
        self.color_idle: tuple[int, int, int, int] = (-1, -1, -1, -1)
        self.color_grip: tuple[int, int, int, int] = (-1, -1, -1, -1)
