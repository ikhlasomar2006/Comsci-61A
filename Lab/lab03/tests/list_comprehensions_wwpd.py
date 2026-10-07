from pytest_grader import points


@points(0)
def list_comprehensions_wwpd():
    """What Would Python Display?

    >>> [2 * x for x in range(4)]
    LOCKED: 90ed715bb8968cea
    >>> [y for y in [6, 1, 6, 1] if y > 2]
    LOCKED: dc6ad4f418c99999
    >>> [[1] + s for s in [[4], [5, 6]]]
    LOCKED: 962934db79d88563
    >>> [z + 1 for z in range(10) if z % 3 == 0]
    LOCKED: d673b9729b34ce52
    """
