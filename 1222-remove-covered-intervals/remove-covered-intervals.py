class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        remaining = 0
        prev_start = -1
        max_end = -1
        for start, end in intervals:
            if end > max_end:
                if start == prev_start:
                    max_end = end
                else:
                    remaining += 1
                    max_end = end
                    prev_start = start
        return remaining