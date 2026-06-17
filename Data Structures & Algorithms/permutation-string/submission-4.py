class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import string
        if len(s1) > len(s2):
            return False

        s1_list = [0] * 26
        s2_list = [0] * 26

        for c in s1:
            s1_list[string.ascii_lowercase.index(c)] += 1

        print(s1_list)

        l = 0
        r = 0

        while r < len(s1):
            idx_r = string.ascii_lowercase.index(s2[r])
            s2_list[idx_r] += 1
            r += 1

        if s1_list == s2_list:
                return True

        print(s2_list)

        while r < len(s2):
            
            idx_l = string.ascii_lowercase.index(s2[l])
            idx_r = string.ascii_lowercase.index(s2[r])

            s2_list[idx_l] -= 1
            s2_list[idx_r] += 1

            print(s2_list)

            l += 1
            r += 1

            if s1_list == s2_list:
                return True

        return False

        


        


