import pytest
from day_3 import ToboganTrajectory
from utility import read_lines

@pytest.mark.parametrize(
    "right_distance, expected_trees, limit", 
    [(1, 5,  35), 
     (3, 2, 15), 
     (5, 6,  10), 
     (7, 6,  10)] )
def test_count_tree(right_distance, expected_trees, limit):
    # Arrange

    tt = ToboganTrajectory(
        base_map = read_lines('day_3_input.txt')[:limit]
    )
    
    # Act & Assert
    assert tt.count_trees(right_distance) == expected_trees