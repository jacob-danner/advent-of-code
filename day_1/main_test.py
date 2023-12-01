import unittest
import main


class TestGetCalibrationValue(unittest.TestCase):
    """digit character cases"""

    def test_0(self):
        input_line = "1abc2"
        expected = 12

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_1(self):
        input_line = "pqr3stu8vwx"
        expected = 38

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_2(self):
        input_line = "a1b2c3d4e5f"
        expected = 15

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_3(self):
        # this is an unusual case where there is only one digit
        input_line = "treb7uchet"
        expected = 77

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    """mixed "string digit" and digit character cases"""

    def test_4(self):
        # this is an unusual case where there is only one digit
        input_line = "two1nine"
        expected = 29

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_5(self):
        # this is an unusual case where there is only one digit
        input_line = "eightwothree"
        expected = 83

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_6(self):
        # this is an unusual case where there is only one digit
        input_line = "abcone2threexyz"
        expected = 13

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_7(self):
        # this is an unusual case where there is only one digit
        input_line = "xtwone3four"
        expected = 24

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_8(self):
        # this is an unusual case where there is only one digit
        input_line = "4nineeightseven2"
        expected = 42

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_9(self):
        # this is an unusual case where there is only one digit
        input_line = "zoneight234"
        expected = 14

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)

    def test_10(self):
        # this is an unusual case where there is only one digit
        input_line = "7pqrstsixteen"
        expected = 76

        result = main.get_calibration_value(input_line)

        self.assertEqual(result, expected)


class TestGetSumCalibrationValues(unittest.TestCase):
    def test_0(self):
        input_lines = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

        expected = 281

        result = main.get_sum_calibration_values(input_lines)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
