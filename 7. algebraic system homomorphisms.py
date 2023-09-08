def is_homomorphism(f, V1, V2):
  """
  Checks if f is a homomorphism from V1 to V2.

  Args:
    f: A function from V1 to V2.
    V1: A vector space.
    V2: A vector space.

  Returns:
    True if f is a homomorphism, False otherwise.
  """

  # Check if f preserves addition.
  for v1, v2 in itertools.combinations(V1, 2):
    if f(v1) + f(v2) != f(v1 + v2):
      return False

  # Check if f preserves scalar multiplication.
  for v in V1:
    for c in [1, -1]:
      if c * f(v) != f(c * v):
        return False

  return True
