import sys
import math
sys.setrecursionlimit(100000)
class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        max_cost = 0
        for u, v, c in edges:
            if online[u] and online[v]:
                adj[u].append((v, c))
                if c > max_cost:
                    max_cost = c
        def check(min_score: int) -> bool:
            memo = [-1] * n
            def dfs(u: int) -> int:
                if u == n - 1:
                    return 0
                if memo[u] != -1:
                    return memo[u]
                res = math.inf
                for v, cost in adj[u]:
                    if cost >= min_score:
                        res = min(res, cost + dfs(v))
                memo[u] = res
                return res
            return dfs(0) <= k
        low, high = 0, max_cost
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans