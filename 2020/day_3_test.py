from unittest import TestCase
from utility import read_lines
from day_3 import TobboganTrajectory

class TestTobboganTrajectory(TestCase):

    def test_count_trees_3(self):
        # Arrange
        input_file = 'day_3_input.txt'

        tt = TobboganTrajectory(
            base_map = read_lines(input_file)
        )
        
        # Act
        actual = tt.countTrees(3)

        # Assert
        expected = 259
        self.assertEqual(expected, actual)