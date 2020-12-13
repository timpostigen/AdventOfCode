from collections import defaultdict
from re import match, findall
from pathlib import Path

class HandyHaversacks():
    #region --- Day 7: Handy Haversacks ---
    """
    --- Day 7: Handy Haversacks ---

    You land at the regional airport in time for your next flight. In fact, it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage processing.

    Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently, nobody responsible for these regulations considered how long they would take to enforce!

    For example, consider the following rules:

    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.

    These rules specify the required contents for 9 bag types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6 dotted black), and so on.

    You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

    In the above rules, the following options would be available to you:

        A bright white bag, which can hold your shiny gold bag directly.
        A muted yellow bag, which can hold your shiny gold bag directly, plus some other bags.
        A dark orange bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.
        A light red bag, which can hold bright white and muted yellow bags, either of which could then hold your shiny gold bag.

    So, in this example, the number of bag colors that can eventually contain at least one shiny gold bag is 4.

    How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure you get all of it.)

    Notes:
    0 << 5 < answer << len(rules) = 594
    answer probably < 22 bc not taking into account bag limits
    """
    #endregion

    def __init__(self):
        """
        docstring
        """
        self.bag_rules = {}
        self.input_file_name = Path(__file__).parent / f'{Path(__file__).stem}_input.txt'

    def parse_bag_rules(self):
        with open(self.input_file_name) as file:
            for line in file:
                line = line.strip()

                bag_color_label = 'bag_color'
                bag_rule_line_label = 'bag_rule_line'

                rule_entry = match(f'(?P<{bag_color_label}>.*) bags contain (?P<{bag_rule_line_label}>.*)', line).groupdict()
                bag_color = rule_entry[bag_color_label]
                bag_rule_line = rule_entry[bag_rule_line_label]

                if bag_rule_line == 'no other bags.':
                    self.bag_rules[bag_color] = None
                else:
                    bag_rule = {}
                    for rule in findall(r'(\d+) (\w+ \w+) \w+', bag_rule_line):
                        bag_rule[rule[1]] = int(rule[0])
                    
                    self.bag_rules[bag_color] = bag_rule

        return self.bag_rules

    def count_contains_bag(self, bag_color):
        """
        docstring
        """

        can_contain = 0

        for bag_rule in self.bag_rules:
            if(self.contains_bag(bag_rule, bag_color)):
                can_contain += 1

        return can_contain

    # recursive
    # work backward?
    def contains_bag(self, bag_rule_name, bag_color):
        # 2 base cases then recursion
        bag_rule = self.bag_rules[bag_rule_name]

        if bag_rule == None:
            return False
        elif bag_color in bag_rule.keys():
            return True
        else:
            for nested_bag_rule_name in bag_rule.keys():
                return self.contains_bag(nested_bag_rule_name, bag_color)

if __name__ == "__main__":
    hh = HandyHaversacks()

    hh.parse_bag_rules()

    print('parsed')

    bag_color = 'shiny gold'
    bags = hh.count_contains_bag('shiny gold')

    print(bags)