from lib.template import Solution
from lib.helper import load_input_lines, coord_set_printready_complex


def update_knot(h, t):
    dy, dx = h.imag - t.imag, h.real-t.real
    tot = abs(dx)+abs(dy)
    if tot == 4:
        t += (dx//2 + 1j*(dy//2))
    elif tot == 3:
        t += (dx + 1j*(dy//2)) if abs(dx) ==1 else (dx//2 +1j*dy)
    elif abs(dx)==2 or abs(dy)==2:
        t = (h + t)/2
    return t


class Day(Solution):
    def get_input(self, path):
        data = [x.split() for x in load_input_lines(path)]
        return data

    def part1(self):
        chart = self.run_rope(2)
        to_print = coord_set_printready_complex(chart)
        to_print.reverse()
        return len(chart)

    def part2(self):
        return len(self.run_rope(10))

    def run_rope(self, len_rope):
        movement = {"D": -1J, "U": 1J, "L": -1, "R": 1}

        rope = [0j]*len_rope
        chart = set([rope[-1]])
        for direction, c in self.data:
            for _ in range(int(c)):
                rope[0] += movement[direction]
                for i in range(1, len_rope):
                    rope[i] = update_knot(rope[i-1], rope[i])
                # print(direction, rope)
                chart.add(rope[-1])
        return chart
