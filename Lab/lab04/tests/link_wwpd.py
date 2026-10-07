from pytest_grader import points


@points(0)
def link_wwpd():
    """What Would Python Display?

    >>> from lab04 import Link
    >>> a = Link(1000)
    >>> a.first
    LOCKED: 643dd75c0af30998
    >>> a.rest    # the empty linked list is ()
    LOCKED: 144797e3604a66aa
    >>> print(a)  # printing a linked list shows all its items in parentheses
    LOCKED: 7e9888098a737aa6

    >>> b = Link(1, Link(2, Link(3)))
    >>> print(b)
    LOCKED: 4adb026e39df23be
    >>> b.first
    LOCKED: ad2fb42ef006689f
    >>> b.rest.rest.first
    LOCKED: d3ff2998d85cf0bf
    >>> b.rest.rest.rest
    LOCKED: 985f1eb3f479036d
    >>> skip = Link(9001, b.rest.rest)
    >>> skip.first
    LOCKED: 87049e9e29451cea
    >>> skip.rest.first
    LOCKED: a0cca5c8029f0f78
    >>> skip.rest.rest
    LOCKED: 7666bc22d7a9e343
    >>> b.rest.first
    LOCKED: f60539d6a5fca4ff
    >>> print(Link(4, b))
    LOCKED: e4c100ee9f6e49ed

    >>> c = Link(Link(1), Link(2))
    >>> c.first.first
    LOCKED: 783aacd082b5b386
    >>> c.first.rest
    LOCKED: 9adb75b806a011de
    >>> c.rest.first
    LOCKED: 3cf8ebf38c5ab48d
    >>> print(c)
    LOCKED: 2db2f09014379ed8

    >>> d = Link(5, Link(6, Link(7)))
    >>> print(d)
    LOCKED: 1d1462cd6c62ea99
    >>> print(d.rest.rest)
    LOCKED: 48b801dee1072b80
    >>> print(Link(8, Link(9, d.rest)))
    LOCKED: 804061490df72c43
    >>> print(Link(10, Link(d.rest.rest, d.rest)))
    LOCKED: 071b95ab29191a1a

    >>> print(Link(5, 6))  # doctest: +IGNORE_EXCEPTION_DETAIL
    LOCKED: 8e9797d2181f5204
    """
