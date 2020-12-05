import re
from ast import literal_eval
from unittest import TestCase
from utility import read_lines
import inspect
from day_3 import ToboganTrajectory

class TestToboganTrajectory(TestCase):
    def setUp(self):        
        self.test_name_labels = {
            'right': 'right_distance',
            'down': 'down_distance',
            'limit': None,
            'expected': None,
            'input': None
        }

    def gen_test_config(self, test_name):
        """
        docstring
        """
        
        test_config = {'input_file': 'day_3_input.txt'}

        for label, param_name in self.test_name_labels.items():
            match = re.search(rf'_{label}(\w+?)_', test_name)

            if param_name:
                label = param_name

            if(match):
                test_config[label] = literal_eval(match.group(1))

        return test_config

    def test_count_trees_1(self):
        """
        docstring
        """
        pass

    def test_count_trees_right3_limit40_expected259_(self):
        # Arrange
        test_name = inspect.currentframe().f_code.co_name

        test_config = self.gen_test_config(test_name)

        tt = ToboganTrajectory(
            base_map = read_lines(test_config['input_file'])
        )
        
        # Act
        actual = tt.count_trees(**test_config)

        # Assert
        expected = test_config['expected']
        self.assertEqual(expected, actual)