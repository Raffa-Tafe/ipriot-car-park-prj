import random
from sensor import Sensor
from display import Display
class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []
        self.displays = displays if displays is not None else []

    def __str__(self):
        return  f"Car park at {self.location}, with {self.capacity}"


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Sensor):
            self.sensors.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()

    @property
    def available_bays(self):
        if len(self.plates) >= self.capacity:
            return 0
        else:
            return self.capacity - len(self.plates)

    def update_display(self):
        data = {"available_bays": self.available_bays, "temprature": 25}
        for display in self.displays: display.update(data)
