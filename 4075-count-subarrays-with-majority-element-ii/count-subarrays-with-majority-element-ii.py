class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        counts = [0] * ((n << 1) + 2) 
        curr = n
        counts[curr] = 1
        ans = 0
        smaller = 0
        for num in nums:
            if num == target:
                smaller += counts[curr]
                curr += 1
            else:
                curr -= 1
                smaller -= counts[curr]    
            ans += smaller
            counts[curr] += 1   
        return ans