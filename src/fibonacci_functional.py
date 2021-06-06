from functools import reduce

def fibonacci(position):
  if position < 0:
      raise IndexError("Can't calculate fibonacci for negative values")

  return reduce(lambda series, _: [series[1], sum(series)], range(position), [0, 1])[1]
