from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, dist in roads:
            graph[u].append((v, dist))
            graph[v].append((u, dist))
        visited = [False] * (n + 1)
        visited[1] = True
        stack = [1]
        min_score = float('inf')
        while stack:
            node = stack.pop()
            for neighbor, distance in graph[node]:
                if distance < min_score:
                    min_score = distance
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return min_score