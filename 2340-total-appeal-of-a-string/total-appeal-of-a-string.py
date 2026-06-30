class Solution:
    def appealSum(self, s: str) -> int:
        last_seen = {}
        total_appeal = 0
        current_appeal = 0
        for i, char in enumerate(s):
            last_pos = last_seen.get(char, -1)
            current_appeal += (i - last_pos)
            total_appeal += current_appeal
            last_seen[char] = i
        return total_appeal