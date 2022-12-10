from dataclasses import dataclass
from copy import copy

from lib.template import Solution
from lib.helper import load_input_lines


@dataclass
class Tree:
    visible: list[bool]
    height: int

class Day(Solution):
    def get_input(self, path):
        chart = {}
        data = load_input_lines(path)
        for y, line in enumerate(data):
            for x, h in enumerate(line):
                chart[x+1J*y] = Tree([False]*4, int(h))
        return chart, x+1, y+1

    def part1(self):
        chart, len_x, len_y  = self.data
        ranges = [(range(len_x), range(len_y-1, -1, -1), (1, 1j)), (range(len_y), range(len_x), (1j, 1)), (range(len_y), range(len_x-1, -1, -1), (1j, 1)), (range(len_x), range(len_y), (1,1J))]
        for i, (first, second, direction) in enumerate(ranges):
            for x in first:
                max_h = -1
                for y in second:
                    tree = chart[x*direction[0]+y*direction[1]]
                    if max_h < tree.height:
                        max_h = tree.height
                        tree.visible[i] = True
        return sum(any(tree.visible) for tree in chart.values())

    def part2(self):
        chart, _, _ = self.data
        result = {}
        for coord, tree in chart.items():
            value = 1
            for direction in (-1J, -1, 1, 1J):
                tracker = copy(coord)
                tracker += direction
                view = 0
                while current := chart.get(tracker):
                    view += 1
                    if current.height >= tree.height:
                        break
                    tracker += direction
                value *= view
            result[coord] = value

        return max(result.values())
