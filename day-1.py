from functools import reduce

#direction_order = ['N', 'E', 'S', 'W']
direction_list: list[int, int] = [ 
    (0, 1),
    (1, 0), 
    (-1, 0),
    (0, -1), 
]

direction_index = 0

def format_rotation(raw_move: str) -> tuple[int, int]:
    rotation_change: int = 1 if raw_move[0] == 'L' else -1
    houses: int = int(raw_move[1:]) 
    return (rotation_change, houses)

def format_move(move: tuple[int, int]) -> tuple[int, int]:
    global direction_index
    direction_index += move[0]
    direction_vec: tuple[int, int] = direction_list[direction_index % 4]
    return tuple(v*move[1] for v in direction_vec)
    

def main():
    with open('day-1.txt', 'r') as f:
        input: str = f.read()
    raw_rotation_list: list[str] = input.split(', ')
    rotation_list: list[tuple[str, int]] = [format_rotation(s) for s in raw_rotation_list]
    move_list: list[tuple[int, int]] = [format_move(r) for r in rotation_list]
    final_location: tuple[int, int] = reduce(lambda m0, m1: tuple(x + y for x, y in zip(m0, m1)), move_list)
    number_of_houses: int = abs(final_location[0]) + abs(final_location[1])
    print(number_of_houses)

main()