import math

class Vector2D:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)

#Basic Representation
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

#Vector Addition
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

#Vector Subtraction
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

#Scalar Vector Multiplication
    def __mul__(self, scalar: float):
        return Vector2D(self.x * scalar.x, self.y * scalar.y)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

#Magnitude (Pythagorean Theorem)
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

#Normalisation
    def normalise(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2D(0.0, 0.0)
        return Vector2D(self.x / mag, self.y / mag)

#Dot Product
    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

#Angle Between Vectors
    def angle_between(self, other) -> float:
        dot_product = self.dot(other)
        mag_product = self.magnitude() * other.magnitude()

        if mag_product == 0:
            return 0.0

        cos_theta = max(-1.0, min(1.0, dot_product/mag_product))
        return math.acos(cos_theta)

#Rotation (Radians)
    def rotation(self, angle_radians: float):
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)

        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta

        return Vector2D(x_new, y_new)

    @staticmethod
    def from_angle(angle_radians: float):
        return Vector2D(math.cos(angle_radians), math.sin(angle_radians))


