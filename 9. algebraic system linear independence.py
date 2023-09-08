def is_linearly_independent(S):
  """
  Checks if S is a linearly independent set.

  Args:
    S: A set of vectors.

  Returns:
    True if S is a linearly independent set, False otherwise.
  """

  # Check if any vector in S can be written as a linear combination of other vectors in S.
  for i in range(len(S)):
    for j in range(i + 1, len(S)):
      if S[i] == sum(c * S[j] for c in [1, -1]):
        return False

  return True
