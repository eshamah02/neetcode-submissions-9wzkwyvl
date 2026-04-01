class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i, n in enumerate(nums):
            vals[n] = i

        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in vals and vals[diff] != i:
                return [i, vals[diff]]
        
        return []
