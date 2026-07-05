class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 10**9 + 7
        n = len(board)
        dp_score = [[-1] * n for _ in range(n)]
        dp_paths = [[0] * n for _ in range(n)]
        dp_score[n-1][n-1] = 0
        dp_paths[n-1][n-1] = 1
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == n - 1 and c == n - 1) or board[r][c] == 'X':
                    continue
                max_prev_score = -1
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    prev_r, prev_c = r + dr, c + dc
                    if prev_r < n and prev_c < n and dp_score[prev_r][prev_c] != -1:
                        if dp_score[prev_r][prev_c] > max_prev_score:
                            max_prev_score = dp_score[prev_r][prev_c]
                if max_prev_score != -1:
                    current_points = int(board[r][c]) if board[r][c] != 'E' else 0
                    dp_score[r][c] = max_prev_score + current_points
                    for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                        prev_r, prev_c = r + dr, c + dc
                        if prev_r < n and prev_c < n and dp_score[prev_r][prev_c] == max_prev_score:
                            dp_paths[r][c] = (dp_paths[r][c] + dp_paths[prev_r][prev_c]) % MOD
        if dp_score[0][0] == -1:
            return [0, 0]
        return [dp_score[0][0], dp_paths[0][0]]