from src.utils.brick import Motor
import time

MOTOR = Motor("A")
MOTOR.set_limits()

RESTING_POSITION = 0


def oscillate_motor(angle: int, period: float) -> None:
    """
    Controls the oscillation of a motor to a specified angle and resting position within a defined period.
    This function performs a two-step movement: first to the specified angle, and then back to
    the resting position, pausing in between for half of the given period.

    Parameters:
        angle (int): The target angle for the motor to oscillate.
        period (float): The time in seconds for a complete oscillation cycle.

    Returns:
        None
    """
    MOTOR.set_position(angle)
    time.sleep(period / 2)
    MOTOR.set_position(RESTING_POSITION)
    time.sleep(period / 2)
