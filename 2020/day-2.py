from utility import readLines

class passwordPhilosophy:
    """
    Validates passwords
    """
    def __init__(self, passwords=None):
        self.passwords = passwords

    def parseEntry(self, line):
        """
        parses password entry
        """

        password = {'letter': 'f', 'lower': 1, 'upper': 2, 'password': 'bar'} 

        return password

    def validatePassword(self, letter, lower, upper, password):
        """
        Checks a password for min/max occurences of letter
        """
        return True

    def countValidPasswords(self, passwords):
        count = 0
        
        for password in passwords:
            if(self.validatePassword(**password)):
                count += 1
        
        return count

pp = passwordPhilosophy()

passwords = []
for line in readLines('day-2-input.txt'):
    passwords += pp.parseEntry(line)

pp.passwords = passwords

print(pp.countValidPasswords(passwords))