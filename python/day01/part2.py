import os.path

INPUT_PATH = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(input: str) -> int:
    cur_calories = 0
    
    elf_number = 0
    elf_calories = dict()

    elves = input.split('\n\n')
    for elf in elves:
        elf_number += 1
        cur_calories = sum(int(line) for line in elf.splitlines())

        elf_calories[elf_number] = cur_calories

    cal_values = list(elf_calories.values())
    max_values = sorted(list(cal_values))[-3:]
    total_cals = sum(max_values)

    return total_cals


def main() -> int:
    with open(INPUT_PATH) as f:
        print(compute(f.read()))
    
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
