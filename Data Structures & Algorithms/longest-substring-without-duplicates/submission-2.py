class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        res = 0

        l = 0
        r = 0

        str_set = set()

        while r < len(s):

            if s[r] in str_set:
                if s[l] == s[r]:
                    str_set.remove(s[l])
                    l += 1
                else:
                    while s[l] != s[r]:
                        str_set.remove(s[l])
                        l += 1
                    str_set.remove(s[l])
                    l += 1

            str_set.add(s[r])
            res = max(res, r - l + 1)
            r += 1

            

        return res