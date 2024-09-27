def num_islands(grid):
    if not grid or len(grid) == 0:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()  # To keep track of visited land cells
    islands = 0

    # Helper function for Depth-First Search (DFS)
    def dfs(r, c):
        # If we're out of bounds, hit water, or the cell is already visited, stop.
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == 'W' or (r, c) in visited):
            return
        
        # Mark the cell as visited
        visited.add((r, c))
        
        # Visit all neighboring cells (up, down, left, right)
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    # Loop through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If it's an unvisited land cell, start a DFS and count a new island
            if grid[r][c] == 'L' and (r, c) not in visited:
                islands += 1  # Found a new island
                dfs(r, c)  # Mark all land cells connected to this one

    return islands