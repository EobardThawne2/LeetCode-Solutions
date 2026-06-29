class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  
        max_len = 1
        if 1 in freq:
            count = freq[1]
            # Must be an odd number of 1s
            max_len = count if count % 2 == 1 else count - 1
        for num in freq:
            if num == 1:
                continue
            curr_len = 0
            curr = num
            while freq.get(curr, 0) >= 2 and (curr * curr) in freq:
                curr_len += 2
                curr = curr * curr
            curr_len += 1
            if curr_len > max_len:
                max_len = curr_len    
        return max_len