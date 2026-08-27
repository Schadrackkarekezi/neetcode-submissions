class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        
        counts = sorted(count)

        arr = []
        for nun in counts:
            arr.append(num)
        result = []
        while i < k:
            result.append(arr[i])
        
        return result




            

        

