def calculator(first_number: float, second_number: float, operation: str) -> float:
    """
    Виконує арифметичні операції над двома числами.

    :param first_number: Перше число (float)
    :param second_number: Друге число (float)
    :param operation: Операція, яку потрібно виконати ('+', '-', '*', '/')
    :return: Результат виконання операції (float)

    :raises ValueError: Якщо операція не є дійсною.
    :raises ZeroDivisionError: Якщо операція - ділення на нуль.
    """
    if operation == '+':
        return first_number + second_number
    elif operation == '-':
        return first_number - second_number
    elif operation == '*':
        return first_number * second_number
    elif operation == '/':
        if second_number == 0:
            raise ZeroDivisionError("Ділення на нуль недопустимо.")
        return first_number / second_number
    else:
        raise ValueError("Недійсна операція. Використовуйте '+', '-', '*', або '/'.")


# test

import unittest


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(calculator(5, 3, '-'), 2)

    def test_multiplication(self):
        self.assertEqual(calculator(3, 4, '*'), 12)

    def test_division(self):
        self.assertEqual(calculator(10, 2, '/'), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator(10, 0, '/')

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculator(10, 5, '%')


if __name__ == '__main__':
    unittest.main()
