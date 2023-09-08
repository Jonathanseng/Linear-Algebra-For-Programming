def is_vector_space(V):
  """
  Checks if V is a vector space.

  Args:
    V: A set of vectors.

  Returns:
    True if V is a vector space, False otherwise.
  """

  # Check if addition is closed.
  for v1 in V:
    for v2 in V:
      if v1 + v2 not in V:
        return False

  # Check if scalar multiplication is closed.
  for v in V:
    for c in [1, -1]:
      if c * v not in V:
        return False

  # Check if the zero vector exists.
  if [0] not in V:
    return False

  # Check if the additive inverse exists.
  for v in V:
    if -v not in V:
      return False

  return True
