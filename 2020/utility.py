from pathlib import Path

def read_lines(line_filename, targetType=None, trim = False):
    line_file_path = Path(__file__).parent / line_filename

    file_lines = []
    with open(line_file_path) as file:
        file_lines = file.read().splitlines()

    lines = []
    if(not targetType):
        lines = file_lines
    else:
        for line in file_lines:
            lines.append(type(targetType)(line))

    return lines