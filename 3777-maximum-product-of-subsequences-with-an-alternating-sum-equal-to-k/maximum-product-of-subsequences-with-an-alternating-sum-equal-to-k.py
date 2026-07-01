from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        dp0 = defaultdict(set)
        dp1 = defaultdict(set)
        OVERFLOW = limit + 1
        for x in nums:
            ndp0 = defaultdict(set, {s: prods.copy() for s, prods in dp0.items()})
            ndp1 = defaultdict(set, {s: prods.copy() for s, prods in dp1.items()})
            ndp1[x].add(x if x <= limit else OVERFLOW)
            if x == 0:
                for s in dp0:
                    ndp1[s].add(0)
                for s in dp1:
                    ndp0[s].add(0)
            elif x == 1:
                for s, prods in dp0.items():
                    ndp1[s + 1].update(prods)
                for s, prods in dp1.items():
                    ndp0[s - 1].update(prods)
            else:
                for s, prods in dp0.items():
                    ndp1[s + x].update({p * x if p * x <= limit else OVERFLOW for p in prods})
                for s, prods in dp1.items():
                    ndp0[s - x].update({p * x if p * x <= limit else OVERFLOW for p in prods})
            dp0, dp1 = ndp0, ndp1
        ans = -1
        if k in dp0:
            valid = [p for p in dp0[k] if p <= limit]
            if valid: ans = max(ans, max(valid))
        if k in dp1:
            valid = [p for p in dp1[k] if p <= limit]
            if valid: ans = max(ans, max(valid))
        return ans