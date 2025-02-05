from enum import Enum

class Flute:
    def __init__(self, brickophone):
        self.brickophone = brickophone
        self.state = 'idle'

    def process(self):
        while True:
            if self.state == 'active':
                self.play_sound(self.brickophone.get_us_sensor_distance())

    def start(self):
        ...

    def stop(self):
        ...

    def play_sound(self, param):
        pass


class FluteState(Enum):
    IDLE = 'idle'
    ACTIVE = 'active'