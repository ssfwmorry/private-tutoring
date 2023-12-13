from car import Car

class Truck(Car):
    def __init__(self, seats, max_speed, capacity):
        self.seats = seats
        self.max_speed = max_speed
        self.capacity = capacity

    def spec(self):
        print('Seats: ' + str(self.seats) + ', Max speed: ' + str(self.max_speed)+ ', Capacity: ' + str(self.capacity))

t=Truck(4,100,100)
t.spec()