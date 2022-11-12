with open(file='data.txt') as file:
    height_map = [list(line) for line in file.read().split("\n")]


COL_LENGTH = len(height_map[0])
ROW_LENGTH = len(height_map)


def get_adjacent_numbers(r, c):
    global height_map
    a_nums = []
    indices = []

    if c + 1 < COL_LENGTH:
        a_nums.append(height_map[r][c+1])
        indices.append((r, c+1))
    if c - 1 >= 0:
        a_nums.append(height_map[r][c-1])
        indices.append((r, c-1))
    if r + 1 < ROW_LENGTH:
        a_nums.append(height_map[r+1][c])
        indices.append((r+1, c))
    if r - 1 >= 0:
        a_nums.append(height_map[r-1][c])
        indices.append((r-1, c))

    return a_nums, indices


risk_level_sum = 0
basin_starter_indices = []

for r, row in enumerate(height_map):
    for c, col in enumerate(row):
        adjacent_nums, valid_indices = get_adjacent_numbers(r, c)
        if height_map[r][c] < min(adjacent_nums):
            risk_level_sum += 1 + int(height_map[r][c])

            print(f"current number: {height_map[r][c]}, adjacent numbers: {adjacent_nums}, valid indices: {valid_indices}")
            basin_starter_indices.append(valid_indices)


all_basin_sizes = []
indices_checked = []

for entry in basin_starter_indices:
    curr_basin = []
    for index in entry:
        curr_basin.append(index)

    curr_basin_count = 0
    while curr_basin:
        curr_index = curr_basin.pop()
        new_r, new_c = curr_index[0], curr_index[1]

        if height_map[new_r][new_c] < "9" and (new_r, new_c) not in indices_checked:
            curr_basin_count += 1
            indices_checked.append((new_r, new_c))
            _, new_indices = get_adjacent_numbers(new_r, new_c)

            for new_index in new_indices:
                curr_basin.append(new_index)

    all_basin_sizes.append(curr_basin_count)


# part one:
print(risk_level_sum)

# part two:
result = sorted(all_basin_sizes, reverse=True)
print(result[0] * result[1] * result[2])
