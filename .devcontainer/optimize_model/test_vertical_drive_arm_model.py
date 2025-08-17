import numpy as np

from .vertical_drive_arm_model import PID_control_robot
from .vertical_drive_arm_model import I_PD_control_robot


def test_PID_control_robot() -> None:
    pid = PID_control_robot(1, 1, 1)

    ys, ts = pid.excute_result_for_response(np.arange(0, 2, 0.01))
    assert type(ys) == np.ndarray
    assert type(ts) == np.ndarray

    mag, phase, omega = pid.excute_result_bode_line_diagram()
    assert type(mag) == np.ndarray
    assert type(phase) == np.ndarray
    assert type(omega) == np.ndarray


def test_I_PD_control_robot() -> None:
    pid = I_PD_control_robot(1, 1, 1)

    ys, ts, zs = pid.excute_result_for_response(np.arange(0, 2, 0.01))
    assert type(ys) == np.ndarray
    assert type(ts) == np.ndarray
    assert type(zs) == np.ndarray

    mag, phase, omega = pid.excute_result_bode_line_diagram()
    assert type(mag) == np.ndarray
    assert type(phase) == np.ndarray
    assert type(omega) == np.ndarray