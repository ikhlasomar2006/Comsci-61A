from pytest_grader import points


@points(0)
def lists_wwpd():
    """What Would Python Display?

    >>> s = [7//3, 5, [4, 0, 1], 2]
    >>> s[0]
    LOCKED: aace9412eebfd83d
    >>> s[2]
    LOCKED: ad5fee6465d9fc17
    >>> s[-1]
    LOCKED: 429e95eadcc0bd96
    >>> len(s)
    LOCKED: b2c02887d44e58be
    >>> 4 in s
    LOCKED: cbdff137649a9e61
    >>> 4 in s[2]
    LOCKED: c8eb4c081e2beaa4
    >>> s[2] + [3 + 2]
    LOCKED: 6fec33f2d0bf906c
    >>> 5 in s[2]
    LOCKED: 6f6d0a45d266e495
    >>> s[2] * 2
    LOCKED: 3d5f0e5fc5f48170
    >>> list(range(3, 6))
    LOCKED: 3d36249901cbbc6d
    >>> range(3, 6)
    LOCKED: a4015c268d5a51e7
    >>> r = range(3, 6)
    >>> [r[0], r[2]]
    LOCKED: 28a5d80491af3616
    >>> range(4)[-1]
    LOCKED: 9756b5abe50737fe
    """
