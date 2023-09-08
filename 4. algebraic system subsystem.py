def is_subsystem(S, V):
  """
  Checks if S is a subsystem of V.

  Args:
    S: A set of vectors.
    V: A vector space.

  Returns:
    True if S is a subsystem of V, False otherwise.
  """

  # Check if S is a subset of V.
  if not S.issubset(V):
    return False

  # Check if addition is closed in S.
  for v1 in S:
    for v2 in S:
      if v1 + v2 not in S:
        return False

  # Check if scalar multiplication is closed in S.
  for v in S:
    for c in [1, -1]:
      if c * v not in S:
        return False

  return True
