from dataclasses import dataclass, field
from functools import reduce

from typing import Optional

from lib.template import Solution
from lib.helper import load_input_lines


@dataclass
class Node:
    parent: Optional['Node']
    children: dict['Node'] = field(default_factory=lambda: {})
    files: dict[str, int] = field(default_factory=lambda: {})
    _size: Optional[int] = None

    @property
    def size(self, calc=False):
        if not self._size or calc:
            self._size = sum(self.files.values()) + \
                     sum(x.size for x in self.children.values())
        return self._size

    def flatten_children(self):
        if self.children:
            return reduce(lambda a,b: a+b,
                            [x.flatten_children() for x in self.children.values()],
                            list(self.children.values()))
        return []

    def flatten(self):
        return reduce(lambda a,b: a+b,
                            [x.flatten() for x in self.children.values()],
                            [self])


# assume that only the the first line calls / as absolute, all other are relative
# assume that only after a ls lines with no $ might happen
def parse(lines: list[str]):
    first = Node('/', None)
    current = first
    files, dirs = {}, {}
    ls_on = False
    for line in lines[1:]:
        match line.split():
            case ["$", *command]:
                match command:
                    case ["cd", target]:
                        if ls_on:
                            current.children, current.files = dirs, files
                            dirs, files = {}, {}
                            ls_on = False
                        if target == "..":
                            current = current.parent
                        else:
                            current = current.children[target]
                    case ["ls"]:
                        ls_on = True
            case [pre, name]:
                if pre == "dir":
                    dirs[name] = Node(current)
                else:
                    files[name] = int(pre)
    return first


class Day(Solution):
    def get_input(self, path):
        data = load_input_lines(path)
        return parse(data)

    def __init__(self, path) -> None:
        super().__init__(path)
        self.flatten = self.data.flatten()

    def part1(self):
        return sum(x.size for x in self.flatten if x.size <= 100000)

    def part2(self):
        total_size = 70_000_000
        required = 30_000_000
        limit = required + self.data.size - total_size
        return min(x.size for x in self.flatten if x.size>=limit)
