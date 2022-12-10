from collections import defaultdict

from lib.template import Solution
from lib.helper import load_input


class Day(Solution):
    def get_input(self, path):
        data = load_input(path)
        parts = data.split("\n\n")

        load =parts[0].split("\n")
        containers = [x[1::4] for x in load[:-1]]
        containers.reverse()
        columns = [int(x) for x in load[-1].split()]

        def get_load():
            load = defaultdict(lambda : [])
            for row in containers:
                for k, v in zip(columns, row):
                    if v != " ":
                        load[k].append(v)
            return load

        instructions = [[int(n) for n in x.split()[1::2]] for x in parts[1].split("\n")]
        return get_load, instructions, columns

    def part1(self):
        loading, instructions, columns =  self.data
        load = loading()
        for instruction in instructions:
            swap = load[instruction[1]][-instruction[0]:]
            swap.reverse()
            load[instruction[2]].extend(swap)
            load[instruction[1]] = load[instruction[1]][:-instruction[0]]
        return "".join(load[x][-1] for x in columns)

    def part2(self):
        loading, instructions, columns =  self.data
        load = loading()
        for instruction in instructions:
            load[instruction[2]].extend(load[instruction[1]][-instruction[0]:])
            load[instruction[1]] = load[instruction[1]][:-instruction[0]]
        return "".join(load[x][-1] for x in columns)
