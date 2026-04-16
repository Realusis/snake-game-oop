# Snake game - OOP Coursework

## 1. Introduction

### What is this application?
This is a Snake game implemented in Python using Object-Oriented Programming (OOP) principles.
The player controls a snake that moves around the screen, eats food to grow longer and score points.
The game ends when the snake hits a wall or itself.

### How to run the program?
1. Make sure that Python 3 is installed
2. Install pygame:
````
pip install pygame
````
3. Run the game:
````
python main.py
````
### How to use the program?
- Enter your name in the game window 
- Press any key  to start
- Use arrow keys to control the snake
- Eat red squares to grow and score points
- Avoid hitting walls and yourself
- Press **R** to restart or **Q** to quit after game over

## 2. Body/Analysis

### OOP Pillars

#### Encapsulation
Encapsulation means hiding internal data and only exposing it through methods.
In this project, all class attributes use a single underscore `_` to indicate that they are protected.
For example in the `snake` class:

```python
    self._score = 0
    self._color = (0, 200, 0)

    @property
    def score(self):
        return self._score
```
The `_score` attribute is not accesible directly from outside the class, it is accessed through the `score` property.

#### Inheritance 
Inheritance allows a class to reuse code from another class.
Both `Snake` and `Food` classes inherit from abstract base class `Gameobject`:

```python
class Snake(Gameobject):
    def __init__(self, x, y, block_size):
        super().__init__(x,y)
```

This means `Snake` and `Food` automatically get the `_x` and `_y` attributes from `Gameobject`

#### Abstraction
Abstraction means hiding complex implementation details and showing only what is necessary.
`Gameobject` is an abstract class with an abstract method `draw()`:

```python
from abc import ABC, abstractmethod

class Gameobject(ABC):
    """Abstract base class for all game objects apples, snake etc."""
    
    @abstractmethod
    def draw(self, screen):
        pass
```

Every class that inherits from `Gameobject` must implement its own `draw` method.

#### Polymorphism
Polymorphism means the same method works differently in different classes.
Both `Snake` and `Food` have a `draw()` method but they draw differently:

```python
# Snake draws green squares for each body segment
def draw(self, screen):
    for segment in self._body:
        pygame.draw.rect(screen, self._color, ...)

# Food draws a single red square
def draw(self, screen):
    pygame.draw.rect(screen, self._color, ...)
```

### Design pattern - Singleton
The `Game` class uses the Singleton pattern to ensure only one game instance exists at a time.
This is suitable because having multiple game windows would couse conflicts.

```python
class Game:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
```
### Composition and Aggregation
The `Game` class uses composition - it contains `Snake`, `Food` and `FileManager` objects.
These objects are created inside `Game` and cannot exist independently of it.
```python
self._file_manager = FileManager()
snake = Snake(self._width // 2, self._height // 2, self._block_size)
food = Food(self._height, self._width, self._block_size)
```

### Reading and writing to file
The `FileManager` class handles saving and loading scores using a CSV file.

```python
def save_score(self, player_name, score):
    file_exists = os.path.exists(self.file_path)
    with open(self.file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "score", "date"])
        writer.writerow([player_name, score, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def load_scores(self):
    if not os.path.exists(self.file_path):
        return []
    with open(self.file_path, 'r') as file:
        reader = csv.DictReader(file)
        scores = [row for row in reader]
        return  sorted(scores, key=lambda x: int(x['score']), reverse=True)
```

### Testing 
Unit tests were written using the `unittest` framework to test the `Snake` class functionality

```python
def test_initial_score(self):
    self.assertEqual(self.snake.score, 0) 

def test_initial_length(self):
    initial_length = len(self.snake.body)
    self.snake.grow()
    self.assertEqual(len(self.snake.body), initial_length + 1)
```

## 3. Results and Summary

### Results 
- The snake game was successfully implemented using OOP principles in python.
- All four OOP pillars were applied: Encapsulation , Inheritance, Abstraction and Polymorphism.
- The Singleton design pattern was used to ensure only one Game Instance exists.
- Player scores are saved and loaded from CSV file using the FileManager class.
- 6 unit tests were written and all pass successfully.

### Conclusions
The goal of this coursework was to create a Snake game using Object-Oriented Programming principles.
The result is fully functional game where the player can control a snake, eat food, and compete for high scores.
All scores are saved to a CSV file and displayed after each game.
In the future, the game could be extended by adding difficulty levels, different food types, or a multiplayer mode.

## 4. Resources
- [Python documentation](https://docs.python.org/3/)
- [Pygame documentation](https://www.pygame.org/docs/)
- [OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- [Unittest framework](https://docs.python.org/3/library/unittest.html)
- [PEP8 style guide](https://pep8.org/)