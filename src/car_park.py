import random
from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, display=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors
        self.display = display

    def __str__(self):
        return  f"Car park at {self.location}, with {self.capacity}"


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Sensor):
            self.sensors.append(component)