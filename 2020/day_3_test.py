import pytest
from day_3 import ToboganTrajectory
from utility import read_lines

@pytest.mark.parametrize( "right_distance, expected_trees", [(3, 259)] )
def test_count_tree(right_distance, expected_trees):
    # Arrange

    tt = ToboganTrajectory(
        base_map = read_lines('day_3_input.txt')
    )
    
    # Act & Assert
    assert tt.count_trees(right_distance) == expected_trees