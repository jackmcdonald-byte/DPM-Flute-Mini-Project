#!/usr/bin/env python3

"""
This test is used to collect data from the color sensor.
It must be run on the robot.
"""

from utils.brick import TouchSensor, EV3ColorSensor, wait_ready_sensors, reset_brick
from time import sleep

DELAY_SEC = 0.01  # seconds of delay between measurements
COLOR_SENSOR_DATA_FILE = "../data_analysis/color_sensor.csv"

TOUCH_SENSOR = TouchSensor(1) # touch sensor on port 1
COLOR_SENSOR = EV3ColorSensor(2) # color sensor on port 2

wait_ready_sensors(True)
print("Done waiting.")

def collect_color_sensor_data():
    """Collect color sensor data."""
    try:
        with open(COLOR_SENSOR_DATA_FILE, "w") as output_file:
            output_file.write("R,G,B\n")  # CSV header
            prev_pressed = False
            print("Ready to collect samples. Press the touch sensor to record data.")
            while True:
                current_pressed = TOUCH_SENSOR.is_pressed()
                if current_pressed and not prev_pressed:
                    color_data = COLOR_SENSOR.get_value()
                    if color_data is not None:
                        # Extract first 3 values (R, G, B)
                        r, g, b = color_data[:3]  # Slice to 3 elements
                        print(f"R: {r}, G: {g}, B: {b}") # Print to terminal
                        output_file.write(f"{r},{g},{b}\n") # Write to file
                        output_file.flush()
                prev_pressed = current_pressed
                sleep(DELAY_SEC)
    except BaseException as e:
        print(f"An error occurred: {e}")
    finally:
        print("Done collecting color samples")
        reset_brick()
        exit()

if __name__ == "__main__":
    collect_color_sensor_data()
