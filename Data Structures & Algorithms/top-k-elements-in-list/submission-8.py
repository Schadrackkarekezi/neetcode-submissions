class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        
        counts = sorted(count, reverse=True)

        arr = []
        for nun in counts:
            arr.append(nun)
        result = []
        i = 0
        while i < k:
            result.append(arr[i])
            i=i+1
        return result




            

        

