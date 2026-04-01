class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sort_str = {}
        final = []

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in sort_str:
                sort_str[sorted_s].append(s)
            else:
                sort_str[sorted_s] = [s]

        for k, v in sort_str.items():
            final.append(v)

        return final
                