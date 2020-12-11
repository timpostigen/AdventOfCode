from pathlib import Path
from utility import read_lines

class BinaryBoarding():
    #region
    '''
    --- Day 5: Binary Boarding ---

    You board your plane only to discover a new problem: you dropped your boarding pass! You aren't sure which seat is yours, and all of the flight attendants are busy with the flood of people that suddenly made it through passport control.

    You write a quick program to use your phone's camera to scan all of the nearby boarding passes (your puzzle input); perhaps you can find your seat through process of elimination.

    Instead of zones or groups, this airline uses binary space partitioning to seat people. A seat might be specified like FBFBBFFRLR, where F means "front", B means "back", L means "left", and R means "right".

    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

    For example, consider just the first seven characters of FBFBBFFRLR:

        Start by considering the whole range, rows 0 through 127.
        F means to take the lower half, keeping rows 0 through 63.
        B means to take the upper half, keeping rows 32 through 63.
        F means to take the lower half, keeping rows 32 through 47.
        B means to take the upper half, keeping rows 40 through 47.
        B keeps rows 44 through 47.
        F keeps rows 44 through 45.
        The final F keeps the lower of the two, row 44.

    The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

    For example, consider just the last 3 characters of FBFBBFFRLR:

        Start by considering the whole range, columns 0 through 7.
        R means to take the upper half, keeping columns 4 through 7.
        L means to take the lower half, keeping columns 4 through 5.
        The final R keeps the upper of the two, column 5.

    So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

    Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

    Here are some other boarding passes:

        BFFFBBFRRR: row 70, column 7, seat ID 567.
        FFFBBBFRRR: row 14, column 7, seat ID 119.
        BBFFBBFRLL: row 102, column 4, seat ID 820.

    As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?

    Notes:
    Rows are 0-127, columns are 0-7

    Find row, find column, multiply

    '''
    #endregion
    def __init__(self, boarding_passes):
        """
        docstring
        """
        self.boarding_passes = boarding_passes

    def get_highest_seat_id(self):
        """
        docstring
        """
        highest_seat_id = 0
        
        for boarding_pass in self.boarding_passes:
            seat_id = self.get_seat_id(boarding_pass)

            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
        
        return highest_seat_id

    def get_seat_id(self, boarding_pass):
        """
        docstring
        """
        row_range = (128, 0)
        column_range = (0, 8)

        row = -1
        column = -1

        #BFRL
        for part in boarding_pass:
            # TODO: validate .5 rounding
            new_row = int((row_range[0] + row_range[1])/2)

            if part == 'F':
                row_range = (new_row, row_range[1])
            if part == 'B':
                row_range = (row_range[0], new_row)
            pass

        return row * column_range[0]
    

if __name__ == "__main__":
    boarding_passes = read_lines(f'{Path(__file__).stem}_input.txt')

    bb = BinaryBoarding(boarding_passes[:3])

    bb.get_highest_seat_id()