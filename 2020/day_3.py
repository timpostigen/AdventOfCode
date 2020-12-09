from utility import read_lines

class ToboganTrajectory:
    # region --- Day 3: Toboggan Trajectory --- docstring
    """
    --- Day 3: Toboggan Trajectory ---

    With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

    Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#

    These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

    ..##.........##.........##.........##.........##.........##.......  --->
    #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........#.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...##....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

    The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->

    In this example, traversing the map using this slope would cause you to encounter 7 trees.

    Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

    Notes:
    Width of the map always needs to be 3x the height (probably rounded up, not sure). My input height was 323, and width was 32 so, probably 11 repetitions to the right.

    Your puzzle answer was 259.

    The first half of this puzzle is complete! It provides one gold star: *
    --- Part Two ---

    Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

    Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

        Right 1, down 1.
        Right 3, down 1. (This is the slope you already checked.)
        Right 5, down 1.
        Right 7, down 1.
        Right 1, down 2.

    In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

    What do you get if you multiply together the number of trees encountered on each of the listed slopes?

    Notes:
    answer < 2288482560
    """
    #endregion
    
    def __init__(self, base_map, brute_force_suffix='', write_marked_map=False):
        """
        docstring
        """
        self.base_map = base_map
        self.base_map_width = len(base_map[0])
        self.brute_force_suffix = brute_force_suffix
        self.write_marked_map = write_marked_map
    
    def getCoordinate(self, x, y):
        """
        docstring
        """
        return self.base_map[x][y]

    def count_trees(self, right_distance, down_distance=1, write_marked_map=None, **kwargs):
        """
        docstring
        """
        if(not write_marked_map):
            write_marked_map = self.write_marked_map

        right_position = 0
        trees = 0

        marked_map = ''

        marked_map += f'0   {str.strip(self.base_map[0])}\n    ^ 0\n'
        # watch out for zero indexing
        for idx, row in enumerate(self.base_map[down_distance::down_distance], start=1):
            right_position += right_distance

            if right_position >= self.base_map_width:
                # could do something with mod to simulat wrapping
                right_position = right_position - self.base_map_width

            if row[right_position] == '#':
                trees += 1

            map_line = f'{idx}   {str.strip(row)}\n'
            position_line = f'{" " * (right_position+3+len(str(idx)))}^ {trees}\n'

            marked_map += map_line + position_line

        if(write_marked_map):
            output_file = f'day_3_r{right_distance}_d{down_distance}{self.brute_force_suffix}_output.txt'

            with open(output_file, 'w') as f:
                f.write(marked_map)

        return trees

    def route_product(self, slopes):
        product = 1

        for slope in slopes:
            if type(slope) == tuple:
                product = product * self.count_trees(*slope)
            else:
                product = product * self.count_trees(slope)

        return product

if __name__ == "__main__":
    bfs = '_brute_force'
    input_file = f'day_3{bfs}_input.txt'

    tt = ToboganTrajectory(
        base_map = read_lines(input_file),
        brute_force_suffix = bfs,
        write_marked_map=True
    )

    # Part 1
    print(f"Brute Force: {bfs}")

    trees = tt.count_trees(3)

    print(f"Total Trees: {trees}")

    # Part 2 stuff
    route_product = tt.route_product((1, 3, 5, 7, (1,2)))

    print(f"Route Product: {route_product}")
