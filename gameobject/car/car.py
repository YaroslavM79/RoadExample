#import Vector2 as Vector2

from .vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, speed=0, color=0, model=''):
        super(Car, self).__init__(speed, color, model)

    # from vehicle class
    def move(self):
        raise NotImplemented
