from functools import reduce

#direction_order = ['N', 'E', 'S', 'W']
location_type = tuple[int, int]
direction_list: list[location_type] = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]


def format_rotation(raw_move: str) -> location_type:
    rotation_change: int = 1 if raw_move[0] == 'R' else -1
    houses: int = int(raw_move[1:])
    return (rotation_change, houses)


def format_move(rotation: location_type, direction_index: int) -> tuple[int, int]:
    direction_index += rotation[0]
    direction_vec: location_type = direction_list[direction_index % 4]
    return tuple(v*rotation[1] for v in direction_vec), direction_index


def format_move_list(rotation_list, initial_direction_index):
    direction_index = initial_direction_index
    move_list = []
    for rotation in rotation_list:
        move, direction_index = format_move(rotation, direction_index)
        move_list += [move]
    return move_list


def main1():
    with open('day-1.txt', 'r') as f:
        input: str = f.read()
    result: int = challenge1(input)
    print(result)


def challenge1(input: str) -> int:
    initial_direction_index = 0
    raw_rotation_list: list[str] = input.split(', ')
    rotation_list: list[tuple[str, int]] = [
        format_rotation(s) for s in raw_rotation_list]
    move_list: list[location_type] = format_move_list(
        rotation_list, initial_direction_index)
    final_location: location_type = reduce(
        lambda m0, m1: tuple(x + y for x, y in zip(m0, m1)), move_list)
    number_of_houses: int = abs(final_location[0]) + abs(final_location[1])
    return number_of_houses


def process_visited_location(move: location_type, location_list: list[location_type]) -> tuple[list[location_type], location_type]:
    new_location_list: list[location_type] = location_list.copy()
    number_of_moves = move[0] + move[1]
    r = range(1, number_of_moves +
              1) if number_of_moves >= 0 else range(-1, number_of_moves - 1, -1)
    for i in r:
        last_location: location_type = location_list[-1]
        x: int = last_location[0] if move[0] == 0 else last_location[0] + i
        y: int = last_location[1] if move[1] == 0 else last_location[1] + i
        new_location: location_type = (x, y)
        if new_location in location_list:
            return new_location_list, new_location
        new_location_list = [*new_location_list, new_location]
    return new_location_list, None


def process_visited_locations(move_list: list[location_type]) -> tuple[int, int]:
    location_list = [(0, 0)]
    for move in move_list:
        location_list, result = process_visited_location(move, location_list)
        if result:
            return result
    return None


def main2():
    with open('day-1.txt', 'r') as f:
        input: str = f.read()
    location: int = challenge2(input)
    print(location)


def challenge2(input):
    initial_direction_index = 0
    raw_rotation_list: list[str] = input.split(', ')
    rotation_list: list[tuple[str, int]] = [
        format_rotation(s) for s in raw_rotation_list]
    move_list: list[location_type] = format_move_list(rotation_list, initial_direction_index)
    location: location_type = process_visited_locations(move_list)
    number_of_houses: int = abs(location[0]) + abs(location[1])
    return number_of_houses

main1()
main2()
