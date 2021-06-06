def fibonacci(position):
  if position < 0:
    raise IndexError("Can't calculate fibonacci for negative values")

  previous, current = 0, 1

  for _ in range(position):
    previous, current = current, previous + current

  return current
