from lib.template import Solution
from lib.helper import load_input

class Day(Solution):
    def get_input(self, path):
        data = load_input(path)
        users = data.split("\n\n")
        self.users = sorted(sum(int(c) for c in user.split("\n")) for user in users)

    def part1(self):
        return self.users[-1]

    def part2(self):
        return sum(self.users[-3:])
