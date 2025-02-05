class Drum:
    def __init__(self, brickophone):
        self.brickophone = brickophone
        self.state = 'idle'

    def process(self):
        while True:
            if self.state == 'active':
                ...


    def stop(self):
        pass


class DrumState:
    IDLE = 'idle'
    ACTIVE = 'active'