def solve_system(a, b, c, d, e, f):
  """Solve the system of equations ax + by = c, dx + ey = f.

  Args:
    a: The coefficient of x in the first equation.
    b: The coefficient of y in the first equation.
    c: The constant term in the first equation.
    d: The coefficient of x in the second equation.
    e: The coefficient of y in the second equation.
    f: The constant term in the second equation.

  Returns:
    A tuple of (x, y), the solution to the system of equations.
  """

  x = (c * e - f * b) / (a * e - b * d)
  y = (c * d - a * f) / (a * e - b * d)
  return x, y


if __name__ == "__main__":
  a = 1
  b = 2
  c = 3
  d = 4
  e = 5
  f = 6

  x, y = solve_system(a, b, c, d, e, f)
  print("x = %f, y = %f" % (x, y))
