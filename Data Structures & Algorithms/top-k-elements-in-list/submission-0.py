class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for freq, v in count.items():
            arr.append([v, freq])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res