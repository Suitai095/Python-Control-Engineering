from typing import Tuple, Any
from abc import ABCMeta, abstractmethod

import numpy as np
from control.matlab import tf, feedback, step, bode, logspace
from control.matlab import lsim


class VerticalDriveArm:
    
    def set_parameter(
        self,
        kp: float,
        kd: float,
        ki: float,
        l:  float = 0.2,
        M:  float = 0.5,
        mu: float = 1.5e-2,
        J:  float = 1.0e-2
            ) -> None:
        g       = 9.81
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.P  = tf([0, 1], [J, mu, M*g*l])

    @abstractmethod
    def control_model(self) -> None:
        pass

    @abstractmethod
    def K(self) -> Any:
        pass

    @abstractmethod
    def excute_result_for_response(self) -> None:
        pass

    @abstractmethod
    def excute_result_bode_line_diagram(self) -> None:
        pass

    def bode_line_diagram(
        self, Gyr: object) -> Tuple[np.array, np.array, np.array]:
        mag, phase, omega = bode(Gyr, logspace(-1, 2, 1000), plot=False)
        return mag, phase, omega

    def Td(self, Td: np.array) -> np.array:
        return 1*(Td > 0)


class PID_control_robot(VerticalDriveArm):

    def __init__(self, kp: float, kd: float, ki: float) -> None:
        super().__init__()
        self.set_parameter(kp, kd, ki)
        self.control_model()

    def control_model(self) -> None:
        try:
            self.Gyr = feedback(self.K() * self.P, 1)
        except Exception as e:
            raise RuntimeError(f'Error of PID Control Robot: {e}')

    def K(self) -> Any:
        return tf([self.kd, self.kp, self.ki], [1, 0])

    def excute_result_for_response(
        self, Td: np.array) -> Tuple[np.array, np.array]:
        r = self.Td(Td)
        y, t, _ = lsim(self.Gyr, r, Td, 0)
        return y, t

    def excute_result_bode_line_diagram(
        self) -> Tuple[np.array, np.array, np.array]:
        return self.bode_line_diagram(self.Gyr)


class I_PD_control_robot(VerticalDriveArm):
    
    def __init__(self, kp: float, ki: float, kd: float) -> None:
        super().__init__()
        self.set_parameter(kp, kd, ki)
        self.control_model()

    def control_model(self):
        try:
            self.Gyr = feedback(self.K() * self.P, 1)
        except Exception as e:
            raise RuntimeError(f'Error of I_PD Control Robot: {e}')

    def K(self) -> Any:
        return tf([self.kd, self.kp, self.ki], [1, 0])
    
    def K2(self) -> Any:
        return tf([self.kp, self.ki], [self.kd, self.kp, self.ki])

    def excute_result_for_response(
        self, Td: np.array) -> Tuple[np.array, np.array]:
        r = self.Td(Td)
        z, t, _ = lsim(self.K2(), r, Td, 0)
        y, _, _ = lsim(self.Gyr, z, Td, 0)
        return y, t, z

    def excute_result_bode_line_diagram(
        self) -> Tuple[np.array, np.array, np.array]:
        return self.bode_line_diagram(self.Gyr)


# ----------------------------------------------------------------------------
#   Sample class.
# ----------------------------------------------------------------------------
# class VerticalDriveArm(object):
    
#     def __init__(
#         self,
#         kp: float,
#         kd: float,
#         ki: float,
#         l:  float = 0.2,
#         M:  float = 0.5,
#         mu: float = 1.5e-2,
#         J:  float = 1.0e-2
#             ) -> None:
#         g       = 9.81
#         self.kp = kp
#         self.kd = kd
#         self.ki = ki
#         self.P  = tf([0, 1], [J, mu, M*g*l])
    
#     def motion(self) -> None:
#         try:
#             K = tf([self.kd, self.kp, self.ki], [1, 0])
#             self.Gyr = feedback(K * self.P, 1)
#         except Exception as e:
#             raise RuntimeError(f'Error of Vertical Drive Arm: {e}')
    
#     def two_free_control(self, Td: object) -> None:
#         try:
#             K1 = tf([self.kd, self.kp, self.ki], [1, 0])
#             K2 = tf([self.kp, self.ki],          [self.kd, self.kp, self.ki])
            
#             self.Gyr_tfc = feedback(K1 * self.P, 1)
#             r = 1 * (Td > 0)
#             z, t, _ = lsim(K2, r, Td, 0)
            
#             y, _, _ = lsim(self.Gyr_tfc, z, Td, 0)
#         except Exception as e:
#             raise RuntimeError(f'Error of Vertical Drive Arm: {e}')

#     def analysis_step_response(self, T: object) -> Tuple[np.array, np.array]:
#         y, t = step(self.Gyr, T)
#         return y, t

#     def analysis_bode_line_diagram(self) -> Tuple[np.array, np.array, np.array]:
#         mag, phase, omega = bode(self.Gyr, logspace(-1, 2, 1000), plot=False)
#         return mag, phase, omega
