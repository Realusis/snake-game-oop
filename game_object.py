from abc import ABC, abstractmethod

class Gameobject(ABC):
    """Abstract base class for all game objects apples, snake etc."""
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @abstractmethod
    def draw(self, screen):
        pass