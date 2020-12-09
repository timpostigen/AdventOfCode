import pytest
from day_3 import ToboganTrajectory
from utility import read_lines

@pytest.mark.parametrize("right_distance, expected_trees, limit", [
    (1, 5,  35),
    (3, 11, 15),
    (5, 0,  10),
    (7, 1,  10)] )
def test_count_tree(right_distance, expected_trees, limit):
    # Arrange

    limited_map = read_lines('day_3_input.txt')[:limit]

    tt = ToboganTrajectory(
        base_map = limited_map
    )
    
    # Act & Assert
    actual_trees = tt.count_trees(right_distance)
    assert actual_trees == expected_trees

def test_route_product():
    expected_product = 2224913600

    tt = ToboganTrajectory(
        base_map = read_lines('day_3_input.txt')
    )

    # Part 2 stuff
    actual_product = tt.route_product((1, 3, 5, 7, (1,2)))
    
    # Act & Assert
    # actual_product = tt.route_product((1, 3, 5, 7, (1,2)))

    assert actual_product == expected_product