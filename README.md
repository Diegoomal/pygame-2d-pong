# Pong Game in Pygame

This repository contains a classic 2D Pong game implemented using the Pygame library. The game is designed to be simple and easy to understand, with a focus on providing a fun, nostalgic gaming experience. The project is structured to be modular and maintainable, with clear separation between different game components.

## Features
- Classic Pong Gameplay: Relive the classic Pong experience with smooth paddle and ball movements.
- Object-Oriented Design: The game is implemented using object-oriented principles, making it easy to extend and maintain.
- Customizable Settings: Easily modify game settings such as screen dimensions, colors, paddle and ball speeds, and more.
- Score Display: Real-time score display to keep track of the game progress.
- Collision Detection: Accurate collision detection for paddle and ball interactions.
- Configurable Environment: Separate configuration file for easy customization of game settings.

## Project Structure
- main.py: The main file that initializes the game, handles the game loop, and manages user inputs.
- paddle.py: Defines the Paddle class, responsible for paddle attributes and movements.
- ball.py: Defines the Ball class, responsible for ball attributes and movements.
- environment.py: Defines the GameEnvironment class, responsible for drawing the game environment and displaying the score.
- config.py: Contains all configurable settings for the game, such as screen dimensions, colors, and speeds.

## Execute

Create CONDA env
```
conda env create -n pygame-2d-pong-env -f ./env.yml
```

Activate CONDA env
```
conda activate pygame-2d-pong-env
```

Execute game
```
python src/main.py
```

## Customization
You can customize the game settings by modifying the config.py file. This includes changing the screen width and height, colors, paddle and ball speeds, and more.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acnowledgements
This project is built using the Pygame library.
Inspired by the original Pong game created by Atari.
Enjoy the game!

## URL

[github](https://github.com/Diegoomal)