import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(input: str) -> int:
    mark_seq = []

    for c_idx, c in enumerate(input):
        mark_seq.append(c)

        if c_idx >= 4 and len(set(mark_seq)) == 14:
            return c_idx + 1
        elif len(mark_seq) >= 14:
            mark_seq.pop(0)

        print(f'seq: {mark_seq}')
    
    return 0

def main() -> int:
    with open(INPUT_PATH) as f:
        print(compute(f.read()))
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())