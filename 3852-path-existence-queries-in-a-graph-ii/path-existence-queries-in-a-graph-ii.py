class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        unique_vals = sorted(list(set(nums)))
        M = len(unique_vals)
        val_to_idx = {val: i for i, val in enumerate(unique_vals)}
        L = [0] * M
        R = [0] * M
        left = 0
        for i in range(M):
            while unique_vals[i] - unique_vals[left] > maxDiff:
                left += 1
            L[i] = left
        right = 0
        for i in range(M):
            while right < M and unique_vals[right] - unique_vals[i] <= maxDiff:
                right += 1
            R[i] = right - 1
        LOG = 18 # 2^17 is > 100,000 (max N)
        upL = [[0] * LOG for _ in range(M)]
        upR = [[0] * LOG for _ in range(M)]
        for i in range(M):
            upL[i][0] = L[i]
            upR[i][0] = R[i]
        for j in range(1, LOG):
            for i in range(M):
                upL[i][j] = upL[upL[i][j-1]][j-1]
                upR[i][j] = upR[upR[i][j-1]][j-1]
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            valU, valV = nums[u], nums[v]
            if abs(valU - valV) <= maxDiff:
                ans.append(1)
                continue
            startIdx = val_to_idx[valU]
            targetIdx = val_to_idx[valV]
            if startIdx < targetIdx:
                if upR[startIdx][LOG - 1] < targetIdx:
                    ans.append(-1) # Impossible to reach
                else:
                    curr = startIdx
                    steps = 0
                    for j in range(LOG - 1, -1, -1):
                        if upR[curr][j] < targetIdx:
                            curr = upR[curr][j]
                            steps += (1 << j)
                    ans.append(steps + 1)
            else:
                if upL[startIdx][LOG - 1] > targetIdx:
                    ans.append(-1) # Impossible to reach
                else:
                    curr = startIdx
                    steps = 0
                    for j in range(LOG - 1, -1, -1):
                        if upL[curr][j] > targetIdx:
                            curr = upL[curr][j]
                            steps += (1 << j)
                    ans.append(steps + 1)
        return ans