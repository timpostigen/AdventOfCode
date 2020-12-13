from pathlib import Path
from argparse import ArgumentParser

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

def get_input_file(input_file_name=None):
    # parser = ArgumentParser(description='setup solution files')
    # parser.add_argument('input_file', nargs='?', type=str, help='path of the input file')
    # args = parser.parse_args()

    # input_file_name = args.input_file or input_file_name

    return read_lines(input_file_name)