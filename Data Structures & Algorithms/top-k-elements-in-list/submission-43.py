class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        heap = []

        for num in counter.keys():
            heapq.heappuh(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res







    
        
     
        


        




            

        



