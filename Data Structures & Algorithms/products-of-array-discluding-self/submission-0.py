class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pre_prods = []
        suf_prods = [1] * len(nums)

        for n in range(len(nums)):
            total = 1
            total = nums[n - 1] * pre_prods[n - 1] if n > 0 else total * 1
            pre_prods.append(total)

        for n in range(len(nums) - 1, -1, -1):
            # print(n)
            total = 1
            total = nums[n + 1] * suf_prods[n + 1] if n < len(nums) - 1 else total * 1
            suf_prods[n] = total

        # print(pre_prods)
        # print(suf_prods)
        res = [1] * len(nums)
        for n in range(len(nums)):
            res[n] = pre_prods[n] * suf_prods[n]

        return res
