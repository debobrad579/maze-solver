def depth_first_search(maze):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(0, 1)]
    visited = {(0, 1)}
    parents: dict[tuple[int, int], tuple[int, int] | None] = {(0, 1): None}

    while stack:
        row, col = stack.pop()

        if row == maze.num_rows - 1 and col == maze.num_cols - 2:
            path = []
            current = (row, col)
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (
                0 <= new_row < maze.num_rows
                and 0 <= new_col < maze.num_cols
                and maze.matrix[new_row][new_col] == 0
                and (new_row, new_col) not in visited
            ):
                visited.add((new_row, new_col))
                parents[(new_row, new_col)] = (row, col)
                stack.append((new_row, new_col))

    return None
