"""Lab 3: Lists."""


def print_if(s: list[int], f) -> None:
    """Print each element of s for which f returns a true value.

    >>> print_if([3, 4, 5, 6], lambda n: n > 4)
    5
    6
    >>> result = print_if([3, 4, 5, 6], lambda n: n % 2 == 0)
    4
    6
    >>> print(result)  # print_if should return None
    None
    """
    for x in s:
        "*** YOUR CODE HERE ***"
        if f(x):
            print(x)
            


def close(s: list[int], k: int) -> int:
    """Return how many elements of s are within k of their index.

    >>> t = [6, 2, 4, 3, 5]
    >>> close(t, 0)  # Only 3 is equal to its index
    1
    >>> close(t, 1)  # 2, 3, and 5 are within 1 of their index
    3
    >>> close(t, 2)  # 2, 3, 4, and 5 are all within 2 of their index
    4
    >>> close(list(range(10)), 0)
    10
    """
    assert k >= 0
    count = 0
    for i in range(len(s)):  # Use a range to loop over indices
        "*** YOUR CODE HERE ***"
        if abs(s[i] - i) <= k:
            count += 1
    return count


from math import sqrt

def squares(s: list[int]) -> list[int]:
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """
    return [round(sqrt(n)) for n in s if round(sqrt(n)) == sqrt(sqrt(n) ** 2)]


def double_eights(n: int) -> bool:
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # This test checks that you used recursion, with no loops or `in`.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(double_eights))
    >>> banned = ['For', 'While', 'In', 'JoinedStr']
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in banned]
    []
    >>> # This test checks that you did not call the str function.
    >>> [x.id for x in ast.walk(tree) if type(x).__name__ == 'Name' and x.id == 'str']
    []
    """
    "*** YOUR CODE HERE ***"
    if n % 10 == 8 and (n // 10) % 10 == 8:
        return True
    elif n == 0:
        return False
    return double_eights(n // 10)
    

    

def flatten(s: list) -> list:
    """Returns a flattened version of list s, which contains lists and integers.

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> deep = [1, [[2], 3], 4, [[[[5], 6]], 7]]
    >>> flatten(deep)
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(deep[1])
    [2, 3]
    >>> deep                                # input list should be unchanged
    [1, [[2], 3], 4, [[[[5], 6]], 7]]
    """
    "*** YOUR CODE HERE ***"
    if len(s) == 0:
        return []
    elif type(s[-1]) == list:
        return flatten(s[:-1]) + flatten(s[-1])
    return flatten(s[:-1]) + [s[-1]]
    



def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952) # 7+3, 8+2, and 8+2
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469) # 9+1, 6+4, 6+4, 4+6, 1+9, 4+6
    6
    >>> # This test checks that you used recursion, with no loops.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(ten_pairs))
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in ['For', 'While']]
    []
    """
    "*** YOUR CODE HERE ***"


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5) # digit 5 appears 4 times in 55055
    4
    >>> # This test checks that you used recursion, with no loops.
    >>> import inspect, ast
    >>> tree = ast.parse(inspect.getsource(count_digit))
    >>> [type(x).__name__ for x in ast.walk(tree) if type(x).__name__ in ['For', 'While']]
    []
    """
    "*** YOUR CODE HERE ***"


def make_onion(f, g):
    """Return a function can_reach(x, y, limit) that returns
    whether some call expression containing only f, g, and x with
    up to limit calls will give the result y.

    >>> up = lambda x: x + 1
    >>> double = lambda y: y * 2
    >>> can_reach = make_onion(up, double)
    >>> can_reach(5, 25, 4)      # 25 = up(double(double(up(5))))
    True
    >>> can_reach(5, 25, 3)      # Not possible
    False
    >>> can_reach(1, 1, 0)      # 1 = 1
    True
    >>> add_ing = lambda x: x + "ing"
    >>> add_end = lambda y: y + "end"
    >>> can_reach_string = make_onion(add_ing, add_end)
    >>> can_reach_string("cry", "crying", 1)      # "crying" = add_ing("cry")
    True
    >>> can_reach_string("un", "unending", 3)     # "unending" = add_ing(add_end("un"))
    True
    >>> can_reach_string("peach", "folding", 4)   # Not possible
    False
    """
    def can_reach(x, y, limit):
        if limit < 0:
            return ____
        elif x == y:
            return ____
        else:
            return can_reach(____, ____, limit - 1) or can_reach(____, ____, limit - 1)
    return can_reach
