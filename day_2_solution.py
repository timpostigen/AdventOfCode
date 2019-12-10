# 1 is add
# 2 is multiply
# 99 is halt

# steps are 4 positions long

# replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0


def computer(program, position):
    first_input, second_input = program[position+1], program[position+2]

    # 1 is add
    if program[position] == 1:
        program[position+3] = first_input + second_input

    # 2 is multiply
    if program[position] == 2:
        program[position+3] = first_input + second_input
    
    # 99 is halt
    if program[position] == 99:
        return program[0]

    computer(program, [position+4])