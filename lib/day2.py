from lib.template import Solution
from lib.helper import load_input_lines

class Day(Solution):
    def get_input(self, path):
        data = load_input_lines(path)
        return data

    def part1(self):
        scoring = {"A X": 4, "B X": 1, "C X": 7,
        "A Y": 8, "B Y": 5, "C Y": 2,
        "A Z": 3, "B Z": 9, "C Z": 6,}
        return sum(scoring[l] for l in self.data)

    def part2(self):
        scoring = {"A X": 3, "B X": 1, "C X": 2,
        "A Y": 4, "B Y": 5, "C Y": 6,
        "A Z": 8, "B Z": 9, "C Z": 7,}
        return sum(scoring[l] for l in self.data)
