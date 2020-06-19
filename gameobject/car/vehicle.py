from abc import ABCMeta, abstractmethod
from euclid3 import Vector2

__all__ = ['Vehicle']


class Vehicle(metaclass=ABCMeta):

    def __init__(self, speed=0, color=0, model=''):
        self._speed = speed
        self._color = color
        self._model = model
        self._postition = Vector2()
        self._orientation = Vector2()
        #TODO make getter/setter for next 3 objects
        self._belong_to = None
        self._previous_belong_to = None
        self._next_belong_to = None

    @abstractmethod
    def move(self):
        raise NotImplementedError

    #########################
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    ##################
    @property
    def position(self):
        return self._postition

    @position.setter
    def position(self, value: Vector2):
        self._postition = value

    ##################
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    ##################
    @property
    def model(self):
        return self._model

    @model.setter
    def color(self, value):
        self._model = value
