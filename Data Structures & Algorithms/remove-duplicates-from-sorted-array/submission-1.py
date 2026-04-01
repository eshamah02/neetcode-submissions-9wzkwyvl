class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1

        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                r += 1
                l += 1
            else:
                r += 1
        return l


            

        
        
        # p1, p2 = 0, 1

        # while p2 < len(nums):
        #     if nums[p1] == nums[p2]:
        #         nums.pop(p2)
        #     else:
        #         p1 += 1
        #         p2 += 1
        
        # return len(nums)