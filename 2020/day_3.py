from utility import read_lines

class TobboganTrajectory:
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

    """
    #endregion
    
    def __init__(self, base_map):
        """
        docstring
        """
        self.base_map = base_map
        self.base_map_width = len(base_map[0])
    
    def getCoordinate(self, x, y):
        """
        docstring
        """
        return self.base_map[x][y]

    def countTrees(self):
        """
        docstring
        """
        right_position = 0
        trees = 0
        right_distance = 3
        down_distance = 1

        marked_map = ''

        marked_map += f'0   {str.strip(self.base_map[0])}\n    ^ 0\n'
        # watch out for zero indexing
        for idx, row in enumerate(self.base_map[1::down_distance], start=1):
            right_position += right_distance

            if right_position >= self.base_map_width:
                # could do something with mod to simulat wrapping
                right_position = right_position - self.base_map_width + 1

            if row[right_position] == '#':
                trees += 1

            marked_map += f'{idx}   {str.strip(row)}\n{" " * (right_position+3+len(str(idx)))}^ {trees}\n'

        return marked_map, trees
            

input_file = 'day_3_input.txt'
output_file = 'day_3_output.txt'

brute_force = True
if(brute_force):
    input_file = input_file.replace('.txt', '_brute_force.txt') 
    output_file = output_file.replace('.txt', '_brute_force.txt') 


tt = TobboganTrajectory(
    base_map = read_lines(input_file)
)
marked_map, trees = tt.countTrees()

with open(output_file, 'w') as f:
    f.write(marked_map)

print(f"Total Trees:\n{trees}")
