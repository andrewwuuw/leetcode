class Car:
    wheel_number = 0
    car_doors = 0
    passnagers = 0
    
    def __init__(self, wheel_number=4, car_doors=4, passnagers=4):
        self.wheel_number = wheel_number
        self.car_doors = car_doors
        self.passnagers = passnagers
class SUV(Car):
    brand_name = ""
    air_bags = 0
    sunroof = True
    def __init__(self, wheel_number, car_doors, passnagers, brand_name="BMW", air_bags=6, sunroof=True):
        super().__init__(wheel_number, car_doors, passnagers)
        self.brand_name = brand_name
        self.air_bags = air_bags
        self.sunroof = sunroof
    
    def drive(self):
        print("Drive the SUV {0} to my vocation.".format(self.brand_name))
    

class Wagon(Car):
    brand_name = ""
    def __init__(self, wheel_number, car_doors, passnagers, brand_name=""):
        super().__init__(wheel_number, car_doors, passnagers)
        self.brand_name = brand_name

    def drive(self):
        print("Drive the Wagon {0} to my vocation.".format(self.brand_name))

toyota_rav4 = SUV(4, 5, 5, "Toyota")
bmw = SUV(4, 6, 6, "BMW X6")
volsWagon = Wagon(4, 4, 6, "VolsWagon")

def let_drive(cars):
    for car in cars:
        car.drive()

let_drive([toyota_rav4, bmw, volsWagon])