"""Lab 5: Trees."""


from __future__ import annotations
from tree import Tree, is_leaf


def sprout_leaves[T](t: Tree[T], leaves: list[T]) -> Tree[T]:
  """Sprout new leaves containing the labels in leaves at each leaf of
  the original tree t and return the resulting tree.

  >>> t = Tree(1, [Tree(2), Tree(3)])
  >>> print(t)
  1
    2
    3
  >>> print(sprout_leaves(t, [4, 5]))
  1
    2
      4
      5
    3
      4
      5

  >>> u = Tree(1, [Tree(2, [Tree(3)])])
  >>> print(u)
  1
    2
      3
  >>> print(sprout_leaves(u, [6, 1, 2]))
  1
    2
      3
        6
        1
        2
  """

  "*** YOUR CODE HERE ***"  # replace the code below
  for i in t.branches:
    if not is_leaf(i):
        sprout_leaves(i, leaves)
    else:
        for j in leaves:
            i.branches.append(Tree(j))

  return t
  

def pathsum(t: Tree[int], n: int) -> bool:
  """Return whether there is a path from the root of t to a leaf whose
  labels sum to n.

  >>> t = Tree(2, [Tree(3, [Tree(5), Tree(7)]), Tree(4)])
  >>> pathsum(t, 12) # 2 -> 3 -> 7
  True
  >>> pathsum(t, 5)  # A path that doesn't reach a leaf such as 2 -> 3 doesn't count
  False
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  if not t.branches:
     return t.label == n
  for i in t.branches:
     if pathsum(i, n - t.label):
        return True
  return False
  


def prune_leaves[T](t: Tree[T], vals: tuple[T, ...]) -> Tree[T] | None:
  """Return a version of t with all leaves that have a label
  that appears in vals removed.  Return None if the entire tree is
  pruned away.

  >>> t = Tree(2)
  >>> print(prune_leaves(t, (1, 2)))
  None
  >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
  >>> print(numbers)
  1
    2
    3
      4
      5
    6
      7
  >>> print(prune_leaves(numbers, (3, 4, 6, 7)))
  1
    2
    3
      5
    6
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  for i in t.branches[:]:
        if is_leaf(i):
            if i.label in vals:
                t.branches.remove(i)
        else:
            prune_leaves(i, vals)

  return None if t.label in vals and t.branches == [] else t


def sum_tree(t: Tree[int]) -> int:
  """Add all elements in a tree.

  >>> t = Tree(4, [Tree(2, [Tree(3)]), Tree(6)])
  >>> sum_tree(t)
  15
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  return 0

def balanced(t: Tree[int]) -> bool:
  """Checks if each branch has same sum of all elements and
  if each branch is balanced.

  >>> t = Tree(1, [Tree(3), Tree(1, [Tree(2)]), Tree(1, [Tree(1), Tree(1)])])
  >>> balanced(t)
  True
  >>> u = Tree(1, [t, Tree(1)])
  >>> balanced(u)
  False
  >>> t = Tree(1, [Tree(4), Tree(1, [Tree(2), Tree(1)]), Tree(1, [Tree(3)])])
  >>> balanced(t)
  False
  """
  "*** YOUR CODE HERE ***"  # replace the code below
  return False
