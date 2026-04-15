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
    
    def _draw_score(self, score):
        text = self._font.render(f"Score: {score}", True, (255, 255, 255))
        self._screen.blit(text, (10, 10))

    def game_over_screen(self, score):
        """Displays the game over screen with the final score and options to restart or quit."""
        self._file_manager.save_score(self._player_name, score)
        scores = self._file_manager.load_scores()

        self._screen.fill((0, 0, 0))
        game_over_text = self._font.render("Game Over!", True, (255, 0, 0))
        self._screen.blit(game_over_text, (self._width // 2 - 120, 100))

        restart_text = self._font.render("Press R to Restart or Q to Quit", True, (255, 255, 255))
        self._screen.blit(restart_text, (self._width // 2 - 120, 150))

        for i, row in enumerate(scores[:5]):
            line = self._font.render(f"{i + 1}. {row['name']} - {row['score']}", True, (200, 200, 200))
            self._screen.blit(line, (self._width // 2 - 80, 220 + 35 * (i + 1)))

        pygame.display.flip()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()