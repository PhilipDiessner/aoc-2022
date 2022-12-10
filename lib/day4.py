from lib.template import Solution
from lib.helper import load_input_lines


class Day(Solution):
    def get_input(self, path):
        data = load_input_lines(path)

        def split_line(line):
            return [[int(sec) for sec in elf.split("-") ]for elf in line.split(",")]

        return [split_line(line) for line in data]

    def part1(self):
        count = 0
        for numbers in self.data:
            if (numbers[0][0] >= numbers[1][0] and numbers[0][1] <= numbers[1][1]) or (numbers[0][0] <= numbers[1][0] and numbers[0][1] >= numbers[1][1]):
                count  += 1
        return count

    def part2(self):
        count = 0
        for numbers in self.data:
            if max(numbers[0][0], numbers[1][0]) <= min(numbers[0][1], numbers[1][1]):
                count  += 1
        return count
