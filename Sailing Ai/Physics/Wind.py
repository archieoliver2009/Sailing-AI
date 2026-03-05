import math
from Physics.Vector2d import Vector2D

class Wind:
    def __init__(self,
                 base_speed: float,
                 base_direction_degrees: float,
                 direction_variation_amplitude: float,
                 direction_variation_frequency: float,
                 speed_variation_amplitude: float,
                 speed_variation_frequency: float,):

        self.base_speed = base_speed
        self.base_direction = base_direction_degrees

        self.dir_amp = direction_variation_amplitude
        self.dir_freq = direction_variation_frequency

        self.speed_amp = speed_variation_amplitude
        self.speed_freq = speed_variation_frequency

        self.time = 0.0

    def update(self, delta_time: float):
        self.time += delta_time

    #Calculate current wind vector
    def get_wind_vector(self) -> Vector2D:
        direction_offset = self.dir_amp * math.sin(self.dir_freq * self.time)
        current_direction = self.base_direction + direction_offset

        speed_offset = self.speed_amp * math.sin(self.speed_freq * self.time)
        current_speed = self.base_speed + speed_offset

        #assigns x and y values to vector2d
        return Vector2D(
            current_speed * math.cos(current_direction),
            current_speed * math.sin(current_direction)
        )
