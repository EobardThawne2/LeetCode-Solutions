class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        if len(s) < 4 or len(s) > 12:
            return res    
        def backtrack(i, path):
            if len(path) == 4 and i == len(s):
                res.append(".".join(path))
                return
            if len(path) == 4:
                return
            for j in range(i, min(i + 3, len(s))):
                segment = s[i:j+1]
                if len(segment) > 1 and segment[0] == '0':
                    continue
                if int(segment) <= 255:
                    path.append(segment)     
                    backtrack(j + 1, path)    
                    path.pop()                 
        backtrack(0, [])
        return res