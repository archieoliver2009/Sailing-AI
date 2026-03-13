from Physics.Vector2d import Vector2D
from Physics.Wind import Wind
from Physics.Forces import calculate_lift_force, calculate_net_force
from Physics.Boat import Boat

class Simulator:
    def __init__(self, boat: Boat, wind: Wind, time_step: float = 0.1):
        self.boat = boat
        self.wind = wind
        self.time_step = time_step

        self.time = 0.0

        self.position_history = []
        self.velocity_history = []
        self.wind_history = []

    def step(self):
        dt = self.time_step

        #Update wind against timestep
        self.wind.update(dt)

        #Get new wind vector
        wind_vector = self.wind.get_wind_vector()

        #Calculate total force acting on boat
        net_force = calculate_net_force(self.boat, wind_vector)

        #Apply net force to cause an acceleration
        self.boat.apply_force(net_force)

        #Update boat forces
        self.boat.update(dt)

        #Update time
        self.time += dt

        #record changes in history
        self.position_history.append(self.boat.position)
        self.velocity_history.append(self.boat.velocity)
        self.wind_history.append(wind_vector)

    #Run simulation for n steps
    def run(self, steps: int):
        for i in range(steps):
            self.step()

    def reset(self, start_position:Vector2D):
        self.boat.position = start_position
        self.boat.velocity = Vector2D(0.0, 0.0)
        self.boat.acceleration = Vector2D(0.0, 0.0)

        self.time = 0.0

        self.position_history.clear()
        self.velocity_history.clear()
        self.wind_history.clear()





