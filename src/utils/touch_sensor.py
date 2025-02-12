from utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR_1 = TouchSensor(1)
TOUCH_SENSOR_2 = TouchSensor(2)
wait_ready_sensors()


def is_pressed(sensor: int) -> bool:
    """
    Determine if a specific sensor is pressed.

    Parameters:
    sensor (int): The identifier of the sensor to check. Accepted values are
    1 for TOUCH_SENSOR_1 and 2 for TOUCH_SENSOR_2.

    Returns:
    bool: True if the specified sensor is pressed, False otherwise.
    """
    if sensor == 1:
        return TOUCH_SENSOR_1.is_pressed()
    elif sensor == 2:
        return TOUCH_SENSOR_2.is_pressed()
    else:
        return False
