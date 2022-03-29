"""
CS3C, Assignment #4, Pascals Triang;e
Gabriel Alon
Driver File
List containing the sequence of numbers appearing in the nth line of Pascal's triangle.
"""
"""
Run-Time Complexity: O(n^2). There are n rows, where each row has at most n cells (usually less)
Each row is calculated once and is saved for the next row to retrive. 
Each cell in a row requires at most two retrieval operations from a list
which is effectively a constant time operation.

"""

from Assignment4.gabrielalonLab4 import *
import time

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(0))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(1))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(2))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(3))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(4))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(5))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(6))
duration = time.perf_counter() - start
print(duration)

start = time.perf_counter()
new_triangle = pascal_triangle()
(new_triangle.pascal(11))
duration = time.perf_counter() - start
print(duration)

"""
row 0 [1]
3.836299999999959e-05
row 0 [1]
row 1 [1, 1]
2.0960000000000423e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
3.29489999999974e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
row 3 [1, 3, 3, 1]
3.753399999999879e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
row 3 [1, 3, 3, 1]
row 4 [1, 4, 6, 4, 1]
4.834799999999667e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
row 3 [1, 3, 3, 1]
row 4 [1, 4, 6, 4, 1]
row 5 [1, 5, 10, 10, 5, 1]
6.158199999999753e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
row 3 [1, 3, 3, 1]
row 4 [1, 4, 6, 4, 1]
row 5 [1, 5, 10, 10, 5, 1]
row 6 [1, 6, 15, 20, 15, 6, 1]
7.942699999999997e-05
row 0 [1]
row 1 [1, 1]
row 2 [1, 2, 1]
row 3 [1, 3, 3, 1]
row 4 [1, 4, 6, 4, 1]
row 5 [1, 5, 10, 10, 5, 1]
row 6 [1, 6, 15, 20, 15, 6, 1]
row 7 [1, 7, 21, 35, 35, 21, 7, 1]
row 8 [1, 8, 28, 56, 70, 56, 28, 8, 1]
row 9 [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
row 10 [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
row 11 [1, 11, 55, 165, 330, 462, 462, 330, 165, 55, 11, 1]
0.00014911299999999933
"""
