import pytest
from day_5 import BinaryBoarding

@pytest.mark.parametrize("boarding_pass, expected_seat_id", [
    ('FFFFFFFLLL', 0),
    ('BBBBBBBRRR', 1023)
])
def test_get_seat_id(boarding_pass, expected_seat_id):
    # Arrange
    bb = BinaryBoarding(None)
    
    # Act & Assert
    actual_seat_id = bb.get_seat_id(boarding_pass)
    assert actual_seat_id == expected_seat_id