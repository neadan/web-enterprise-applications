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
        self.channels = {}

    def volume_up(self, increment):
        print(f"Turning volume up by {increment}")
        self.volume = self.volume + increment

    def volume_down(self, increment):
        print(f"Turning volume down by {increment}")
        self.volume = self.volume - increment

    def display_volume(self):
        print(f"Current volume is {self.volume}")

    def add_channel(self, channel_nb, channel_name):
        self.channels[channel_nb] = channel_name

    def remove_channel(self, channel_nb):
        del self.channels[channel_nb]

    def __repr__(self):
        return f"{self.brand}:{self.name}"


class Store:
    def __init__(self):
        self.store_stock = {'TVs': [],
                            'Cameras': []}

    def add_tv(self, tv):
        self.store_stock['TVs'].append(tv)

    def add_camera(self, camera):
        self.store_stock['Cameras'].append(camera)

    def display_stock(self):
        print(f"Number of TVs: {len(self.store_stock['TVs'])}, Number of Cameras: {len(self.store_stock['Cameras'])}")

    def sell(self, item):
        if item == 'Camera':
            if len(self.store_stock['Cameras']) == 0:
                raise ValueError("No more cameras in stock")
            else:
                self.store_stock['Cameras'].pop(0)
        elif item == 'TV':
            if len(self.store_stock['TVs']) == 0:
                raise ValueError("No more TVs in stock")
            else:
                self.store_stock['TVs'].pop(0)
        else:
            raise ValueError(f"Store does not sell {item}")