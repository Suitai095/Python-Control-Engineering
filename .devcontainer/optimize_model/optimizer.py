# define objective function.
import numpy as np


def get_motion_stop_point(
    y: np.array,
    t: np.array,
    ref: float,
    stability_time: float,
    ) -> np.array:
    residual_vibration = []
    for y_i, t_i in zip(y, t):
        if y_i >= ref:
            residual_vibration.append(y_i)
        
        if t_i > stability_time:
            break

    return np.array(residual_vibration)


def get_stability_time(
    wave_array: np.array,
    time_array: np.array,
    limit_over_shoot_line: float,
    limit_under_shoot_line: float
    ) -> np.array:
    stability_times = []
    for wave_elem, time_elem in zip(wave_array, time_array):
        if wave_elem > limit_over_shoot_line or wave_elem < limit_under_shoot_line:
            stability_times.append(time_elem)

    return np.array(stability_times)


def term_over_and_under_value(wave_array: np.array) -> float:
    over_shoot = np.abs(np.max(wave_array))
    under_shoot = np.abs(np.min(wave_array))
    return over_shoot + under_shoot


def term_stability_time(
    time_array: np.array,
    limit_stablity_time: float,
    penalty: float = 1_000_000) -> float:
    max_time = np.max(time_array)
    if (time := (max_time / limit_stablity_time)) < limit_stablity_time:
        return time
    else:
        return time + penalty


def optimize_function(
    wave_array: np.array,
    time_array: np.array,
    ref: float,
    over_shoot_value: float = 1.0,
    under_shoot_value: float = 1.0,
    limit_stability_time: float = 1.0,
    ) -> float:
    limit_over_shoot_line = ref + over_shoot_value
    limit_under_shoot_line = ref - under_shoot_value
    
    wave = get_motion_stop_point(
        wave_array, time_array, ref, limit_stability_time)
    stability_times = get_stability_time(
        wave_array, time_array, limit_over_shoot_line, limit_under_shoot_line)

    term_over_and_under_data = term_over_and_under_value(wave)
    term_stability_time_data = term_stability_time(
        stability_times, limit_stability_time)

    return term_over_and_under_data + term_stability_time_data
