import math
from Physics.Vector2d import Vector2D


def calculate_apparent_wind(true_wind: Vector2D, boat_velocity: Vector2D) -> Vector2D:
    #Apparent wind = True wind - Boat velocity
    return true_wind - boat_velocity


def calculate_lift_force(apparent_wind: Vector2D,
                         boat_heading:float,
                         sail_area: float,
                         air_density:float) -> Vector2D:

    wind_speed = apparent_wind.magnitude()

    if wind_speed == 0:
        return Vector2D(0.0, 0.0)

    heading_vector = Vector2D.from_angle(boat_heading)
    angle_of_attack = apparent_wind.angle_between(heading_vector)
    lift_coefficient = math.sin(angle_of_attack)


    lift_magnitude = 0.5 * air_density * (wind_speed ** 2) * sail_area * lift_coefficient
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
    heading_vector = Vector2D.from_angle(boat_heading).normalise()

#projects velocity on to heading direction
    forward_speed = boat_velocity.dot(heading_vector)
    forward_velocity = forward_speed * heading_vector

#sideways component of velocity
    lateral_velocity = boat_velocity - forward_velocity
    lateral_speed = lateral_velocity.magnitude()

    if lateral_speed == 0:
        return Vector2D(0.0, 0.0)

    resistance = lateral_velocity.normalise() * -1 * lateral_drag_coeffiecient * (lateral_speed ** 2)

    return resistance

#Net Force
# Net force = Lift + Drag + Keel

def calculate_net_force (true_wind: Vector2D,
                         boat_velocity: Vector2D,
                         boat_heading: float,
                         parameters: dict) -> Vector2D:

    apparent_wind = calculate_apparent_wind(true_wind, boat_velocity)

    lift = calculate_lift_force(
        apparent_wind,
        boat_heading,
        parameters['boat_heading'],
        parameters['air_density'],
        parameters['sail_area']
    )

    drag = calculate_water_drag(
        boat_velocity,
        parameters['water_density'],
        parameters['reference_area'],
        parameters['drag_coefficient']
    )

    keel = calculate_keel_resistance(
        boat_velocity,
        boat_heading,
        parameters['lateral_drag_coefficient']
    )

    net_force = lift + drag + keel
    return net_force