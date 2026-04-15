import pygame
import sys
from snake import Snake
from food import Food
from file_manager import FileManager


class Game:
    """Main game class that manages the game loop, events, and rendering.  """
    _instance = None

    def __new__(cls):
        """Singleton pattern to ensure only one instance of Game exists."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True

        pygame.init()
        self._width = 600
        self._height = 600
        self._block_size = 20
        self._fps = 10
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption("Snake Game")
        self._clock = pygame.time.Clock()
        self._font = pygame.font.SysFont("Arial", 24)
        self._file_manager = FileManager()
        self._player_name = "Player"

    def set_player_name(self, name):
        self._player_name = name