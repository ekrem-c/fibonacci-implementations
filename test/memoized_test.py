import unittest
import time
from fibonacci_base_test import FibonacciTest
from src.fibonacci_memoized import fibonacci
from src.fibonacci_recursive import fibonacci as recursive_fibonacci

class TestFibonacciMemoized(FibonacciTest, unittest.TestCase):
  def create_fibonacci(self):
    return fibonacci

  def test_is_memo_faster(self):
    self.assertTrue(measure_time(fibonacci) * 4 < measure_time(recursive_fibonacci))

def measure_time(function):
  initial_time = time.time()
  function(20)
  return time.time() - initial_time
