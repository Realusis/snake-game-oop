import pygame
import random
from game_object import Gameobject

class Food(Gameobject):
    """represents the food that the snake eats to grow and score points."""

    def __init__(self, height, width, block_size):
        x, y = self._random_position(height, width, block_size)
        super().__init__(x, y)
        self._height = height
        self._width = width
        self._color = (200, 0, 0)
        self._block_size = block_size

    def _random_position(self, height, width, block_size):
        x = random.randrange(0, width, block_size)
        y = random.randrange(0, height, block_size)
        return x, y
    
    def respawn(self):
        self._x, self._y = self._random_position(self._height, self._width, self._block_size)

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            self._color,
            pygame.Rect(self._x, self._y, self._block_size, self._block_size)
        )