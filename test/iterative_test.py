import unittest
from fibonacci_base_test import FibonacciTest
from src.fibonacci_iterative import fibonacci


class TestFibonacciIterative(FibonacciTest, unittest.TestCase):
  def create_fibonacci(self):
    return fibonacci

