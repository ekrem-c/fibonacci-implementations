from fibonacci_base_test import FibonacciTest
from src.fibonacci_functional import fibonacci
import unittest

class TestFibonacciFunctional(FibonacciTest, unittest.TestCase):
  def create_fibonacci(self):
    return fibonacci
