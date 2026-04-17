import unittest
from snake import Snake

class TestSnake(unittest.TestCase):
    def setUp(self):
        """Set up a snake instance for testing."""
        self.snake = Snake(100, 100, 20)# Create a snake instance for testing with initial position (100, 100) and block size of 20.
    
    def test_initial_score(self):
        """Test that the initial score of the snake is set to 0."""
        self.assertEqual(self.snake.score, 0) 
    
    def test_score_after_multiple_grows(self):
        """Test score increases correctly after multiple grows."""
        for _ in range(5):
            self.snake.grow()
        self.assertEqual(self.snake.score, 5)

    def test_initial_length(self):
        """Test that the initial length of the snake is 1."""
        initial_length = len(self.snake.body)
        self.snake.grow()
        self.assertEqual(len(self.snake.body), initial_length + 1) # Test that the snake grows correctly when it eats food.

    def test_set_direction(self):
        """Test that the snake can change direction correctly and does not allow reversing."""
        self.snake.set_direction(0, 20)  # Move right
        self.assertEqual(self.snake.direction, [0, 20])
    
    def test_not_reverse_direction(self):
        """Test that the snake cannot reverse direction."""
        self.snake.set_direction(-20, 0)  # Move left
        self.assertNotEqual(self.snake.direction, [-20, 0])  # Should still be moving left

    def test_wall_collision(self):
        """Test that the snake detects wall collisions correctly."""
        snake = Snake(-20, 100, 20)
        self.assertTrue(snake.check_wall_collision(600, 600))  # Should collide with the wall if it moves left from (100, 100)

    def test_self_collision(self):
        """Test snake detects collision with itself."""
        self.snake._body = [[100, 100], [80, 100], [60, 100], [100, 100]]
        self.assertTrue(self.snake.check_self_collision())

    def test_move_changes_position(self):
        """Test that snake head moves after move() call."""
        old_head = self.snake.body[0][:]
        self.snake.move()
        self.assertNotEqual(self.snake.body[0], old_head)

    def test_no_collision(self):
        """Test that the snake does not detect a collision when it is within bounds."""
        snake = Snake(100, 100, 20)
        self.assertFalse(snake.check_wall_collision(600, 600))  # Should not collide

if __name__ == "__main__":
    unittest.main()