import pygame
from game_object import Gameobject

class Snake(Gameobject):
    def __init__(self, x, y, block_size):
        super().__init__(x,y)
        self._block_size = block_size
        self._body= [[x, y]]
        self._direction = [block_size, 0]
        self._score = 0
        self._color = (0, 200, 0)

    @property
    def score(self):
        return self._score
        
    @property
    def body(self):
        return self._body
        
    @property
    def direction(self):
        return self._direction
        
    def set_direction(self, dx: int, dy: int):
        if [dx,dy] != [-self._direction[0], -self._direction[1]]:
            self._direction= [dx, dy]

    def move(self):
        head = [self.body[0][0] + self._direction[0], self._body[0][1] + self._direction[1]]
        self._body.insert(0, head)
        self._body.pop()

    def grow(self):
        tail = self._body[-1][:]
        self._body.append(tail)
        self._score += 1
        
    def check_self_collision(self) -> bool:
            return self._body[0] in self._body[1:]
        
    def check_wall_collision(self, width: int, height: int) -> bool:
        x, y =self._body[0]
        return x < 0 or x>=width or y < 0 or y >= height
        
    def draw(self, screen):
        for segment in self._body:
            pygame.draw.rect(
                screen,
                self._color,
                pygame.Rect(segment[0], segment[1],
                                self._block_size, self._block_size)
            )

