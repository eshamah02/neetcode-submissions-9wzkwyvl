class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for l in range(len(numbers)):
            r = l + 1
            print(f"l:{l}, r:{r}")
            while r < len(numbers):
                if numbers[r] + numbers[l] == target:
                    return [l + 1, r + 1]
                else:
                    r += 1



