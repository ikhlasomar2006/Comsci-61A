"""Lab 4: Linked Lists."""


from __future__ import annotations
from link import Link, LinkedList



def change[T](s: LinkedList[T], old: T, new: T) -> LinkedList[T]:
    """Returns a linked list matching s but with all instances of old (if any)
    replaced by new.

    >>> s = Link(1, Link(2, Link(3)))
    >>> t = change(s, 3, 1)
    >>> print(t)
    (1 2 1)
    >>> u = change(t, 1, 2)
    >>> print(u)
    (2 2 2)
    >>> v = change(u, 5, 1)
    >>> print(v)
    (2 2 2)
    >>> print(s)   # The original linked list s is unchanged.
    (1 2 3)
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    def helper(z):
        if z == ():
            return ()
        if z.first == old:
            return Link(new, helper(z.rest))
        return Link(z.first, (helper(z.rest)))

    return helper(s)



def without(s: LinkedList, i: int) -> LinkedList:
    """Return a linked list like s but without the element at index i.

    >>> s = Link(3, Link(5, Link(7, Link(9))))
    >>> print(without(s, 0))
    (5 7 9)
    >>> print(without(s, 2))
    (3 5 9)
    >>> print(without(s, 4))  # There is no index 4, so all of s is retained.
    (3 5 7 9)
    >>> print(s)              # The original linked list s is unchanged.
    (3 5 7 9)
    >>> without((), 0)
    ()
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    def helper(x, counter):
        if x == ():
            return ()
        if counter == i:
            return helper(x.rest, counter + 1)
        return Link(x.first, (helper(x.rest, counter + 1)))

    return helper(s, 0)


def print_every_other(s: LinkedList) -> None:
    """Print every other element of linked list s, starting with the first.

    >>> sentence = Link('I', Link('have', Link('love', Link('for', Link('Oski')))))
    >>> print_every_other(sentence)
    I
    love
    Oski
    >>> print_every_other(Link(1, Link(2, Link(3, Link(4)))))
    1
    3
    >>> print_every_other(Link(5))
    5
    >>> print_every_other(())
    """
    "*** YOUR CODE HERE ***"
    def helper(x, counter):
        if x == ():
            return
        elif counter % 2 == 0:
            print(x.first)
        return helper(x.rest, counter + 1)

    return helper(s, 0)

def store_digits(n: int) -> LinkedList[int]:
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(first=1, rest=())
    >>> print(store_digits(2345))
    (2 3 4 5)
    >>> print(store_digits(876))
    (8 7 6)
    >>> print(store_digits(2450))
    (2 4 5 0)
    >>> print(store_digits(20105))
    (2 0 1 0 5)
    >>> # a check that you do not use str or reversed
    >>> import inspect, ast
    >>> [n.id for n in ast.walk(ast.parse(inspect.getsource(store_digits)))
    ...  if isinstance(n, ast.Name) and n.id in ('str', 'reversed')]
    []
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    def helper(x):
        if x == 0:
            return ()
        return Link((x % 10), helper(x // 10))

    copy = helper(n)

    def reverse(x, y):
        if x is ():
            return y
        return reverse(x.rest, Link(x.first, y))

    return reverse(copy, ())


def linked_sum(s: LinkedList[int], total: int) -> int:
    """Return the number of combinations of elements in s that
    sum up to total.

    >>> # Four combinations: 1 1 1 1 , 1 1 2 , 1 3 , 2 2
    >>> linked_sum(Link(1, Link(2, Link(3, Link(5)))), 4)
    4
    >>> linked_sum(Link(2, Link(3, Link(5))), 1)
    0
    >>> # One combination: 2 3
    >>> linked_sum(Link(2, Link(4, Link(3))), 5)
    1
    """
    if total == 0:
        return 1
    elif total < 0 or s is ():
        return 0
    else:
        with_first = linked_sum(s, total - s.first)
        without_first = linked_sum(s.rest, total)
        return with_first + without_first


def max_pair_sum(s: LinkedList[int]) -> int:
    """Return the largest sum of values in a pairing for a linked list of positive numbers s.

    >>> L = Link                                                     # Abbreviate Link
    >>> max_pair_sum(L(3, L(4, L(5, L(3, L(4, L(5, L(6))))))))       # 4+5 + 5+6
    20
    >>> max_pair_sum(L(3, L(4, L(5, L(3, L(4, L(5, L(6, L(3))))))))) # 3+4 + 3+4 + 6+3
    23
    """
    if s is () or s.rest is ():
        return 0
    n = s.first + s.rest.first
    if not isinstance(s.rest.rest, Link):
        return n
    else:
        return max(n + max_pair_sum(s.rest.rest.rest), max_pair_sum(s.rest))
