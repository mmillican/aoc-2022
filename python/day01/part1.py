import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')

def compute(input: str) -> int:
    cur_calories = 0
    max_calories = 0

    lines = input.splitlines()
    for line in lines:
        if line != '':
            cur_calories += int(line)
        else:
            if cur_calories > max_calories:
                max_calories = cur_calories

            cur_calories = 0

    return max_calories

def main() -> int:
    with open(INPUT_PATH) as f:
        print(compute(f.read()))
    
    return 0

if __name__ == '__main__':
    raise SystemExit(main())