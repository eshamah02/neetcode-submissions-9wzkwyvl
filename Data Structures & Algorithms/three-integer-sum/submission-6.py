class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(f"sorted nums: {nums}")

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -1 * nums[i]
            j = i + 1
            k = len(nums) - 1

            # print(f"i:{nums[i]}, j:{nums[j]}, k:{nums[k]}")
            while j < k: 
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    print(f"adding to res:[{nums[i], nums[j], nums[k]}]")
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                # print(f"i:{nums[i]}, j:{nums[j]}, k:{nums[k]}")
        return res


