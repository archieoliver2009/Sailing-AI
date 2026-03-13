import math
from Physics.Vector2d import Vector2D

class Boat:
    def __init__(self, position, mass, sail_area, drag_coeffiecient):
        self.position = position
        self.velocity = Vector2D(0.0, 0.0)
        self.acceleration = Vector2D(0.0, 0.0)

        self.heading = 0.0

        self.mass = mass
        self.sail_area = sail_area
        self.drag_coeffiecient = drag_coeffiecient

    def heading_vector(self):
        return Vector2D.from_angle(self.heading)

#F=ma
    def apply_force(self, force: Vector2D):
        self.acceleration = force * (1/self.mass)

    def update(self, dt):
        self.velocity = self.velocity + (self.acceleration * dt)
        self.position = self.position + (self.velocity * dt)

        #Resets acceleration for next time step
        self.acceleration = Vector2D(0.0, 0.0)

    def heading_change(self, delta_angle):
        self.heading += delta_angle

    def speed(self):
        return self.velocity.magnitude()

    def forward_speed(self):
        heading_vec = self.heading_vector()
        return self.velocity.dot(heading_vec)

    def lateral_speed(self):
        heading_vec = self.heading_vector()
        lateral = heading_vec.rotate(math.pi/2)
        return self.velocity.dot(lateral)

    def apply_keel_resistance(self, keel_drag):
        lateral = self.heading_vector().rotate(math.pi/2)

        sideways_velocity = lateral * self.lateral_speed()

        drag_force = sideways_velocity * -keel_drag

        self.apply_force(drag_force)

