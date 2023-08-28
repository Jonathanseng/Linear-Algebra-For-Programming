class Group:
  """A group is a set with a binary operation that is associative, has an identity element, and every element has an inverse."""

  def __init__(self, elements, operation):
    """Creates a group.

    Args:
      elements: The elements of the group.
      operation: The binary operation on the group.
    """
    self.elements = elements
    self.operation = operation

  def __repr__(self):
    """Returns a string representation of the group."""
    return "Group(%s, %s)" % (self.elements, self.operation)

  def __eq__(self, other):
    """Returns True if the group is equal to other, False otherwise."""
    return (self.elements == other.elements and
            self.operation == other.operation)

  def is_group(self):
    """Returns True if the group is a group, False otherwise."""
    # Check that the operation is associative.
    for a in self.elements:
      for b in self.elements:
        for c in self.elements:
          if (self.operation(self.operation(a, b), c) !=
              self.operation(a, self.operation(b, c))):
            return False
    # Check that the group has an identity element.
    for a in self.elements:
      if not self.operation(a, self.identity()) == a:
        return False
    # Check that every element has an inverse.
    for a in self.elements:
      if not self.operation(a, self.inverse(a)) == self.identity():
        return False
    return True

  def identity(self):
    """Returns the identity element of the group."""
    for a in self.elements:
      for b in self.elements:
        if self.operation(a, b) == b:
          return a
    return None

  def inverse(self, a):
    """Returns the inverse of a in the group."""
    for b in self.elements:
      if self.operation(a, b) == self.identity():
        return b
    return None
