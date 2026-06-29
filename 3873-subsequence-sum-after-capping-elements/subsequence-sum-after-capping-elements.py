class Solution:
    def subsequenceSumAfterCapping(self, nums: list[int], k: int) -> list[bool]:
        n = len(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[num] += 1
        greater_or_equal = n
        dp = 1
        mask = (1 << (k + 1)) - 1
        ans = []
        for x in range(1, n + 1):
            T_x = greater_or_equal
            possible = False
            max_c = min(T_x, k // x)
            for c in range(max_c + 1):
                target = k - c * x
                if (dp >> target) & 1:
                    possible = True
                    break
            ans.append(possible)
            if x <= k:
                for _ in range(count[x]):
                    dp |= (dp << x)
                dp &= mask
            greater_or_equal -= count[x]
        return ans