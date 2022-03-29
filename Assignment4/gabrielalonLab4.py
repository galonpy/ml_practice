"""
CS3C, Assignment #4, Pascals Triang;e
Gabriel Alon
Main File
List containing the sequence of numbers appearing in the nth line of Pascal's triangle.
"""


class pascal_triangle:
    def __init__(self):
        self.row_num = 0

    def pascal(self, n):
        if n == 0:
            data = [1]
            print(f"row {self.row_num} {data}")
            self.row_num += 1
            return data
        elif n == 1:
            self.pascal(0)
            data = [1, 1]
            print(f"row {self.row_num} {data}")
            self.row_num += 1
            return data
        else:
            result = (self.pascal(n - 1))
            data = [1]
            for i in range(1, n):
                data.append(result[i - 1] + result[i])
            data.append(1)
            print(f"row {self.row_num} {data}")
            self.row_num += 1
            return data
