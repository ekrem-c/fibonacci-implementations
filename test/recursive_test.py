import unittest
from fibonacci_base_test import FibonacciTest
from src.fibonacci_recursive import fibonacci

class TestFibonacciRecursive(FibonacciTest, unittest.TestCase):
  def create_fibonacci(self):
    return fibonacci