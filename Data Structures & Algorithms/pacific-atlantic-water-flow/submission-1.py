class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific
        ROWS, COLS = len(heights), len(heights[0])
        q = deque()
        fromPacific = set()
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            fromPacific.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and heights[r][c] <= heights[nr][nc] and (nr, nc) not in fromPacific:
                    q.append((nr, nc))
        
        q = deque()
        fromAtlantic = set()

        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1:
                    q.append((r, c))
        while q:
            r, c = q.popleft()
            fromAtlantic.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr in range(ROWS) and nc in range(COLS) and heights[r][c] <= heights[nr][nc] and (nr, nc) not in fromAtlantic:
                    q.append((nr, nc))
        
        res = []
        for r, c in fromPacific.intersection(fromAtlantic):
            res.append([r,c])
        return res
        

