from typing import Callable, List
from random import random


class Matrix:
  def __init__(self, rows: int, cols: int):
    self.rows = rows
    self.cols = cols
    # self.data = FilledList(self.rows, None).map(lambda: FilledList(self.cols, 0))
    self.data = listMap(FilledList(self.rows, None), lambda e, i: FilledList(self.cols, 0))

  def copy(self):
    """Returns a new Matrix with the same data"""
    m = Matrix(self.rows, self.cols)
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        m.data[i][j] = self.data[i][j]
    return m

  @staticmethod
  def static_fromArray(arr: list):
    """Creates a new Matrix from a List"""
    return Matrix(len(arr), 1).map(lambda e, i, j: arr[i])

  @staticmethod
  def static_subtract(a, b):
    """Return a new Matrix a-b"""
    if (a.rows != b.rows or a.cols != b.cols):
      # print('Columns and Rows of A must match Columns and Rows of B.')
      return

    return Matrix(a.rows, a.cols).map(lambda _, i, j: a.data[i][j] - b.data[i][j])

  def toArray(self) -> List:
    """Returns a 1D List containing the Matrix data"""
    arr = []
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        arr.append(self.data[i][j])
    return arr

  def randomize(self):
    """Randomly sets all values to a float between -1 and 1"""
    return self.map(lambda e, i, j: (random() * 2) - 1)

  def add(self, n):
    """Adds a scalar value to every element of the Matrix OR adds another Matrix to this Matrix"""
    if isinstance(n, Matrix):
      if (self.rows != n.rows or self.cols != n.cols):
        # print('Columns and Rows of A must match Columns and Rows of B.')
        return
      return self.map(lambda e, i, j: e + n.data[i][j])
    else:
      return self.map(lambda e, i, j: e + n)

  @staticmethod
  def static_transpose(matrix):
    """Returns the transposed Matrix"""
    return Matrix(matrix.cols, matrix.rows).map(lambda _, i, j: matrix.data[j][i])

  @staticmethod
  def static_multiply(a, b):
    """Returns the Matrix product of a and b, i.e. a×b"""
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
    """Performs a scalar multiplication or a hadamard multiplication on the Matrix"""
    if isinstance(n, Matrix):
      if (self.rows != n.rows or self.cols != n.cols):
        # print('Columns and Rows of A must match Columns and Rows of B.')
        return

      # Hadamard product
      return self.map(lambda e, i, j: e * n.data[i][j])
    else:
      # Scalar product
      return self.map(lambda e, i, j: e * n)

  def map(self, func):
    """Applies a function to every single element of the matrix"""
    for i in range(0, self.rows):
      for j in range(0, self.cols):
        val = self.data[i][j]
        self.data[i][j] = func(val, i, j)
    return self

  @staticmethod
  def static_map(matrix, func):
    """Apply a function to every element of matrix"""
    return Matrix(matrix.rows, matrix.cols).map(lambda e, i, j: func(matrix.data[i][j], i, j))

  #def printData(self):
  #  print(self.data);
  #  return self;


def FilledList(size=0, fill=None) -> List:
  return [fill]*size

def listMap(list: List, func: Callable) -> List:
  """Applies a function on every element of the list"""
  for i in range(len(list)):
    list[i] = func(list[i], i)

  return list