# https://neetcode.io/problems/count-number-of-islands
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# Input: grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
# Output: 1

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
        islands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])


        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r >=0 and r < ROWS) and 
                        (c >=0 and c < COLS) and
                        (r, c) not in visited and 
                        grid[r][c] == "1"):
                        q.append((r, c))
                        visited.add((r, c))


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        return islands
