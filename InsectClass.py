import random

class Insect:
    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0     #You first have to initialize to 0

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_miles(self):
        return self.flight      #It's better to have one method do just one thing.