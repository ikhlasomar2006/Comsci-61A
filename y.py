from dataclasses import dataclass, field

@dataclass
class Tree[T]:
    label: T
    branches: list["Tree[T]"] = field(default_factory=list)

def is_leaf(t: Tree) -> bool:
    "Return whether a Tree t is a leaf with no branches."
    return not t.branches

def label(t: Tree[int]) -> int:
    return t.label


def only_paths(t: Tree[int], n: int) -> Tree[int] | None:

    if is_leaf(t) and n == 0:
        return t
    new_branches = [only_paths(b, n - b.label) for b in t.branches]
    if Tree(new_branches):
        return Tree(t.label, [b for b in new_branches if b])

