class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        count = 0
        for i, char in enumerate(s):
            last_seen[char] = i
            min_index = min(last_seen['a'], last_seen['b'], last_seen['c'])
            if min_index != -1:
                count += (min_index + 1)
        return count