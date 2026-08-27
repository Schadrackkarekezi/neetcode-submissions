class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        for i , num in count.items():
            arr.append(num)
        arr.sort()
        return arr[:k]
        




            

        

