import unittest   # The test framework
from day_2_solution import *
from pathlib import Path

class Test_Day2(unittest.TestCase):
    # part 1
    def test_computer_with_example(self):
        with open(Path(__file__).parent.resolve() / Path('day_2_input.example-dat')) as data:
            programs = data.read().splitlines()

        for program in programs:
            code = [int(x) for x in program.split(',')]
            program, expected =  code[:-1], code[-1]

            actual = computer(program, 0)

            self.assertEqual(expected, actual)

    def test_computer_with_input(self):
        with open(Path(__file__).parent.resolve() / Path('day_2_input.dat')) as data:
            program = [int(x) for x in data.read().split(',')]

            expected = 2
            actual = computer(program, 0)

            self.assertEqual(expected, actual)