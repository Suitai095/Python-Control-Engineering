from typing import Tuple

import numpy as np
from control.matlab import tf, feedback, step


class VerticalDriveArm(object):
    
    def __init__(
        self,
        l: float = 0.2,
        M: float = 0.5,
        mu: float = 1.5e-2,
        J: float = 1.0e-2
            ) -> None:
        g = 9.81
        self.P = tf([0, 1], [J, mu, M*g*l])
    
    def motion(
        self,
        kp: float,
        T: object
            ) -> Tuple[np.array, np.array]:
        K = tf([0, kp], [0, 1])
        Gyr = feedback(K * self.P, 1)
        y, t = step(Gyr, T)
        return y, t
