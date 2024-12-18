
class Vehicle:
    def start(self):
        raise NotImplementedError("Tato metoda musí být přepsána.")


class Car(Vehicle):
    def start(self):
        return "Auto startuje"


class Truck(Vehicle):
    def start(self):
        return "Náklaďák startuje"


class Bus(Vehicle):
    def start(self):
        return "Autobus startuje"


class VehicleFactory:
    @staticmethod
    def get_vehicle(enum):
        if enum == "car":
            return Car()
        elif enum == "truck":
            return Truck()
        elif enum == "bus":
            return Bus()
        else:
            raise ValueError("Neznámý typ vozidla")