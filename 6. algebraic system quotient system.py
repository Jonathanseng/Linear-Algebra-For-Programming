def quotient_system(V, S):
  """
  Returns the quotient system of V and S.

  Args:
    V: A vector space.
    S: A subsystem of V.

  Returns:
    A vector space that is the quotient of V and S.
  """

  # Create the set of all vectors v in V such that v - s is in S for some s in S.
  Q = set()
  for v in V:
    for s in S:
      if v - s in S:
        Q.add(v)

  # Check if addition is closed.
  for v1 in Q:
    for v2 in Q:
      if v1 + v2 not in Q:
        return None

  # Check if scalar multiplication is closed.
  for v in Q:
    for c in [1, -1]:
      if c * v not in Q:
        return None

  return Q
