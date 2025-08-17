from typing import Any, Tuple

import numpy as np
import matplotlib.pyplot as plt

from .vertical_drive_arm_model import I_PD_control_robot
from .optimizer import get_motion_stop_point, get_stability_time


def arm_model_1() -> Tuple[np.array, np.array, np.array]:
    ipd = I_PD_control_robot(2, 10, 0.1)
    y, t, z = ipd.excute_result_for_response(np.arange(0, 2, 0.01))
    return y, t, z


def test_get_motion_stop_point() -> None:
    y, t, _ = arm_model_1()
    residual_vibration = get_motion_stop_point(
        y, t, ref=30, stability_time=1.0)

    stability_times = get_stability_time(y, t, 35, 25)

    assert len(residual_vibration) > 0, "No residual vibration found"
    assert np.max(residual_vibration) > 30, f"Residual vibration max: {np.max(residual_vibration)}"
    assert np.min(residual_vibration) > 20, f"Residual vibration min: {np.min(residual_vibration)}"
    assert len(stability_times) > 0, "No stability time found"
