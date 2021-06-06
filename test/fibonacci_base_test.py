import unittest

class FibonacciTest():
  def setUp(self):
    self.fibonacci = self.create_fibonacci()

  def test_canary(self):
    self.assertTrue(True)

  def test_for_positions(self):
    for(position, expected) in [(0, 1), (1, 1), (2, 2), (3, 3), (5, 8), (10, 89)]:
      self.check_fibonacci(position, expected)

  def check_fibonacci(self, position, expected):
    self.assertEqual(expected, self.fibonacci(position))

  def test_negative_one_fib(self):
    self.assertRaisesRegex(IndexError, "Can't calculate fibonacci for negative values", self.fibonacci, -1)
