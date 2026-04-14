from abc import ABC, abstractmethod

class gameobject(ABC):
    """Abstract base class for all game objects apples, snake etc."""
    
    def __init__(self):
        self._x = x
        self._y = y

    @roperty
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @abstractmethod
    def draw(self, screen):
        pass