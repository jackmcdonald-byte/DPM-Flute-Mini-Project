import time

from utils.touch_sensor import TOUCH_SENSOR_1
from utils.brick import TouchSensor, wait_ready_sensors

TOUCH_SENSOR_1 = TouchSensor(1)
TOUCH_SENSOR_2 = TouchSensor(2)
wait_ready_sensors()

def main():
    while True:
        time.sleep(0.5)
        print(TOUCH_SENSOR_1.get_value())
        print(TOUCH_SENSOR_2.get_value())

if __name__ == '__main__':
    main()