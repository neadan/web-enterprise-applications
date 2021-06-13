class ElectronicDevice:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def turn_on(self):
        print(f"Turning {self.name} on...")

    def turn_off(self):
        print(f"Turning {self.name} off...")


class Camera(ElectronicDevice):
    def __init__(self, name, brand, case='leather'):
        super().__init__(name=name, brand=brand)
        self.case = case

    def take_picture(self):
        print("Taking picture with camera...")

    def print_case(self):
        print(f"Camera has case made of: {self.case}")

    def __repr__(self):
        return f"Camera name is: {self.name}, brand is: {self.brand}"


class Television(ElectronicDevice):
    def __init__(self, name, brand, screen_size):
        super().__init__(name=name, brand=brand)
        self.screen_size = screen_size
        self.volume = 0

    def volume_up(self, increment):
        print(f"Turning volume up by {increment}")
        self.volume = self.volume + increment

    def volume_down(self, increment):
        print(f"Turning volume down by {increment}")
        self.volume = self.volume - increment

    def display_volume(self):
        print(f"Current volume is {self.volume}")

    def __repr__(self):
        return f"TV name is: {self.name}, brand is: {self.brand}, screen size is: {self.screen_size}"


