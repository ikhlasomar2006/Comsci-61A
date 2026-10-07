"""Homework 4: Recursive Data."""


from __future__ import annotations
from dataclasses import dataclass
from link import Link, LinkedList
from tree import Tree, is_leaf


type Structure = Mobile | Planet

@dataclass
class Mobile:
    left: Arm
    right: Arm

@dataclass
class Arm:
    length: int
    end: Structure

@dataclass
class Planet:
    mass: int

def examples():
    t = Mobile(Arm(1, Planet(2)),
               Arm(2, Planet(1)))
    u = Mobile(Arm(5, Planet(1)),
               Arm(1, Mobile(Arm(2, Planet(3)),
                             Arm(3, Planet(2)))))
    v = Mobile(Arm(4, t), Arm(2, u))
    return t, u, v

def total_mass(m: Structure) -> int:
    """Return the total mass of m, a Planet or Mobile.

    >>> total_mass(Planet(5))
    5
    >>> t, u, v = examples()
    >>> total_mass(t)
    3
    >>> total_mass(u)
    6
    >>> total_mass(v)
    9
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    def helper(thing):
        if isinstance(thing, Planet):
            return thing.mass
        
        if not(isinstance(thing, Mobile)):

            if isinstance(thing.end, Planet):
                return thing.end.mass

        left = helper(thing.left if isinstance(thing.left.end, Planet) else thing.left.end)
        right = helper(thing.right if isinstance(thing.right.end, Planet) else thing.right.end)

        return left + right

    return helper(m)

def balanced(m: Structure) -> bool:
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = Mobile(Arm(3, t), Arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(Mobile(Arm(1, v), Arm(1, p)))
    False
    >>> balanced(Mobile(Arm(1, p), Arm(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"  # replace the code below

    if isinstance(m, Planet):          # base case: a planet is always balanced
        return True

    left_torque = m.left.length * total_mass(m.left.end)
    right_torque = m.right.length * total_mass(m.right.end)

    return (left_torque == right_torque
            and balanced(m.left.end)
            and balanced(m.right.end))

def interleave[T](s: LinkedList[T],  t: LinkedList[T]) -> LinkedList[T]:
    """Interleave linked lists s and t to produce a new linked list.

    >>> evens = Link(2, Link(4, Link(6, Link(8))))
    >>> odds = Link(1, Link(3))
    >>> print(interleave(odds, evens))
    (1 2 3 4 6 8)
    >>> print(interleave(evens, odds))
    (2 1 4 3 6 8)
    >>> print(interleave(odds, odds))
    (1 1 3 3)
    >>> print(interleave((), odds))
    (1 3)
    >>> print(Link(evens, Link(odds)))  # should not change
    ((2 4 6 8) (1 3))
    """
    if s is () or t is ():
        return s if s is not () else t
    return Link(s.first, interleave(t, s.rest))
@dataclass
class Treasure:
    description: str
    weight: int
    worth: int

    def __str__(self):
        return self.description

trophy = Treasure('trophy', 2, 5)
gem = Treasure('gem', 4, 7)
ring = Treasure('ring', 1, 3)
crown = Treasure('crown', 6, 12)
vase = Treasure('vase', 3, 4)
orb = Treasure('orb', 5, 9)
gift = Treasure('gift', 1, 1)

def total_worth(s: LinkedList[Treasure]) -> int:
    """Return the total worth of the treasures in linked list s.

    >>> total_worth(Link(trophy, Link(ring)))
    8
    >>> total_worth(())
    0
    """
    total = 0
    while isinstance(s, Link):
        total, s = total + s.first.worth, s.rest
    return total

def knapsack(treasures: list[Treasure], max_weight: int) -> LinkedList[Treasure]:
    """Return a linked list of treasures with the largest total worth that do not
    exceed max_weight, in the same order as they appear in treasures.

    >>> print(knapsack([trophy, gem, ring], 6))
    (trophy gem)
    >>> print(knapsack([trophy, gem, ring], 7))
    (trophy gem ring)
    >>> print(knapsack([trophy, gem, ring, crown, vase], 8))
    (trophy crown)
    >>> print(knapsack([crown, orb, trophy, vase], 10))
    (orb trophy vase)
    >>> print(knapsack([gem, orb, ring, gift], 6))
    (orb ring)
    >>> knapsack([crown], 3)
    ()
    >>> knapsack([], 3)
    ()
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    
    def helper(t, mw):
        if not t or mw == 0:
            return ()
        if t[0].weight <= mw:
            value1 = Link(t[0], helper(t[1:], mw - t[0].weight))
            value2 = helper(t[1:], mw)  

            return value1 if total_worth(value1) > total_worth(value2) else value2
        else:
            return helper(t[1:], mw)
    
    return helper(treasures, max_weight)

def berry_finder(t: Tree) -> bool:
    """Return True if t contains the label 'berry' and False otherwise.

    >>> scrat = Tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = Tree('roots', [Tree('branch1', [Tree('leaf'), Tree('berry')]), Tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = Tree(1, [Tree(2), Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = Tree(1, [Tree('berry', [Tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"  # replace the code below
    def helper(x: Tree):
        if x.label == 'berry':
            return True
        for i in x.branches:
            if i.label == 'berry':
                return True
            if helper(i):
                return True 
        return False
    return helper(t) 
    



def max_path_sum(t: Tree[int]) -> int:
    """Return the maximum sum of labels along any path that starts at the root.

    >>> t = Tree(1, [Tree(5, [Tree(-1), Tree(-3)]), Tree(4)])
    >>> max_path_sum(t) # 1, 5
    6
    >>> u = Tree(5, [Tree(4, [Tree(1), Tree(3)]), Tree(-2, [Tree(10), Tree(-3)])])
    >>> max_path_sum(u) # 5, -2, 10
    13
    >>> v = Tree(-3, [Tree(-1), Tree(-2, [Tree(8)])])
    >>> max_path_sum(v) # -3, -2, 8
    3
    >>> w = Tree(-3, [Tree(-1), Tree(-2)])
    >>> max_path_sum(w) # -3
    -3
    """
    "*** YOUR CODE HERE ***"  # replace the code below

    def helper(t, counter):
        counter += t.label
        if is_leaf(t):
            return counter
        reuslts = []
        for i in t.branches:
            reuslts.append(helper(i, counter))
        return max([counter] + reuslts)
            

    return helper(t, 0)
    
