from utils.sound import Sound
import time

NOTE_MAPPING = {
    0: "B3",
    1: "C3",
    2: "C#3",
    3: "D3",
    4: "D#3",
    5: "E3",
    6: "F3",
    7: "F#3",
    8: "G3",
    9: "G#3",
    10: "A3",
    11: "A#3",
    12: "B3",
    13: "C4",
    14: "C#4",
    15: "D4",
    16: "D#4",
    17: "E4",
    18: "F4",
    19: "F#4",
    20: "G4",
    21: "G#4",
    22: "A4",
    23: "A#4",
    24: "B4",
    25: "C5"}

NOTE_DISTANCE_SPACING = 5
MAX_DISTANCE = 20
DISTANCE_OFFSET = 0
VOLUME = 100
DURATION = 0.3


class Flute:
    """
    This class represents a Flute instrument that interacts with a Brickophone device.

    The Flute class is designed to integrate with a Brickophone, utilizing its sensors
    such as touch and ultrasonic sensors. The class maps distances to specific sound
    tones, providing a mechanism to play corresponding notes based on measured distances.
    It supports state management (active or off) to control when sounds should be played.

    Attributes:
        brickophone (Brickophone): The Brickophone object that the Flute interacts with.
        state (str): The current state of the Flute, either 'off' or 'active'.
        note_capacity (int): The maximum number of notes that can be mapped based on
                             defined distance and spacing.
        note_distance_mapping (dict): A mapping between distances (int) and Sound objects
                                      of different tones.

    Author: Jack McDonald
    """

    def __init__(self, brickophone) -> None:
        self.brickophone = brickophone
        self.state = 'off'

        self.note_capacity = MAX_DISTANCE // NOTE_DISTANCE_SPACING
        self.note_distance_mapping = {}

        for i in range(1, MAX_DISTANCE + 1):
            sound = Sound(duration=DURATION, volume=VOLUME, pitch=NOTE_MAPPING[(i + 1) // NOTE_DISTANCE_SPACING])
            self.note_distance_mapping[i + DISTANCE_OFFSET] = sound

    def process(self) -> None:
        """
        Call this once to periodically execute a state's 'do' action.

        This method determines the current state of the flute and plays a sound
        when the correct conditions are met.

        Returns:
            None
        """
        while True:
            if self.state == 'active' and self.brickophone.get_touch_sensor_1_state():
                self.play_sound(self.brickophone.get_us_sensor_distance())

    def start(self) -> None:
        """
        Updates the flute state to 'active'.

        Returns:
            None
        """
        self.state = 'active'

    def stop(self) -> None:
        """
        Updates the flute state to 'off'.

        Returns:
            None
        """
        self.state = 'off'

    def play_sound(self, distance: int) -> None:
        """
        Plays a tone given a distance in centimeters.

        Parameters:
            distance (int): The distance measured by ultrasonic sensor in centimeters.

        Returns:
            None
        """
        if distance in self.note_distance_mapping:
            self.note_distance_mapping[distance].play()
            time.sleep(DURATION - DURATION * 0.2)
