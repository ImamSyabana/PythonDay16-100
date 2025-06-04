class Animal:
    def __init__(self):
        self.number_of_eyes = 2
        
    def breathe(self):
        print("inhale and exhale")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def breatheFish(self):
        super().breathe()
        print("doing this underwater.")
        
    def swim(self):
        print("moving in the water")
        
        
nemo = Fish()
nemo.swim()
nemo.breatheFish()

print(nemo.number_of_eyes)