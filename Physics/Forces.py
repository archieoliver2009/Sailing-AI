import math
from Physics.Vector2d import Vector2D


def calculate_apparent_wind(true_wind: Vector2D, boat_velocity: Vector2D) -> Vector2D:
    #Apparent wind = True wind - Boat velocity
    return true_wind - boat_velocity


def calculate_lift_force(apparent_wind: Vector2D,
                         boat_heading:float,
                         lift_coefficient: float,
                         air_density:float) -> Vector2D:

    wind_speed = apparent_wind.magnitude()

    if wind_speed == 0:
        return Vector2D(0.0, 0.0)

    heading_vector = Vector2D.from_angle(boat_heading)
    angle_of_attack = apparent_wind.angle_between(heading_vector)

    lift_magnitude = 0.5 * air_density * (wind_speed ** 2) * lift_coefficient * math.sin(angle_of_attack)
    lift_direction = apparent_wind.rotate(math.pi /2).normalise()

    return lift_direction * lift_magnitude

def calculate_water_drag(boat_velocity: Vector2D,
                                drag_coefficient: float,
                                water_density: float,
                                reference_area: float) -> Vector2D:
    boat_speed = boat_velocity.magnitude()

    if boat_speed == 0:
        return Vector2D(0.0, 0.0)

    drag_magnitude = 0.5 * drag_coefficient * water_density * reference_area * (boat_speed ** 2)
    drag_direction = boat_velocity.normalise() * -1

    return drag_direction * drag_magnitude

#Lateral Keel resistance
def calculate_keel_resistance (boat_velocity: Vector2D,
                               boat_heading: float,
                               lateral_drag_coeffiecient: float,) -> Vector2D:

#Net Force