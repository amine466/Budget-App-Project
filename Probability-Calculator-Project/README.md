# **Probability Calculator Project** 

FreeCodeCamp - **Scientific Computing with Python** (Last Project)  

## 📌 **Project Overview**  
This project simulates drawing balls from a hat and calculates the probability of drawing a specific combination of balls. The simulation is based on random experiments and provides an approximation of the desired probability.

## Problem Statement

You are tasked with calculating the probability of drawing a certain combination of balls from a hat. The hat contains various colored balls, and you need to estimate the probability of drawing a specific set of balls. The program will perform a number of experiments and calculate the approximate probability.

## Project Breakdown

### 1. **Hat Class (main.py)**

The `Hat` class represents a hat containing colored balls. The constructor of the class takes a variable number of arguments that specify how many balls of each color are in the hat. It stores the balls as a list of strings, where each string represents a ball of a specific color.

#### Example Usage:
```python
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
```
### 2. **Drawing Balls**
The `Hat` class also has a `draw` method. This method accepts an argument indicating how many balls to draw from the hat. The balls are selected randomly, and they are not returned to the hat after the draw.

Example Usage:
```python
drawn_balls = hat1.draw(4)
```

### 3. **Experiment Function (main.py)**
The `experiment` function calculates the probability of drawing a specific combination of balls from the hat. It performs multiple experiments (based on the number of experiments you specify) and checks if the combination you expect appears in the drawn balls. The function returns the estimated probability.

Function Signature:
```python
def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
```
- `hat`: The hat object containing the balls.
- `expected_balls`: A dictionary representing the exact combination of balls to try to draw (e.g., {'red': 2, 'green': 1}).
- `num_balls_drawn`: The number of balls to draw in each experiment.
- `num_experiments`: The number of experiments to perform.

Example Usage:
```python
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, 
                         expected_balls={'red': 2, 'green': 1}, 
                         num_balls_drawn=5, 
                         num_experiments=2000)
```
The result would be something like this:
```python
0.356
```
### 4. **Randomness**
Since this experiment is based on random draws, the probability will slightly vary each time the program is run.

### 5. **Hint**
Consider using the modules that are already imported at the top of the file. Do not initialize the random seed within the file.
