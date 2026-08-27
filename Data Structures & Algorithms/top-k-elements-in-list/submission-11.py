class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        counts =[]
        for j in nums:
            count[j] = 1 + count.get(j, 0)
        counts = sorted(count, key=counts.get,reverse=True)[:k]
        return counts
        




            

        

