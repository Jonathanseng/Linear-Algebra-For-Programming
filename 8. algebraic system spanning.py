def is_spanning_set(S, V):
  """
  Checks if S is a spanning set of V.

  Args:
    S: A set of vectors.
    V: A vector space.

  Returns:
    True if S is a spanning set of V, False otherwise.
  """

  # Check if every vector in V can be written as a linear combination of vectors in S.
  for v in V:
    if not any(v == c * s for s in S for c in [1, -1]):
      return False

  return True
