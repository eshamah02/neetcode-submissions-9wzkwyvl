class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        for l in s:
            if l in s_hash:
                s_hash[l] += 1
            else:
                s_hash[l] = 1

        for l in t:
            if l in t_hash:
                t_hash[l] += 1
            else:
                t_hash[l] = 1

        if s_hash != t_hash:
            return False
        return True

        # s = sorted(s)
        # t = sorted(t)

        # if s != t:
        #     return False
        # return True