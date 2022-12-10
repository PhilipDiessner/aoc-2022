import importlib
from time import perf_counter
from argparse import ArgumentParser
from lib.helper import get_input


parser = ArgumentParser(prog="AoC22")
parser.add_argument("day")
parser.add_argument("--sample", action='store_true')
parser.add_argument("--printer", action='store_true')
parser.add_argument("--download", action='store_true')



def main(day, sample=False, printer=False, download=False):

    if download:
        with open("aoc.cookie") as f:
            COOKIE = f.read()
        output = get_input(COOKIE, day)
        print(f"Downloaded to {output}")
        return
    
    i = importlib.import_module(f"lib.{day}")
    datapath = f"./data/{day}" + ("_sample.txt" if sample else "_input.txt")
    start = perf_counter()
    solution = i.Day(datapath)
    print("Setup Time:", perf_counter()-start)
    start = perf_counter()

    print("Part 1:", solution.part1(), "Time:", perf_counter()-start)
    start = perf_counter()

    print("Part 2:", solution.part2(), "Time:", perf_counter()-start)


if __name__ == '__main__':
    args = vars(parser.parse_args())
    main(**args)
