from math import floor

def get_fuel_requirement(module_mass):
    return floor(module_mass/3) - 2

def get_total_fuel_requirement(module_masses):
    total_fuel = 0

    for module_mass in module_masses:
        total_fuel += get_fuel_requirement(module_mass)

    return total_fuel