class Display:
    def __init__(self, id, car_park,message="", is_on= False):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.message}"

    def update(self, data):
        for key, value in data.items():
            if key == "message":
                self.message = value
            print(f"{key}: {value}")
