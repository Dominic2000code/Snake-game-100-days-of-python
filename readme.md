# Snake Game with Python and Turtle - 100 days of python

---
This is a classic Snake game implemented using Python and Turtle graphics.

## Overview

The Snake game consists of the following files:

- `main.py`: Main script to run the game.
- `snake.py`: Defines the Snake class and its functionalities.
- `food.py`: Defines the Food class and its functionalities.
- `score_board.py`: Defines the ScoreBoard class to keep track of the player's score.

## Running the Game

To play the game, run the `main.py` script. You can control the snake using the arrow keys (Up, Down, Left, Right). The objective is to eat the food and avoid colliding with the walls or the snake's body.

## Files Description

### `main.py`

- Initializes the game screen.
- Creates instances of the Snake, Food, and ScoreBoard classes.
- Listens for keyboard input to control the snake's movement.
- Checks for collisions and updates the game state accordingly.

### `snake.py`

- Defines the Snake class.
- Initializes the snake's attributes such as color, and starting positions.
- Contains methods to create the snake, add segments, grow the snake, move the snake, and handle direction changes.

### `food.py`

- Defines the Food class.
- Initializes the food's attributes such as shape, color, and position.
- Contains a method to refresh the food's position when eaten by the snake.

### `score_board.py`

- Defines the ScoreBoard class.
- Initializes the score and displays it on the screen.
- Contains methods to increase the score, update the score display, and show the game over message.

## Dependencies

The game requires the Turtle module, which is included in the Python Standard Library.

## Gameplay

- Use the arrow keys to control the snake's movement.
- Eat the food to increase your score.
- Avoid colliding with the walls or the snake's body.
- The game ends when the snake collides with the walls or itself.

---