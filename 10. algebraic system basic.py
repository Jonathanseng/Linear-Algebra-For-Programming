def is_basic(S):
  """
  Checks if S is a basic set of vectors.

  Args:
    S: A set of vectors.

  Returns:
    True if S is a basic set of vectors, False otherwise.
  """

  # Check if S is linearly independent.
  if not is_linearly_independent(S):
    return False

  # Check if S spans V.
  if not is_spanning_set(S, S):
    return False

  return True
