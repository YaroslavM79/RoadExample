from gameobject import GameObject
from .car import Car

__all__ = ['PassengerCar']


class PassengerCar(GameObject, Car):

    def __init__(self, speed=0, color=0, model=''):
        super(PassengerCar, self).__init__(speed, color, model)

    def Draw(self):
        pass

    def Start(self):
        pass

    def Update(self):
        pass
