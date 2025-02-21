from utils import motor
import time

ANGLE = 80
PERIOD = 0.2


class Drum:
    """
    Represents a Drum component that interacts with a Brickophone and its respective
    touch sensors for rhythmic actions.

    The Drum class manages the operational states ('off', 'idle', 'active') of the drum.
    It provides methods to start, stop, and process drum actions based on inputs from
    a connected device (Brickophone). The purpose is to mimic a toggleable drum loop
    controlled via external sensors.

    Attributes:
        brickophone (Brickophone): An instance of the Brickophone class used to interact with touch sensors.
        state (str): The current state of the drum, which can be 'off', 'idle', or 'active'.

    Author: Jack McDonald
    """

    def __init__(self, brickophone) -> None:
        self.brickophone = brickophone
        self.state = 'off'

    def process(self) -> None:
        """
        Call this once to periodically execute a state's 'do' action.

        This method determines the current state of the drum and controls
        the toggleable drum loop.

        Returns:
            None
        """
        while True:
            # Toggle loop on
            if self.brickophone.get_touch_sensor_2_state() and self.state == 'idle':
                self.state = 'active'

            while self.state == 'active':
                time.sleep(0.5)
                motor.oscillate_motor(ANGLE, PERIOD)

                # Toggle loop off
                if self.brickophone.get_touch_sensor_2_state():
                    self.state = 'idle'
                    time.sleep(0.5)
                    break

    def stop(self) -> None:
        """
        Updates the drum state to 'off'.

        Returns:
            None
        """
        self.state = 'off'

    def start(self) -> None:
        """
        Updates the drum state to 'idle'.

        Returns:
            None
        """
        self.state = 'idle'
