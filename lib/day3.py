import string

from lib.template import Solution
from lib.helper import load_input_lines

class Day(Solution):

    def __init__(self, path) -> None:
        super().__init__(path)
        self.score = {l:i+1 for i,l in enumerate(string.ascii_letters)}

    def get_input(self, path):
        data = load_input_lines(path)
        return data

    def part1(self):
        count = 0
        for content in self.data:
            split = len(content)//2
            a, b  = content[:split], content[split:]
            for c in a:
                if c in b:
                    count += self.score[c]
                    break
        return count

    def part2(self):
        count = 0
        for ind in range(0, len(self.data), 3):
            group = self.data[ind:ind+3]
            for a in group[0]:
                if a in group[1] and a in group[2]:
                    count += self.score[a]
                    break
        return count
