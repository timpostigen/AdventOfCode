from utility import read_lines
import re

class passwdPhilo:
    """
    Validates passwords
    """
    def __init__(self, passwords=None):
        self.password_entries = passwords
        self.pasword_parse = re.compile(r'(\d+)-(\d+) (\w): (.*)') 

    def parse_password_line(self, line):
        """
        parses password entry
        """

        # 1-3 a: abcde
        m = self.pasword_parse.match(line)

        password = {'start': int(m.group(1)), 'end': int(m.group(2)), 'letter': m.group(3), 'password': m.group(4)} 

        return password

    def validate_password_bounds(self, start, end, letter, password):
        """
        Checks a password for min/max occurences of letter
        """
        lower = start
        upper = end

        count = 0
        for char in password:
            if char == letter:
                count += 1

        valid = lower <= count <= upper

        return valid

    def validate_password_line_position(self, start, end, letter, password):
        first_postion = start
        second_postion = end

        valid = password[first_postion-1] == letter and password[second_postion-1] != letter

        return valid

    def count_valid_passwords(self, password_entries= None):
        if(not password_entries):
            password_entries = self.password_entries
        count = 0
        
        for password in password_entries:
            if(self.validate_password_line_position(**password)):
                count += 1
        
        return count

pp = passwdPhilo()

password_lines = []
for line in read_lines('day-2-input.txt'):
    parsed_password = pp.parse_password_line(line)
    password_lines.append(parsed_password)

pp.password_entries = password_lines

# valid_password = pp.validate_password(**pp.password_entries[0])

print(pp.count_valid_passwords())

# print(pp.countValidPasswords(passwords))