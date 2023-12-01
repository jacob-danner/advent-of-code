import re
from pathlib import Path


string_digit_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_calibration_value(line: str) -> int:
    # find 'string digits' or digit characters
    raw_digit_capture = r"one|two|three|four|five|six|seven|eight|nine|\d"

    raw_digits = re.findall(raw_digit_capture, line)

    def parse_digit(raw_digit: str) -> int:
        def is_string(raw_digit: str) -> bool:
            return raw_digit in string_digit_map.keys()

        def get_int_from_string(raw_digit: str) -> int:
            return string_digit_map[raw_digit]

        digit: int

        if is_string(raw_digit):
            digit = get_int_from_string(raw_digit)
        else:
            digit = int(raw_digit)

        return digit

    clean_digits = [parse_digit(raw_digit) for raw_digit in raw_digits]

    first = clean_digits[0]
    last = clean_digits[-1]

    calibration_value = int(f"{first}{last}")

    return calibration_value


def get_sum_calibration_values(lines: list[str]):
    sum_calibration_values = 0

    for line in lines:
        calibration_value = get_calibration_value(line)
        sum_calibration_values += calibration_value

    return sum_calibration_values


def main():
    with open(Path.cwd() / "input.txt") as file:
        lines = file.readlines()

    final_sum = get_sum_calibration_values(lines)
    print(final_sum)


if __name__ == "__main__":
    main()
