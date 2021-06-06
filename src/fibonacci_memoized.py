from fibonacci_recursive import fibonacci as recursive_fibonacci
from functools import partial

def fibonacci(position, cache_ref = [{}]):
  cache = cache_ref[0]

  if position < 0:
      raise IndexError("Can't calculate fibonacci for negative values")

  if position not in cache:
    cache[position] = recursive_fibonacci(position, partial(fibonacci, cache_ref = [cache]))

  return cache[position]

