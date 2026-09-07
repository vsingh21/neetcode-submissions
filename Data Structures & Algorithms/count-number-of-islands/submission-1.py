class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def bfs(pos):
            for d in dirs:
                i = pos[0] + d[0]
                j = pos[1] + d[1]
                if i in range(height) and j in range(width) and grid[i][j] == "1":
                    grid[i][j] = "0"
                    bfs((i,j))

        result = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    result += 1
                    bfs((i, j))
        
        return result
