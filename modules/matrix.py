from typing import List
from random import random


class Matrix:
  def __init__(self, rows, cols):
    self.rows = rows
    self.cols = cols
    self.data = FilledList(self.rows, None).map(lambda: FilledList(self.cols, 0))

  def copy(self):
    m = Matrix(self.rows, self.cols)
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        m.data[i][j] = self.data[i][j]
    return m

  def static_fromArray(self, arr):
    return Matrix(arr.length, 1).map(lambda e, i: arr[i])

  def static_subtract(self, a, b):
    if (a.rows != b.rows or a.cols != b.cols):
      # print('Columns and Rows of A must match Columns and Rows of B.')
      return

    # Return a new Matrix a-b
    return Matrix(a.rows, a.cols).map(lambda _, i, j: a.data[i][j] - b.data[i][j])

  def toArray(self):
    arr = []
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        arr.append(self.data[i][j])
    return arr

  def randomize(self):
    return self.map(lambda e: (random() * 2) - 1)

  def add(self, n):
    if isinstance(n, Matrix):
      if (self.rows != n.rows or self.cols != n.cols):
        # print('Columns and Rows of A must match Columns and Rows of B.')
        return
      return self.map(lambda e, i, j: e + n.data[i][j])
    else:
      return self.map(lambda e: e + n)

  def static_transpose(self, matrix):
    return Matrix(matrix.cols, matrix.rows).map(lambda _, i, j: matrix.data[j][i])

  def static_multiply(self, a, b):
    # Matrix product
    if (a.cols != b.rows):
      # print('Columns of A must match rows of B.');
      return
    
    def mapFuncToPassAsArg(e, i, j):
        # Dot product of values in col
        sum = 0
        for k in range(0, a.cols):
          sum += a.data[i][k] * b.data[k][j]
        return sum
    return Matrix(a.rows, b.cols).map(mapFuncToPassAsArg)

  def multiply(self, n):
    if isinstance(n, Matrix):
      if (self.rows != n.rows or self.cols != n.cols):
        # print('Columns and Rows of A must match Columns and Rows of B.')
        return

      # Hadamard product
      return self.map(lambda e, i, j: e * n.data[i][j])
    else:
      # Scalar product
      return self.map(lambda e: e * n)

  def map(self, func):
    # Apply a function to every element of matrix
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        val = self.data[i][j]
        self.data[i][j] = func(val, i, j)
    return self

  def static_map(self, matrix, func):
    # Apply a function to every element of matrix
    return Matrix(matrix.rows, matrix.cols).map(lambda e, i, j: func(matrix.data[i][j], i, j))

  #def printData(self):
  #  print(self.data);
  #  return self;


def FilledList(size=0, fill=None):
    return [fill]*size