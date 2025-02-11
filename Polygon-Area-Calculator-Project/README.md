# **Polygon Area Calculator**

FreeCodeCamp - **Scientific Computing with Python** (First Project)  

## 📌 **Project Overview**  

This project is a **Polygon Area Calculator** implemented using **Object-Oriented Programming (OOP)** principles. It includes two classes:

- `Rectangle`: Represents a rectangle with width and height attributes.
- `Square`: A subclass of `Rectangle` that represents a square.

## Features

### Rectangle Class
The `Rectangle` class includes the following functionalities:

- **Initialization**: Requires `width` and `height` as parameters.
- **Methods**:
  - `set_width(width)`: Sets the rectangle's width.
  - `set_height(height)`: Sets the rectangle's height.
  - `get_area()`: Returns the area `(width * height)`.
  - `get_perimeter()`: Returns the perimeter `(2 * width + 2 * height)`.
  - `get_diagonal()`: Returns the diagonal `((width ** 2 + height ** 2) ** 0.5)`.
  - `get_picture()`: Returns a string representation of the rectangle using `*`. If `width` or `height` > 50, it returns `'Too big for picture.'`.
  - `get_amount_inside(shape)`: Returns how many times another `Rectangle` or `Square` can fit inside this rectangle without rotation.
  - **String Representation**: Prints as `Rectangle(width=5, height=10)`.

### Square Class
The `Square` class inherits from `Rectangle` and has:

- **Initialization**: Accepts a single `side` parameter, setting both `width` and `height`.
- **Additional Method**:
  - `set_side(side)`: Updates both `width` and `height`.
- **Overridden Methods**:
  - `set_width(width)`: Updates both width and height.
  - `set_height(height)`: Updates both width and height.
- **String Representation**: Prints as `Square(side=9)`.

## Usage Example
Below is an example demonstrating how to use the `Rectangle` and `Square` classes:

```python
rect = Rectangle(10, 5)
print(rect.get_area())  # Output: 50
rect.set_height(3)
print(rect.get_perimeter())  # Output: 26
print(rect)  # Output: Rectangle(width=10, height=3)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())  # Output: 81
sq.set_side(4)
print(sq.get_diagonal())  # Output: 5.656854249492381
print(sq)  # Output: Square(side=4)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Output: 8
```

## Installation & Setup
No additional libraries are required. Simply run the Python script containing the class definitions and usage examples.

## License
This project is released under the **MIT License**.
