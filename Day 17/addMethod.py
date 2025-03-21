class Car:
    
    def __init__(self, seat):
        self.seat = seat
        pass
    # bikin method
    def enter_race_mode(self):
        self.seat = 2
        
        
car_1 = Car(10)
print(car_1.seat)

car_1.enter_race_mode()
print(car_1.seat)