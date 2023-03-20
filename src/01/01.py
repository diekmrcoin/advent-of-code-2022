import pathlib
import numpy as np


def part1():
    current_dir = pathlib.Path(__file__).parent.absolute()
    file = current_dir / 'input.txt'
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        lines = [[int(x) for x in line] for line in lines]
        max = 0
        acc = 0
        for line in lines:
            if len(line) < 1:
                max = max if max > acc else acc
                acc = 0
            else:
                acc += line[0]
        print(max)


def part2():
    current_dir = pathlib.Path(__file__).parent.absolute()
    file = current_dir / 'input.txt'
    with open(file, 'r') as f:
        lines = f.readlines()
        lines = [line.split() for line in lines]
        lines = [[int(x) for x in line] for line in lines]
        lines.append([])
        max = []
        acc = 0
        for line in lines:
            if len(line) < 1:
                max.append(acc)
                acc = 0
            else:
                acc += line[0]
        max.sort(reverse=True)
        print(max[0:3])
        print(np.sum(max[0:3]))


if __name__ == '__main__':
    part1()
    part2()
