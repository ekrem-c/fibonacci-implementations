def fibonacci(position, recursion = None):
  recursion = recursion or fibonacci

  if position < 0:
    raise IndexError("Can't calculate fibonacci for negative values")

  if position < 2:
    return 1

  return recursion(position - 1) + recursion(position - 2)