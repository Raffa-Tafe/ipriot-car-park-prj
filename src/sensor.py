
class Sensor:
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"{self.id} and {self.is_active}"

class EnterySensor(Sensor):
    ...

class ExitSensor(Sensor):
    ...