import unittest   # The test framework
from day_1_solution import get_fuel_requirement, get_only_modules_fuel, get_module_with_fuel_requirement, get_total_fuel_requirement
from pathlib import Path

class Test_Day1(unittest.TestCase):
    # part 1
    def test_fuel_requirement(self):
        with open(Path(__file__).parent.resolve() / Path('day_1_example.dat')) as data:
            fuel_requirements = data.read().splitlines()

        just_mass = []

        for fuel_requirement in fuel_requirements[:-1]:
            mass, fuel =  [int(x) for x in fuel_requirement.split(',')]
            just_mass.append(mass)
            calculated_fuel = get_fuel_requirement(mass)
            

            self.assertEqual(calculated_fuel, fuel)

        # get total fuel requirements
        self.assertEqual(get_only_modules_fuel(just_mass), int(fuel_requirements[-1]))
    
    def test_module_with_fuel(self):
        with open(Path(__file__).parent.resolve() / Path('day_1_input.dat')) as data:
            fuel_requirements = data.read().splitlines()

        fuel_requirements = [int(x) for x in fuel_requirements]

        self.assertEqual(get_only_modules_fuel(fuel_requirements),3395944)

    # part 2
    def test_example_fully_fueled(self):
        with open(Path(__file__).parent.resolve() / Path('day_1_part_2_example.dat')) as data:
            fuel_requirements = data.read().splitlines()

        just_mass = []

        for fuel_requirement in fuel_requirements[:-1]:
            mass, fuel =  [int(x) for x in fuel_requirement.split(',')]
            just_mass.append(mass)
            calculated_fuel = get_module_with_fuel_requirement(mass)

            self.assertEqual(calculated_fuel, fuel)

        # get total fuel requirements
        self.assertEqual(get_total_fuel_requirement(just_mass), int(fuel_requirements[-1]))
    
    def test_fully_fueled(self):
        with open(Path(__file__).parent.resolve() / Path('day_1_input.dat')) as data:
            fuel_requirements = data.read().splitlines()

        fuel_requirements = [int(x) for x in fuel_requirements]

        self.assertEqual(get_total_fuel_requirement(fuel_requirements),5091036)


        
if __name__ == '__main__':
    unittest.main()