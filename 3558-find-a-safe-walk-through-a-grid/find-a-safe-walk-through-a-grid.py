from collections import deque
import math
class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = grid[0][0]
        q = deque([(0, 0)])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    cost = grid[nx][ny]
                    if dist[x][y] + cost < dist[nx][ny]:
                        dist[nx][ny] = dist[x][y] + cost
                        if cost == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return dist[-1][-1] < health