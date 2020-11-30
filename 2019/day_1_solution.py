from math import floor

# part 1
def get_fuel_requirement(mass):
    return floor(mass/3) - 2

def get_only_modules_fuel(module_masses):
    total_fuel = 0

    for module_mass in module_masses:
        total_fuel += get_fuel_requirement(module_mass)

    return total_fuel

# part 2
def get_module_with_fuel_requirement(module_mass):
    fuel_mass = get_fuel_requirement(module_mass)
    total_module_fuel = 0

    while fuel_mass > 0:
        total_module_fuel += fuel_mass
        fuel_mass = get_fuel_requirement(fuel_mass)
        
    
    return total_module_fuel

def get_total_fuel_requirement(module_masses):
    total_fuel = 0

    for module_mass in module_masses:
        total_fuel += get_module_with_fuel_requirement(module_mass)

    return total_fuel