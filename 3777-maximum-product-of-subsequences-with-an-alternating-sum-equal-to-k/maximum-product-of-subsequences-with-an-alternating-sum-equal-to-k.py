from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        dp = defaultdict(set)
        OVERFLOW = limit + 1
        for x in nums:
            next_dp = defaultdict(set)
            for state, prods in dp.items():
                next_dp[state] = prods.copy()
            initial_p = x if x <= limit else OVERFLOW
            next_dp[(x, 1)].add(initial_p)
            for (s, sign), prods in dp.items():
                new_s = s + x if sign == 0 else s - x
                new_sign = 1 - sign
                for p in prods:
                    np = p * x
                    if np > limit:
                        np = OVERFLOW
                    next_dp[(new_s, new_sign)].add(np)
            dp = next_dp
        ans = -1
        for sign in (0, 1):
            if (k, sign) in dp:
                valid_prods = [p for p in dp[(k, sign)] if p <= limit]
                if valid_prods:
                    ans = max(ans, max(valid_prods))
        return ans