from src.flute import Flute
from src.drum import Drum
import threading
import time
from src.utils import us_sensor, touch_sensor


class Brickophone:
    """
    Represents a Brickophone control system.

    The Brickophone class simulates the behavior of a musical instrument
    that is controlled via sensors and operates with two components: a Flute
    and a Drum. It can transition between 'on' and 'off' states based on input
    from touch sensors. The class manages internal threads to handle sensor
    updates and component processing, ensuring seamless integration of the system.
    
    Attributes:
        state (str): The current state of the Brickophone, either 'on' or 'off'.
        us_sensor_distance (int): The distance measured by the ultrasonic sensor in centimeters.
        touch_sensor_1_state (bool): The current state of Touch Sensor 1 (pressed or not).
        touch_sensor_2_state (bool): The current state of Touch Sensor 2 (pressed or not).
        flute (Flute): The Flute component of the Brickophone.
        drum (Drum): The Drum component of the Brickophone.
        flute_thread (threading.Thread): The thread managing the processing of the Flute.
        drum_thread (threading.Thread): The thread managing the processing of the Drum.
        us_sensor_thread (threading.Thread): The thread that updates the ultrasonic sensor state.
        touch_sensor_thread (threading.Thread): The thread that updates the touch sensor states.
    
    Author: Jack McDonald
    """

    def __init__(self) -> None:
        self.state = 'off'
        self.us_sensor_distance = 0
        self.touch_sensor_1_state = False
        self.touch_sensor_2_state = False
        self.flute = Flute(self)
        self.drum = Drum(self)

        self.flute_thread = threading.Thread(target=self.flute.process, name='flute_thread')
        self.drum_thread = threading.Thread(target=self.drum.process, name='drum_thread')
        self.us_sensor_thread = threading.Thread(target=self.__update_distance, name='us_sensor_thread')
        self.touch_sensor_thread = threading.Thread(target=self.__update_touch_states, name='touch_sensor_thread')

        self.flute_thread.setDaemon(True)
        self.drum_thread.setDaemon(True)
        self.us_sensor_thread.setDaemon(True)
        self.touch_sensor_thread.setDaemon(True)

        self.flute_thread.start()
        self.drum_thread.start()
        self.us_sensor_thread.start()
        self.touch_sensor_thread.start()

    def process(self) -> None:
        """
        Call this once to periodically execute a state's 'do' action.
        
        This method determines the current state of the Brickophone 
        and transitions between 'on' and 'off' states based on 
        the touch sensor inputs.
        
        Returns:
            None
        """
        while True:
            if self.state == 'off':
                print('The brickophone is off.')
                if self.touch_sensor_1_state and self.touch_sensor_2_state:
                    print('Powering on...')
                    self.__transition_to('on')
                    time.sleep(2)

            elif self.state == 'on':
                print('The brickophone is on.')
                if self.touch_sensor_1_state and self.touch_sensor_2_state:
                    print('Powering off...')
                    self.__transition_to('off')
                    time.sleep(2)

    def __transition_to(self, new_state: str) -> None:
        self.__exit_state()
        self.state = new_state
        self.__enter_state()

    def __exit_state(self) -> None:
        if self.state == 'on':
            self.flute.stop()
            self.drum.stop()

    def __enter_state(self) -> None:
        if self.state == 'on':
            self.flute.start()
            self.drum.start()

    def __update_distance(self) -> None:
        while True:
            self.us_sensor_distance = us_sensor.get_distance()

    def __update_touch_states(self) -> None:
        while True:
            self.touch_sensor_1_state = touch_sensor.is_pressed(1)
            self.touch_sensor_2_state = touch_sensor.is_pressed(2)

    def get_us_sensor_distance(self) -> int:
        """
        Returns the distance measured by ultrasonic sensor in centimeters.
        
        Returns:
            int: The distance measured by ultrasonic sensor in centimeters.
        """
        return self.us_sensor_distance

    def get_touch_sensor_1_state(self) -> bool:
        """
        Returns the current state of Touch Sensor 1.
        
        Returns:
            bool: The current state of Touch Sensor 1.
        """
        return self.touch_sensor_1_state

    def get_touch_sensor_2_state(self) -> bool:
        """
        Returns the current state of Touch Sensor 2.
        
        Returns:
            bool: The current state of Touch Sensor 2.
        """
        return self.touch_sensor_2_state

    def turn_on(self) -> None:
        """
        Updates the Brickophone state to 'on'.
        
        Returns:
            None
        """
        self.__transition_to('on')

    def turn_off(self) -> None:
        """
        Updates the Brickophone state to 'off'.
        
        Returns:
            None
        """
        self.__transition_to('off')
