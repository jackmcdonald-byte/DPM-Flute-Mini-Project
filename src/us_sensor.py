from project.utils.brick import EV3UltrasonicSensor, wait_ready_sensors

us_sensor = EV3UltrasonicSensor(1)

wait_ready_sensors()

def get_distance():
    return us_sensor.get_cm()