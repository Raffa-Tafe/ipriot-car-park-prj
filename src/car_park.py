import random
from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return  f"Car park at {self.location}, with {self.capacity}"

    @property
    def available_bays(self):
        bays_left = self.capacity - len(self.plates)
        return max(0, bays_left)


    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")
        if isinstance(component, Sensor):
            self.sensors.append(component)

    # in CarPark class
    def add_car(self, plate):
        if self.available_bays <= 0:
            return
        if plate not in self.plates:
            self.plates.append(plate)
            self.available_bays -= 1
            self.update_display()
            self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate not in self.plates:
            pass
        self.plates.remove(plate)
        self.available_bays += 1
        self.update_display()
        self._log_car_activity(plate, "exited")


    def update_display(self):
        data = {"available_bays": self.available_bays, "temprature": 25}
        for display in self.displays: display.update(data)

    # in CarPark class
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    @available_bays.setter
    def available_bays(self, value):
        self._available_bays = value



