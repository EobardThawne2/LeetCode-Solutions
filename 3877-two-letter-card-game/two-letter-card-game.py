class Solution:
    def score(self, cards: list[str], x: str) -> int:
        cnt1 = [0] * 10  
        cnt2 = [0] * 10  
        both = 0         
        for c in cards:
            if c[0] == x and c[1] == x:
                both += 1
            elif c[0] == x:
                cnt1[ord(c[1]) - ord('a')] += 1
            elif c[1] == x:
                cnt2[ord(c[0]) - ord('a')] += 1
        sum1, max1 = sum(cnt1), max(cnt1) if cnt1 else 0
        sum2, max2 = sum(cnt2), max(cnt2) if cnt2 else 0
        max_score = 0
        for give_to_first in range(both + 1):
            have1 = give_to_first
            have2 = both - give_to_first
            tot1 = sum1 + have1
            mx1 = max1 if max1 > have1 else have1
            score1 = min(tot1 // 2, tot1 - mx1)
            tot2 = sum2 + have2
            mx2 = max2 if max2 > have2 else have2
            score2 = min(tot2 // 2, tot2 - mx2)
            if score1 + score2 > max_score:
                max_score = score1 + score2
        return max_score