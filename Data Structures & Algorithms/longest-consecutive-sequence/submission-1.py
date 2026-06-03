class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # Some way to identify the start of the sequence?
        # The start of the sequence is only considered the 'start'
        # if there is no number num - 1 that exists
        if len(nums) == 0:
            return 0
            
        nums_set = set(nums)
        starters = []

        for num in nums:
            if num - 1 in nums_set:
                # NOT a starter
                continue
            else:
                starters.append(num)

        print(starters)
        print(nums_set)
        max_res = 1
        for start in starters:
            res = 1
            plus_one = start + 1
            print(f"res:{res}, plus_one:{plus_one}, max_res:{max_res}")
            while plus_one in nums_set:
                res += 1
                plus_one += 1
                print(f"res:{res}, plus_one:{plus_one}, max_res:{max_res}")

            max_res = max(res, max_res)
            print(f"max_res:{max_res}")

        return max_res