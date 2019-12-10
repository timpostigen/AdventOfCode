import unittest   # The test framework
from day_2_solution import *
from pathlib import Path

class Test_Day1(unittest.TestCase):
    # part 1
    def test_fuel_requirement(self):
        with open(Path(__file__).parent.resolve() / Path('day_1_example.dat')) as data:
            programs = data.read().splitlines()

        for program in programs:
            computer(program)