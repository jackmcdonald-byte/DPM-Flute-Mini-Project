from enum import Enum
from src.flute import Flute
from src.drum import Drum
import threading
import time
from src import us_sensor

UPDATE_FREQUENCY = 10

class Brickophone:

    def __init__(self):
        self.state = 'off'
        self.us_sensor_distance = 0
        self.flute = Flute(self)
        self.drum = Drum(self)
        self.flute_thread = threading.Thread(target = self.flute.process, name = 'flute_thread')
        self.drum_thread = threading.Thread(target = self.drum.process, name = 'drum_thread')
        self.us_sensor_thread = threading.Thread(target = self.__update_distance, name ='us_sensor_thread')
        self.flute_thread.setDaemon(True)
        self.drum_thread.setDaemon(True)
        self.us_sensor_thread.setDaemon(True)
        self.flute_thread.start()
        self.drum_thread.start()
        self.us_sensor_thread.start()


    def process(self):
        """call this periodically to execute a states 'do' action"""
        if self.state == 'off':
            print('The brickophone is off.')
        elif self.state == 'on':
            print('The brickophone is on.')


    def __transition_to(self, new_state):
        self.__exit_state()
        self.state = new_state
        self.__enter_state()


    def __exit_state(self):
        if self.state == 'on':
            self.flute.stop()
            self.drum.stop()


    def __enter_state(self):
        ...


    def __update_distance(self):
        while True:
            self.us_sensor_distance = us_sensor.get_distance()
            time.sleep(1 / UPDATE_FREQUENCY)


    def get_us_sensor_distance(self):
        return self.us_sensor_distance


    def turn_on(self):
        self.__transition_to('on')


    def turn_off(self):
        self.__transition_to('off')


class BrickophoneState(Enum):
    OFF = 'off'
    ON = 'on'