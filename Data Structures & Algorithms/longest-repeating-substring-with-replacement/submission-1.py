class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0
        
        for char in set(s):
            for l in range(len(s)):
                counter_k = 0
                r = l
                while r < len(s):
                    if s[r] != char:
                        counter_k += 1
                        if counter_k > k:
                            break
                    r += 1
                res = max(res, r - l)
        
        return res