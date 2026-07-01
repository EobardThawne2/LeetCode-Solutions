from typing import List
from collections import defaultdict
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        dp = defaultdict(set)
        OVERFLOW = limit + 1
        for x in nums:
            updates = []
            app = updates.append 
            app((x, 1, x if x <= limit else OVERFLOW))
            for (s, sign), prods in dp.items():
                new_s = s + x if sign == 0 else s - x
                new_sign = 1 - sign
                for p in prods:
                    np = p * x
                    if np > limit:
                        np = OVERFLOW
                    app((new_s, new_sign, np))
            for s, sign, p in updates:
                dp[(s, sign)].add(p)
        ans = -1
        for sign in (0, 1):
            if (k, sign) in dp:
                for p in dp[(k, sign)]:
                    if p <= limit and p > ans:
                        ans = p
        return ans