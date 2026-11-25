# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. According to the docstring "true for even numbers", it should return `True` when `n` is even, which means `n % 2 == 0`.
Example: is_even(4) returns False, expected True.
Fix: return n % 2 == 0

Line: 8
Problem: The function calculates the sum of width and height, but the docstring states "area of a rectangle", which should be width multiplied by height.
Example: rectangle_area(5, 3) returns 8, expected 15.
Fix: return width * height

Line: 13
Problem: The function adds 2 to n, but the docstring says "twice the number n", meaning it should return `n * 2`, not `n + 2`.
Example: double(5) returns 7, expected 10.
Fix: return n * 2
