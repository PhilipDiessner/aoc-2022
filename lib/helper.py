import os
import requests


def get_input(cookie, day, year=2022):
    response = requests.get(
        f'https://adventofcode.com/{year}/day/{day[3:]}/input',
        cookies={'session': cookie}
    )

    path = f"data/{day}_input.txt"
    with open(path, 'w') as f:
        f.write(response.text)
    return path


def load_input(file_path: str) -> str:
    with open(file_path, "r") as f:
        return f.read().rstrip()


def load_input_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        return [x.rstrip() for x in f.readlines()]


def load_intlist(file_path: str) -> list[int]:
    return [int(y) for y in load_input(file_path).split(",")]


def load_input_int(file_path: str) -> list[int]:
    return [int(x) for x in load_input_lines(file_path)]


def load_input_int_lines(file_path: str) -> list[int]:
    return [[int(x) for x in y] for y in load_input_lines(file_path)]


def coord_dict_printready(d: dict):
    xset = set(x[0] for x in d.keys())
    yset = set(y[1] for y in d.keys())
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    return ["".join(str(d[(x, y)]) for x in range(xmin, xmax)) for y in range(ymin, ymax)]


def coord_set_printready(d):
    xset = set(x[0] for x in d)
    yset = set(y[1] for y in d)
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    return ["".join(str("#" if (x, y) in d else ".") for x in range(xmin, xmax)) for y in range(ymin, ymax)]


def coord_set_printready_complex(d):
    xset = set(int(x.real) for x in d)
    yset = set(int(y.imag) for y in d)
    xmin, xmax, ymin, ymax = min(xset), max(xset)+1, min(yset), max(yset)+1
    print((ymin, ymax), (xmin, xmax))
    return ["".join(str("#" if x+1J*y in d else ".") for x in range(xmin, xmax)) for y in range(ymin, ymax)]


def around(point, diag=False, include_point=False):
    if diag and include_point:
        return point-1j-1, point-1j, point-1j+1, point-1, point, point+1, point+1J-1, point+1J, point+1J+1
    if diag:
        return point-1j-1, point-1j, point-1j+1, point-1, point+1, point+1J-1, point+1J, point+1J+1
    if include_point:
        return point-1j, point-1, point, point+1, point+1J
    return point-1J, point-1, point+1, point+1J

def start_of_packet(data, n=14):
        for i in range(len(data)-n+1):
            if len(set(data[i:i+n])) == n:
                break
        return i+n