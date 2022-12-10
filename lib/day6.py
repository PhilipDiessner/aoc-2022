from lib.template import Solution
from lib.helper import load_input, start_of_packet

class Day(Solution):
    def get_input(self, path):
        data = load_input(path)
        return data

    def part1(self):
        return start_of_packet(self.data, n=4)

    def part2(self):
        return start_of_packet(self.data, n=14)
