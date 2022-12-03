from utility import get_input_file
from pathlib import Path
from copy import deepcopy
from json import dumps

class SeatingSystem():
    #region  --- Day 11: Seating System ---
    """
    Your plane lands with plenty of time to spare. The final leg of your journey is a ferry that goes directly to the tropical island where you can finally start your vacation. As you reach the waiting area to board the ferry, you realize you're so early, nobody else has even arrived yet!

    By modeling the process people use to choose (or abandon) their seat in the waiting area, you're pretty sure you can predict the best place to sit. You make a quick map of the seat layout (your puzzle input).

    The seat layout fits neatly on a grid. Each position is either floor (.), an empty seat (L), or an occupied seat (#). For example, the initial seat layout might look like this:

    L.LL.LL.LL
    LLLLLLL.LL
    L.L.L..L..
    LLLL.LL.LL
    L.LL.LL.LL
    L.LLLLL.LL
    ..L.L.....
    LLLLLLLLLL
    L.LLLLLL.L
    L.LLLLL.LL

    Now, you just need to model the people who will be arriving shortly. Fortunately, people are entirely predictable and always follow a simple set of rules. All decisions are based on the number of occupied seats adjacent to a given seat (one of the eight positions immediately up, down, left, right, or diagonal from the seat). The following rules are applied to every seat simultaneously:

        If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        Otherwise, the seat's state does not change.

    Floor (.) never changes; seats don't move, and nobody sits on the floor.

    After one round of these rules, every seat in the example layout becomes occupied:

    #.##.##.##
    #######.##
    #.#.#..#..
    ####.##.##
    #.##.##.##
    #.#####.##
    ..#.#.....
    ##########
    #.######.#
    #.#####.##

    After a second round, the seats with four or more occupied adjacent seats become empty again:

    #.LL.L#.##
    #LLLLLL.L#
    L.L.L..L..
    #LLL.LL.L#
    #.LL.LL.LL
    #.LLLL#.##
    ..L.L.....
    #LLLLLLLL#
    #.LLLLLL.L
    #.#LLLL.##

    This process continues for three more rounds:

    #.##.L#.##
    #L###LL.L#
    L.#.#..#..
    #L##.##.L#
    #.##.LL.LL
    #.###L#.##
    ..#.#.....
    #L######L#
    #.LL###L.L
    #.#L###.##

    #.#L.L#.##
    #LLL#LL.L#
    L.L.L..#..
    #LLL.##.L#
    #.LL.LL.LL
    #.LL#L#.##
    ..L.L.....
    #L#LLLL#L#
    #.LLLLLL.L
    #.#L#L#.##

    #.#L.L#.##
    #LLL#LL.L#
    L.#.L..#..
    #L##.##.L#
    #.#L.LL.LL
    #.#L#L#.##
    ..L.L.....
    #L#L##L#L#
    #.LLLLLL.L
    #.#L#L#.##

    At this point, something interesting happens: the chaos stabilizes and further applications of these rules cause no seats to change state! Once people stop moving around, you count 37 occupied seats.

    Simulate your seating area by applying the seating rules repeatedly until no seats change state. How many seats end up occupied?

    """
    #endregion
    def __init__(self, seating_area):
        """
        docstring
        """

        self.seating_area = [[spot for spot in subarray] for subarray in seating_area]
        self.new_seating_area = deepcopy(self.seating_area)
        pass
    
    def check_seats(self):
        """
        docstring
        """
        for row_idx, row in enumerate(self.seating_area):
            for spot_idx, current_spot in enumerate(row):
                adjacent_occupied = self.check_adjacent_spots(row_idx, spot_idx)

                if(current_spot == '.'):
                    self.new_seating_area[row_idx][spot_idx] = current_spot
                    continue

                if(adjacent_occupied == 0):
                    self.new_seating_area[row_idx][spot_idx] = '#'
                elif(adjacent_occupied >= 4):
                    self.new_seating_area[row_idx][spot_idx] = 'L'
                else:
                    self.new_seating_area[row_idx][spot_idx] = current_spot


    def check_adjacent_spots(self, row_idx, spot_idx):
        occupied = 0

        for row in range(row_idx + 1, row_idx - 2, -1):
            # corner/edge special case
            if(-1 < row < len(self.seating_area)):
                for spot in range(spot_idx + 1, spot_idx - 2, -1):
                    if(row == row_idx and spot == spot_idx):
                        continue
                    if(-1 < spot < len(self.seating_area[row])):
                        if self.seating_area[row][spot] == '#':
                            occupied += 1
        
        return occupied

    def check_seats_until_stable(self):
        """
        docstring
        """
        stable = False
        
        while(not stable):
            self.seating_area = deepcopy(self.new_seating_area)

            self.check_seats()

            s_seating_area = dumps(self.seating_area)
            s_new_seating_area = dumps(self.new_seating_area)

            stable = bool(s_seating_area == s_new_seating_area)
        


if __name__ == "__main__":    
    ss = SeatingSystem(get_input_file(f'{Path(__file__).stem}_input.txt'))

    ss.check_seats_until_stable()