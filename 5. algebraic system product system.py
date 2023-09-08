def product_system(V1, V2):
  """
  Returns the product system of V1 and V2.

  Args:
    V1: A vector space.
    V2: A vector space.

  Returns:
    A vector space that is the product of V1 and V2.
  """

  # Create the set of all pairs of vectors (v1, v2).
  S = set()
  for v1 in V1:
    for v2 in V2:
      S.add((v1, v2))

  # Check if addition is closed.
  for (v11, v12), (v21, v22) in itertools.combinations(S, 2):
    if (v11 + v21, v12 + v22) not in S:
      return None

  # Check if scalar multiplication is closed.
  for (v1, v2) in S:
    for c in [1, -1]:
      if (c * v1, c * v2) not in S:
        return None

  return S
