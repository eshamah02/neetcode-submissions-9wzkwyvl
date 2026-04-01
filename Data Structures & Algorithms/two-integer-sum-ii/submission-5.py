class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        r = 1

        for l in range(len(numbers)):
            r = l + 1
            while r < len(numbers):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                else:
                    r += 1
            

