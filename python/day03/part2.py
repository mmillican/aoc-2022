import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(input: str) -> int:
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    total = 0
    grp_idx = 0
    grp = []
    
    for line in input.splitlines():
        grp.append(line)
        
        grp_idx += 1

        if grp_idx > 2:
            same = list(set(grp[0]).intersection(set(grp[1])).intersection(set(grp[2])))[0]

            grp = []
            grp_idx = 0

            same_pri = priorities.index(same) + 1 # add one to adjust for index
            total += same_pri

    return total

def main() -> int:
    with open(INPUT_PATH) as f:
        print(compute(f.read()))
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())