from abc import ABCMeta, abstractmethod

__all__ = ['GameObject']


class GameObject(metaclass=ABCMeta):

    @abstractmethod
    def Start(self):
        pass

    @abstractmethod
    def Update(self):
        pass

    @abstractmethod
    def Draw(self):
        pass
