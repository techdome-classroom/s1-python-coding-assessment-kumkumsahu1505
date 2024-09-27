class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 'W' or (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and (i, j) not in visited:
                    islands += 1
                    dfs(i, j)

        return islands
