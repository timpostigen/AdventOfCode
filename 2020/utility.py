from pathlib import Path

def readLines(line_filename):
    lines = []

    line_file_path = Path(__file__).parent / line_filename

    with open(line_file_path) as file:
        file_lines = file.readlines()

        for line in file_lines:
                lines.append(int(line))

    return lines