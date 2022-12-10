from lib.template import Solution
from lib.helper import load_input_lines


def parse(data):
    cycle, x = 1, 1
    parsed = {}
    for line in data:
        match line.split():
            case ["addx", val]:
                parsed[cycle], parsed[cycle+1] = x, x
                x += int(val)
                cycle += 2
            case ["noop"]:
                parsed[cycle] = x
                cycle += 1
    return parsed


class Day(Solution):
    def get_input(self, path):
        data = load_input_lines(path)
        return parse(data)

    def part1(self):
        cycles = range(20, 221, 40)
        return sum(cycle*self.data[cycle] for cycle in cycles)

    def part2(self):
        sprite = [-1, 0, 1]
        drawn = ['']
        for k, v in self.data.items():
            print(k, v)
            drawn[-1] += ('#' if (k % 40) - v - 1 in sprite else '.')
            if not k % 40:
                drawn.append("")
        for line in drawn:
            print(line)
        return 0
