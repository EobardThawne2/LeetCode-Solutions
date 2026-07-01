class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        dist = [[-1] * n for _ in range(n)]
        queue = []
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    dist[r][c] = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q_idx = 0
        while q_idx < len(queue):
            r, c = queue[q_idx]
            q_idx += 1  
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        def can_reach(safeness: int) -> bool:
            if dist[0][0] < safeness or dist[n-1][n-1] < safeness:
                return False
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            path_queue = [(0, 0)]
            path_idx = 0
            while path_idx < len(path_queue):
                r, c = path_queue[path_idx]
                path_idx += 1
                if r == n - 1 and c == n - 1:
                    return True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if dist[nr][nc] >= safeness:
                            visited[nr][nc] = True
                            path_queue.append((nr, nc))
            return False
        low, high = 0, n * 2
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_reach(mid):
                ans = mid   
                low = mid + 1
            else:
                high = mid - 1
        return ans