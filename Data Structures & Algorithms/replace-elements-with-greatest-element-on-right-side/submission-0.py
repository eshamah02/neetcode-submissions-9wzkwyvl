class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_element = arr[-1]
        for l in range(len(arr) - 1, -1, -1):
            if l == len(arr) - 1:
                arr[l] = -1
            else:
                current_val = arr[l]
                arr[l] = max_element
                max_element = max(current_val, max_element)
            # max_element = max(arr[l + 1], max_element)


        return arr