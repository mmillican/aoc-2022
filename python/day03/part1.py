import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(input: str) -> int:
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    total = 0
    for line in input.splitlines():
        compart_size = int(len(line) / 2)
        first = line[0:compart_size]
        second = line[-1 * compart_size:]

        same = list(set(first).intersection(set(second)))[0]
        same_pri = priorities.index(same) + 1 # add one to adjust for index

        total += same_pri

    return total

def main() -> int:
    with open(INPUT_PATH) as f:
        print(compute(f.read()))
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())